import pytest
from myClasses.UVSim_Class import UVSim
import os
import unittest

# Test that checks the fetch function UT1
def test_fetch():
    sim = UVSim()
    sim.memory[0] = 01002  # opcode 010 and operand 02
    sim.memory[1] = 02130  # opcode 021 and operand 30
    sim.memory[2] = 04300  # opcode 043 and operand 00
    sim.memory[3] = 00000  # opcode 000 and operand 00
    sim.memory[4] = 0000  # opcode 000 and operand 00
    sim.memory[5] = 0000  # opcode 000 and operand 00

    sim.fetch()
    assert sim.operation_code == 10
    assert sim.operand == 2

#UT2
def test_fetch_instruction():
    uvsim = UVSim()

    uvsim.memory = [01007, 02010, 03018, 02119, 04017]
    uvsim.instruction_counter = 2
    uvsim.fetch()

    assert uvsim.instruction_register == 03018
    assert uvsim.operation_code == 30
    assert uvsim.operand == 18

# Test the UVSim class constructor UT3
def test_UVSim_Constructor():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 250
    assert uvsim.accumulator == 0
    assert uvsim.instruction_counter == 0
    assert uvsim.instruction_register == 0
    assert uvsim.operation_code == 0
    assert uvsim.operand == 0


#UT4
def test_UVSim_Memory():
    uvsim = UVSim()

    assert uvsim.memory == [0] * 250
    assert isinstance(uvsim.memory, list)

#UT5
def test_UVSim_Memory_Range_Error():
    uvsim = UVSim()

    with pytest.raises(IndexError):
        value = uvsim.memory[251]

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
    expected_memory = [+01007, +01008, +02007, +02008, +02109, +01109, +04300, +00000, +00000, +00000, -099999]

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
    assert sim.memory == [0] * 250

#UT15
def test_execute_op_code_11(capsys):
    sim = UVSim()
    sim.memory[sim.operand] = 05678
    sim.write_output()
    captured = capsys.readouterr()
    assert captured.out.strip().endswith("Memory[0]: 5678")


#UT16
def test_execute_op_code_20():
    sim = UVSim()
    sim.memory[sim.operand] = 04321
    sim.load_word()
    assert sim.accumulator == 04321

#UT17
def test_execute_op_code_21():
    sim = UVSim()
    sim.accumulator = 08765
    sim.store_word()
    assert sim.memory[sim.operand] == 08765

#UT18
def test_execute_op_code_30():
    sim = UVSim()
    sim.accumulator = 250
    sim.memory[sim.operand] = 0200
    sim.add_word()
    assert sim.accumulator == 0300

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
    sim.accumulator = 250
    sim.memory[sim.operand] = 5
    sim.divide_word()
    assert sim.accumulator == 20

#UT21
def test_execute_op_code_32_with_zero():
    sim = UVSim()
    sim.accumulator = 250
    sim.memory[sim.operand] = 0
    with pytest.raises(ZeroDivisionError):
        sim.divide_word()

#UT22
def test_execute_op_code_33():
    sim = UVSim()
    sim.accumulator = 250
    sim.memory[sim.operand] = 4
    sim.multiply_word()
    assert sim.accumulator == 200

#UT22
def test_execute_op_code_40():
    sim = UVSim()
    sim.operand = 010
    sim.branch_memory()
    assert sim.instruction_counter == sim.operand

#UT23
def test_execute_op_code_41():
    sim = UVSim()
    sim.accumulator = -5
    sim.operand = 010
    sim.branch_negative()
    assert sim.instruction_counter == sim.operand

def test_execute_op_code_41_no_branch():
    sim=UVSim()
    sim.accumulator = 5
    sim.operand = 010
    sim.branch_negative()
    assert sim.instruction_counter != sim.operand

#UT24
def test_execute_op_code_42():
    sim = UVSim()
    sim.accumulator = 0
    sim.operand = 010
    sim.branch_zero()
    assert sim.instruction_counter == sim.operand

def test_execute_op_code_42_no_branch():
    sim = UVSim()
    sim.accumulator = 5
    sim.operand = 010
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
    expected_memory = [+01009,+01010,+02009,+03110,+04107,+01109,+04300,+01110,+04300,+00000,+00000,-099999]
    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'

#UT27
def test_load_data_type_text1():
    sim = UVSim()
    sim.load('Test Files/Test1.txt')
    expected_memory = [+01007, +01008, +02007, +02008, +02109, +01109, +04300, +00000, +00000, +00000, -099999]

    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'
    assert isinstance(sim.memory, list)

#UT28
def test_load_data_type_text2():
    sim = UVSim()
    filename = "Test Files/Test2.txt"
    sim.load(filename)
    # Assert the desired behavior based on the loaded file
    expected_memory = [+01009,+01010,+02009,+03110,+04107,+01109,+04300,+01110,+04300,+00000,+00000,-099999]
    assert sim.memory[:len(expected_memory)] == expected_memory, f'Expected {expected_memory}, but got {sim.memory[:len(expected_memory)]}'
    assert isinstance(sim.memory, list)


class TestUVSim(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim(None, None, None, None)
        self.test_file = "test_file.txt"
        self.output_file = "test_file_converted.txt"

        # Create a test input file
        with open(self.test_file, 'w') as file:
            file.write('+123\n-456\n789')

    def tearDown(self):
        # Clean up test files
        os.remove(self.test_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_convert_file(self):
        converted_filename = self.sim.convert_file(self.test_file)

        # Validate the filename
        self.assertEqual(converted_filename, self.output_file)

        # Validate the file content
        with open(converted_filename, 'r') as file:
            lines = file.read().split('\n')
            self.assertEqual(lines[0], '+00123')
            self.assertEqual(lines[1], '-00456')
            self.assertEqual(lines[2], '000789')

if __name__ == '__main__':
    unittest.main()

