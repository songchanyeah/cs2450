import pytest
from UVSim_Class import UVSim
# To run these tests, open a terminal and run "pytest" in the terminal to check if tests pass.

#test that checks the fetch function 
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

# testing UVSim class constructor
def test_UVSim():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 100
    assert uvsim.accumulator == 0
    assert uvsim.instruction_counter == 0
    assert uvsim.instruction_register == 0
    assert uvsim.operation_code == 0
    assert uvsim.operand == 0

#test that checks the load function
def test_load():
    sim = UVSim()
    sim.load('Test1.txt')
    expected_memory = [+1007, +1008, +2007, +2008, +2109, +1109, +4300, +0000, +0000, +0000, -99999]

    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'

#another test for the fetch function
def test_new_fetch_update():
    sim = UVSim()

    sim.load('Test1.txt')
    sim.fetch()

    assert sim.instruction_register == +\
        1007, f'Expected instruction register to be +1007, but got {sim.instruction_register}'
    assert sim.operation_code == 10, f'Expected operation code 10, but got {sim.operation_code}'
    assert sim.operand == 7, f'Expected operand 07, but got {sim.operand}'


def test_execute():
    sim = UVSim()
    sim.operation_code = 43
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."