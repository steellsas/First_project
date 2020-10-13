from create_db import Employeer
import json

is_work_more_3 = lambda x: x >= 3

e_data = {}
f_data = {}
result = ''

# Read from JSON files
with open("company_employees (1).json", 'r') as e_file:
    e_data = json.load(e_file)

with open("feedback_for_employees (1).json", 'r') as e_file:
    f_data = json.load(e_file)


def dict_to_string(dict_c):
    s = []
    for i in dict_c.keys():
        s.append(dict_c[i])
    listToStr = ' '.join(map(str, s))
    return listToStr

str12 = None
str_list = []

# Merge two dict  if  emails egual
for first_d_key11 in e_data.keys():
    # Employee dict
    for dict_a in e_data[first_d_key11]:

        # Feedback dict
        for first_d_key2 in f_data.keys():
            # feedback dict
            for dict_b in f_data[first_d_key2]:
                if dict_a['emailAddress'] == dict_b['emailAddress']:
                    dict_c = dict_a.copy()
                    dict_c.update(dict_b)
                    if is_work_more_3(dict_c["years_employed"]):
                        str12 = dict_to_string(dict_c)
            if str12 :
                str_list.append(str12)

for sentence1 in str_list:
  empl1 = Employeer.create_from_string(sentence1)
