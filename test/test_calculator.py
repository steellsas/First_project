from calc.calculator import Calculator
import pytest

@pytest.fixture
def answer():
    return 4

def test_calculator_multiply_is_zero():

    calt = Calculator()
    num1 = 3
    num2 = 1
    expected = 0
    with pytest.raises(Exception):
        assert calt.multiply(num1, num2)

def test_calculator_add_is_begative(answer):

    calt = Calculator()
    num1 = 2
    num2 = 2
    with pytest.raises(Exception):
        assert calt.add_1(num1, num2) == answer()

def test_calculator_add_is_zero():

    calt = Calculator()
    num1 = 0
    num2 = 1
    expected = 0

    assert calt.multiply(num1, num2) == expected

def test_calculator_add_is_zero():

    calt = Calculator()
    num1 = 1
    num2 = 1
    expected = 0

    assert calt.substract(num1, num2) == expected

def test_calculator_power_is():

    calt = Calculator()
    num1 = 5
    num2 = 2
    expected = 25

    assert calt.power(num1, num2) == expected

def test_calculator_power_is_one():

    calt = Calculator()
    num1 = 1
    num2 = 2
    expected = 1

    assert calt.power(num1, num2) ==  expected

def test_calculator_power_is():
    calt = Calculator()
    num1 = 1
    num2 = 1
    expected = 1
    assert calt.power(num1, num2) ==  expected

print("hello Worls")