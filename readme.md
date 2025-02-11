# Homework 3 Calculator

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

-note: tests for the operation and calculation classes are in test_calculator.py, and tests for the history and calculator classes are in test_history.py
The Calculator class is in __init__.py, and it is the main class for running calculations, history, and operations in one go

## requirements
1. add, subtract, multiply, divide
2. throw exception for divide by zero and test that the exception is thrown
3. use at least one class, at least one static method, at least one class method
4. it needs to store a history of calculations, so that you can retrieve the last calculation, add a calculation
5. it needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code
6. you should use type hints for input parameter types and return types 
7. implement a pytest fixture
