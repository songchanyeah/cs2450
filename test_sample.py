import pytest

from main import main, UVSim

# To run these tests, open a terminal and run "pytest" in the terminal to check if tests pass.


# tutorial function for test number 1
def func(x):
    return x + 1



# tutorial function and test number 2


def f():
    raise SystemExit(1)


def test_fetch():
    sim = UVSim()
    sim.memory[0] = 1002  # opcode 10 and operand 01
    sim.memory[1] = 2130  # opcode 21 and operand 30
    sim.memory[2] = 4300  # opcode 43 and operand 00
    sim.memory[3] = 0000  # opcode 00 and operand 00
    sim.memory[4] = 0000  # opcode 00 and operand 00
    sim.memory[5] = 0000  # opcode 00 and operand 00

    sim.fetch()
    assert sim.operation_code == 10
    assert sim.operand == 2

###DENIS
def test_load():
    ohno = UVSim()
    ohno.load('badtest1.txt')
    expected_memory = [ +1010, +20+07, +20+09, -1110, +1o0O, 3100+, -+1100, -----, +9999, -4300, -0000, +4300, -0000, +0000, +0000 ,-99999]
    assert ohno.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {ohno.memory[:len(expected_memory)]}'

def test_fetch():
    ohno = UVSim()
    ohno.load('Test1.txt')
    ohno.fetch()
    assert ohno.instruction_register == +1007, f'Expected instruction register to be +1007, but got {ohno.instruction_register}'
    assert ohno.operation_code == 10, f'Expected operation code 10, but got {ohno.operation_code}'
    assert ohno.operand == 7, f'Expected operand 07, but got {ohno.operand}'
#test made to fail to check for cheaters and other things
###DENIS

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# function for testing main in main.py returns a 1 integer


def test_main():
    assert main() == 1

# testing UVSim class constructor


def test_UVSim():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 100
    assert uvsim.accumulator == 0
    assert uvsim.instruction_counter == 0
    assert uvsim.instruction_register == 0
    assert uvsim.operation_code == 0
    assert uvsim.operand == 0
