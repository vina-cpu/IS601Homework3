import pytest
from interface import Interface
from command import Command, AddCommand, SubtractCommand
'''Tests for Command Design Pattern'''

def test_add_command(capsys, monkeypatch):
    '''Test AddCommand()'''
    inputs = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newadd = AddCommand()
    newadd.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "What is your first number:\nWhat is your second number:\nCalculating ... \n3"

def test_subtract_command(capsys, monkeypatch):
    '''Test SubtractCommand()'''
    inputs = iter(['1', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newsubtract = SubtractCommand()
    newsubtract.execute()
    captured = capsys.readouterr()
    assert captured.out.strip() == "What is your first number:\nWhat is your second number:\nCalculating ... \n-3"

def test_interface_start_exit_command(monkeypatch):
    '''Test that the REPL exits with 'exit' input''' 
    #this is SIMULATING USER
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    
    
    
    
    
    