'''Test configuration for test_for_num_records.py and new configuration to test a number of records'''
from typing import Callable, List
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operation import Operation

fake = Faker()

def pytest_addoption(parser):
    '''This function interprets the command line through pytest'''
    #parser interprets command line
    parser.addoption("--num_records", action = "store", default = 10, type = int, help = "Number of test records to generate")

def new_test_data(num_records):
    '''This function makes test data for _ in range(num_records)'''
    operationslist: List[Callable[[Decimal, Decimal], Decimal]] = [Operation.add, Operation.subtract, Operation.multiply, Operation.divide] #organized this differently than example because i am not using name of operation
    for _ in range(num_records):
        a: Decimal = fake.random_number()
        b: Decimal = fake.random_number()
        operfunc: Callable[[Decimal, Decimal], Decimal] = fake.random_element(operationslist)
        expected = 0
        try:
            expected = operfunc(a, b)
        except ValueError:
            with pytest.raises(ValueError, match="Division by zero"):
                expected = operfunc(a, b)
        yield a, b, operfunc, expected


def pytest_generate_tests(metafunc):
    '''This function takes all of the data that's in newparameters and puts it into anything that looks like "a,b,oper,expected" like in metafunc.parametrize'''
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)): #this checks if test is expecting any of these dynamically generated fixtures
        num_records = metafunc.config.getoption("num_records") # this is from the pytest_addoption function where we get this value
        parameters = list(new_test_data(num_records - 1))
        parameters.append((1, 0, Operation.divide, "ValueError: Division by zero")) #manually added a test that was getting missed all the time
        metafunc.parametrize("a,b,oper,expected", parameters) # parameterize is spelled parametrize !!!
        # this metafunc.parameterize is setting a, b, operation, expected in a test to these values
