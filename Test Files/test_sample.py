import pytest
from myClasses.UVSim_Class import UVSim

# Test that checks the fetch function UT1
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

#UT2
def test_fetch_instruction():
    uvsim = UVSim()

    uvsim.memory = [1007, 2010, 3018, 2119, 4017]
    uvsim.instruction_counter = 2
    uvsim.fetch()

    assert uvsim.instruction_register == 3018
    assert uvsim.operation_code == 30
    assert uvsim.operand == 18

# Test the UVSim class constructor UT3
def test_UVSim_Constructor():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 100
    assert uvsim.accumulator == 0
    assert uvsim.instruction_counter == 0
    assert uvsim.instruction_register == 0
    assert uvsim.operation_code == 0
    assert uvsim.operand == 0


#UT4
def test_UVSim_Memory():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 100
    assert isinstance(uvsim.memory, list)

#UT5
def test_UVSim_Memory_Range_Error():
    uvsim = UVSim()

    with pytest.raises(IndexError):
        value = uvsim.memory[101]

#UT6
def test_UVSim_Accumulator():
    uvsim = UVSim()

    assert uvsim.accumulator == 0
    assert isinstance(uvsim.accumulator, int)

#UT7
def test_UVSim_Instruction_Counter():
    uvsim = UVSim()

    assert uvsim.instruction_counter == 0
    assert isinstance(uvsim.instruction_counter, int)

#UT8
def test_UVSim_Instruction_Register():
    uvsim = UVSim()

    assert uvsim.instruction_register == 0
    assert isinstance(uvsim.instruction_register, int)

#UT9
def test_UVSim_Operation_Code():
    uvsim = UVSim()

    assert uvsim.operation_code == 0
    assert isinstance(uvsim.operation_code, int)

#UT10
def test_UVSim_Operand():
    uvsim = UVSim()
    
    assert uvsim.operand == 0
    assert isinstance(uvsim.operand, int)


# Test that checks the load function UT11
def test_load():
    sim = UVSim()
    sim.load('Test Files/Test1.txt')
    expected_memory = [+1007, +1008, +2007, +2008, +2109, +1109, +4300, +0000, +0000, +0000, -99999]

    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'

#UT12
def test_Load_Wrong_Input(capsys):
    sim = UVSim()
    sim.load('FakeFile.txt')

    captured = capsys.readouterr()
    expected_output = f"File 'FakeFile.txt' does not exist.\n"
    assert captured.out == expected_output

#UT13
def test_load_empty_file():
    sim = UVSim()
    sim.load('Test File/empty.txt')
    assert sim.memory == [0] * 100

#UT15
def test_execute_op_code_11(capsys):
    sim = UVSim()
    sim.memory[sim.operand] = 5678
    sim.write_output()
    captured = capsys.readouterr()
    assert captured.out.strip().endswith("Memory[0]: 5678")


#UT16
def test_execute_op_code_20():
    sim = UVSim()
    sim.memory[sim.operand] = 4321
    sim.load_word()
    assert sim.accumulator == 4321

#UT17
def test_execute_op_code_21():
    sim = UVSim()
    sim.accumulator = 8765
    sim.store_word()
    assert sim.memory[sim.operand] == 8765

#UT18
def test_execute_op_code_30():
    sim = UVSim()
    sim.accumulator = 100
    sim.memory[sim.operand] = 200
    sim.add_word()
    assert sim.accumulator == 300

#UT19
def test_execute_op_code_31():
    sim = UVSim()
    sim.accumulator = 500
    sim.memory[sim.operand] = 200
    sim.subtract_word()
    assert sim.accumulator == 300

#UT20
def test_execute_op_code_32():
    sim = UVSim()
    sim.accumulator = 100
    sim.memory[sim.operand] = 5
    sim.divide_word()
    assert sim.accumulator == 20

#UT21
def test_execute_op_code_32_with_zero():
    sim = UVSim()
    sim.accumulator = 100
    sim.memory[sim.operand] = 0
    with pytest.raises(ZeroDivisionError):
        sim.divide_word()

#UT22
def test_execute_op_code_33():
    sim = UVSim()
    sim.accumulator = 50
    sim.memory[sim.operand] = 4
    sim.multiply_word()
    assert sim.accumulator == 200

#UT22
def test_execute_op_code_40():
    sim = UVSim()
    sim.operand = 10
    sim.branch_memory()
    assert sim.instruction_counter == sim.operand

#UT23
def test_execute_op_code_41():
    sim = UVSim()
    sim.accumulator = -5
    sim.operand = 10
    sim.branch_negative()
    assert sim.instruction_counter == sim.operand

def test_execute_op_code_41_no_branch():
    sim=UVSim()
    sim.accumulator = 5
    sim.operand = 10
    sim.branch_negative()
    assert sim.instruction_counter != sim.operand

#UT24
def test_execute_op_code_42():
    sim = UVSim()
    sim.accumulator = 0
    sim.operand = 10
    sim.branch_zero()
    assert sim.instruction_counter == sim.operand

def test_execute_op_code_42_no_branch():
    sim = UVSim()
    sim.accumulator = 5
    sim.operand = 10
    sim.branch_zero()
    assert sim.instruction_counter != sim.operand

#UT25
def test_execute_op_code_43():
    sim = UVSim()

    assert sim.halt_program() == "Program halted."

def test_invalid_operation(capsys):
    sim = UVSim()
    sim.invalid_operation()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid operation code."

# Test reading in a filename and loading the corresponding file UT26
def test_reading_in_filename_2():
    sim = UVSim()
    filename = "Test Files/Test2.txt"
    sim.load(filename)
    # Assert the desired behavior based on the loaded file
    expected_memory = [+1009,+1010,+2009,+3110,+4107,+1109,+4300,+1110,+4300,+0000,+0000,-99999]
    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'

#UT27
def test_load_data_type_text1():
    sim = UVSim()
    sim.load('Test Files/Test1.txt')
    expected_memory = [+1007, +1008, +2007, +2008, +2109, +1109, +4300, +0000, +0000, +0000, -99999]

    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'
    assert isinstance(sim.memory, list)

#UT28
def test_load_data_type_text2():
    sim = UVSim()
    filename = "Test Files/Test2.txt"
    sim.load(filename)
    # Assert the desired behavior based on the loaded file
    expected_memory = [+1009,+1010,+2009,+3110,+4107,+1109,+4300,+1110,+4300,+0000,+0000,-99999]
    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'
    assert isinstance(sim.memory, list)