import pytest
from main import main, UVSim

#To run these tests, open a terminal and run "pytest" in the terminal to check if tests pass.


#tutorial function for test number 1
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

#tutorial function and test number 2
def f():
    raise SystemExit(1)

def test_fetch():
    sim = UVSim()
    sim.memory[0] = 1002 # opcode 10 and operand 01
    sim.memory[1] = 2130 # opcode 21 and operand 30
    sim.memory[2] = 4300 # opcode 43 and operand 00
    sim.memory[3] = 0000 # opcode 00 and operand 00
    sim.memory[4] = 0000 # opcode 00 and operand 00
    sim.memory[5] = 0000 # opcode 00 and operand 00
    
    sim.fetch()
    assert sim.operation_code == 10
    assert sim.operand == 2

def test_mytest():
    with pytest.raises(SystemExit):
        f()

#function for testing main in main.py returns a 1 integer
def test_main():
    assert main() == 1

#testing UVSim class constructor
def test_UVSim():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 100
    assert uvsim.accumulator == 0
    assert uvsim.instruction_counter == 0
    assert uvsim.instruction_register == 0
    assert uvsim.operation_code == 0
    assert uvsim.operand == 0