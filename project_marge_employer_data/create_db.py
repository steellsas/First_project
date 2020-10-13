import sqlite3
import re


class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def create_employee_table():
        query = """CREATE TABLE Employees(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    role TEXT,
                    annual_salary FLOAT,
                    feedback INTEGER,
                    years_employed INTEGER,
                    email TEXT)"""
        with DatabaseContextManager("employees") as db:
            db.execute(query)

    def create_employee(first_name: str, last_name: str, role: str, annual_salary: float, feedback: int,
                        years_employed: int, email: str):
        query = f"""INSERT INTO Employees(first_name, last_name, role, annual_salary, feedback, years_employed, email) 
                    VALUES('{first_name}','{last_name}','{role}',{annual_salary},'{feedback}','{years_employed}', '{email}')"""
        with DatabaseContextManager("employees") as db:
            db.execute(query)

    def get_employees():
        query = f"SELECT * FROM Employees"
        with DatabaseContextManager("employees") as db:
            data = db.execute(query)
            for record in data:
                print(record)

    def delete_employee(email: str):
        query = f"DELETE FROM Employees WHERE email = '{email}'"
        with DatabaseContextManager("employees") as db:
            db.execute(query)


class Employeer:
    def __init__(self, name, last_name, role, annual_salary, feedback, years_employed, email):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.feedback = feedback
        self.annual_salary = annual_salary
        self.years_employed = years_employed

    def __str__(self):
        return f"{self.name},{self.last_name}"

    @classmethod
    def create_from_string(cls, sentence):
        name, last_name, annual_salary, years_employed, email, feedback, role = sentence.split(' ')
        annual_salary, years_employed, feedback = int(annual_salary), int(years_employed), int(feedback)
        if cls.validate_email(email):
            return cls(name, last_name, email, feedback, role, annual_salary, years_employed)

    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        return False
