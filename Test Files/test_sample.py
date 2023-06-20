from myClasses.UVSim_Class import UVSim
# To run these tests, open a terminal and run "pytest" in the terminal to check if tests pass.

#test that checks the fetch function 
def test_fetch():
    sim = UVSim()
    sim.memory[0] = 1002  # opcode 10 and operand 02
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

#Tests the execute function with the op_code 10 READ
def test_execute_op_code_10():
    sim = UVSim()
    sim.operation_code = 10
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 11 WRITE
def test_execute_op_code_11():
    sim = UVSim()
    sim.operation_code = 11
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 20 LOAD
def test_execute_op_code_20():
    sim = UVSim()
    sim.operation_code = 20
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 21 STORE
def test_execute_op_code_21():
    sim = UVSim()
    sim.operation_code = 21
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 30 ADD
def test_execute_op_code_30():
    sim = UVSim()
    sim.operation_code = 30
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 31 SUBTRACT
def test_execute_op_code_31():
    sim = UVSim()
    sim.operation_code = 31
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 32 DIVIDE
def test_execute_op_code_32():
    sim = UVSim()
    sim.operation_code = 32
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 33 MULTIPLY
def test_execute_op_code_33():
    sim = UVSim()
    sim.operation_code = 33
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 40 BRANCH
def test_execute_op_code_40():
    sim = UVSim()
    sim.operation_code = 40
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 41 BRANCHNEG
def test_execute_op_code_41():
    sim = UVSim()
    sim.operation_code = 41
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 42 BRANCHZERO
def test_execute_op_code_42():
    sim = UVSim()
    sim.operation_code = 42
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."

#Tests the execute function with the op_code 43 Halt
def test_execute_op_code_43():
    sim = UVSim()
    sim.operation_code = 43
    
    assert sim.execute() == "Program halted."
    assert sim.execute() != "Bluey halted."


def test_reading_in_filename():
        sim = UVSim()
        filename = "Test1.txt"
        sim.load(filename)
        # Assert the desired behavior based on the loaded file
        expected_memory = [+1007, +1008, +2007, +2008, +2109, +1109, +4300, +0000, +0000, +0000, -99999]
        assert sim.memory[:len(expected_memory)] == expected_memory

