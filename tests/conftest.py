import pytest
from typing import Callable, List
from faker import Faker
from calculator.operation import Operation

def pytest_addoption(parser):
    parser.addoption("--num_records", action = "store", default = 10, type = int, help = "Number of test records to generate")