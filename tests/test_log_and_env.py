'''My Tests for Environment Variables and Logging'''
from pathlib import Path
import pytest
from interface import Interface

def test_exists_log_file():
    '''Test to show at least one file is in logs file'''
    # note that i could check the name of the filehere, however i am
    # adding log files down to the minute so it would be hard
    # to make this test pass running everything under a minute
    assert any(Path("logs").iterdir()) is True

@pytest.fixture
def myinterface():
    '''setting an interface here so pytest knows it is being used'''
    #had something weird happen that pytest wasn't being used
    return Interface.newInterface()

def test_env_var(myinterface):
    '''Test to test that environment variable is inside of Interface'''
    assert myinterface.getEnv() is not None
