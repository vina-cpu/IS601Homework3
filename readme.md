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
