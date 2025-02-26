# Homework 3 Calculator
# This is Homework 4 checkpoint

# Project Install Instructions

## install 
1. clone
2. pip install -r requirements.txt
    NOTE: i had to modify from the original instructions, there is an additional line adding from the 2nd homework video
    NOTE: i did this because i had a problem running pylint --pytest as in the 2nd homework video, so i reinstalled with "pip install pytest-pylint", and then i tried freezing it to a new txt file and it gave me an extra line of requirements than what i originally had; this should fix the issue but install as normal

## testing
1. pytest
2. pytest --pylint
3. pytest --pylint --cov
4. pytest --num_records=10

-note: tests for the operation and calculation classes are in test_calculator.py, and tests for the history and calculator classes are in test_history.py
The Calculator class is in __init__.py, and it is the main class for running calculations, history, and operations in one go

-note: i am also convinced that my slight loss of coverage in tests/test_for_num_records.py, and conftest.py 
is due to the if-statements and except statements not being run if i don't run into a case it matches,
but i don't want the test to fail either, so that is my explanation of why there is a slight loss of coverage
-test_command.py doesn't get to the exception case in plugins/add, plugins/subtract, plugins/multiply, and plugins/divide, 
so that explains the loss of coverage there as well; goes through all other cases though
-for the main.py function loss of coverage, i didn't know how to test the main function itself, so that's why it is so low;
i also was not able to figure out how to trigger the exception as {e} exception case, so that accounts for another missed line


## requirements
1. add, subtract, multiply, divide
2. throw exception for divide by zero and test that the exception is thrown
3. use at least one class, at least one static method, at least one class method
4. it needs to store a history of calculations, so that you can retrieve the last calculation, add a calculation
5. it needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code
6. you should use type hints for input parameter types and return types 
7. implement a pytest fixture
