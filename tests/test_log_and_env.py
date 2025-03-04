'''My Tests for Environment Variables and Logging'''
import pytest
import os
from pathlib import Path
from datetime import datetime
from interface import Interface

def test_exists_log_file():
    '''Test to show at least one file is in logs file'''
    # note that i could check the name of the filehere, however i am 
    # adding log files down to the minute so it would be hard
    # to make this test pass running everything under a minute
    assert any(Path("logs").iterdir()) == True

#def test_env_var():
    #'''Test to test that environment variable is inside of Interface'''
    # really just showing that i have one and i can get it from the Interface
    #myInterface: Interface = Interface.newInterface()
    #assert myInterface.getEnv() == {key: value for key, value in os.environ.items()}