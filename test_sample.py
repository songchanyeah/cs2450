import pytest
from main import main

#To run these tests, open a terminal and run "pytest" in the terminal to check if tests pass.


#tutorial function for test number 1
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

#tutorial function and test number 2
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

#function for testing main in main.py returns a 1 integer
def test_main():
    assert main() == 1