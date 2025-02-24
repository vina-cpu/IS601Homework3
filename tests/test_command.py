'''Tests for Command Design Pattern'''
import pytest
from interface import Interface
from command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand, ExitCommand
#cov due to all the try excepts which will be fixed in final submission

def test_add_command(capfd, monkeypatch):
    '''Test AddCommand()'''
    inputs = iter(['1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newadd = AddCommand()
    newadd.execute()
    captured = capfd.readouterr()
    assert "The result of 1 add 2 is equal to 3" in captured.out

def test_subtract_command(capfd, monkeypatch):
    '''Test SubtractCommand()'''
    inputs = iter(['1', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newsubtract = SubtractCommand()
    newsubtract.execute()
    captured = capfd.readouterr()
    assert "The result of 1 subtract 4 is equal to -3" in captured.out

def test_multiply_command(capfd, monkeypatch):
    '''Test MultiplyCommand()'''
    inputs = iter(['200', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newmultiply = MultiplyCommand()
    newmultiply.execute()
    captured = capfd.readouterr()
    assert "The result of 200 multiply 1 is equal to 200" in captured.out

def test_divide_command(capfd, monkeypatch):
    '''Test DivideCommand()'''
    inputs = iter(['1', '-1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    newdivide = DivideCommand()
    newdivide.execute()
    captured = capfd.readouterr()
    assert "The result of 1 divide -1 is equal to -1" in captured.out

def test_exit_command(capfd):
    '''Test ExitCommand()'''
    newexit = ExitCommand()
    with pytest.raises(SystemExit):
        newexit.execute()
    captured = capfd.readouterr()
    assert "Goodbye!" in captured.out

def test_menu_command(capfd):
    '''Test MenuCommand()'''
    newmenu = MenuCommand()
    newmenu.execute()
    captured = capfd.readouterr()
    assert "Here is a list of commands:" in captured.out

def test_interface_start_exit_command(capsys, monkeypatch):
    '''Test that the REPL exits with 'exit' input''' 
    #this is SIMULATING USER
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    inter = Interface()
    #captured = capsys.readouterr()
    #assert captured.out.strip() == "Hello! Type calculator commands to utilize the calculator, or type 'exit' to exit!"
    with pytest.raises(SystemExit):
        inter.start()

def test_interface_start_no_command(capfd, monkeypatch):
    '''Test that the REPL doesn't explode if i put in something other than a command it knows'''
    inputs = iter(['unknown command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "No such command: unknown command" in captured.out

def test_interface_start_menu_command(capfd, monkeypatch):
    '''Test that REPL can display the menu'''
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "Here is a list of commands:" in captured.out

def test_interface_start_add_command(capfd, monkeypatch):
    '''Test that the REPL can add'''
    inputs = iter(['add', '2', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "The result of 2 add 4 is equal to 6" in captured.out

def test_interface_start_subtract_command(capfd, monkeypatch):
    '''Test that the REPL can subtract'''
    inputs = iter(['subtract', '-1', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "The result of -1 subtract 2 is equal to -3" in captured.out

def test_interface_start_multiply_command(capfd, monkeypatch):
    '''Test that the REPL can multiply'''
    inputs = iter(['multiply', '3', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "The result of 3 multiply 5 is equal to 15" in captured.out

def test_interface_start_divide_command(capfd, monkeypatch):
    '''Test that the REPL can divide'''
    inputs = iter(['divide', '2', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    inter = Interface()
    with pytest.raises(SystemExit):
        inter.start()
    captured = capfd.readouterr()
    assert "The result of 2 divide 4 is equal to 0.5" in captured.out
