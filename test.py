
import unittest
import os
from myClasses.UVSim_Class import UVSim

class TestUVSim(unittest.TestCase):
    def setUp(self):
        # Dummy functions to pass to UVSim
        def output_function(x): pass
        def output_accumulator(x): pass
        def output_instruction_process(x): pass
        def handle_user_input(x): pass
        # Instantiate the UVSim class
        self.uv = UVSim(output_function, output_accumulator, output_instruction_process, handle_user_input)
        # Test file 1 & 2
        self.test1 = "Test Files/Test1.txt"
        self.test2 = "Test Files/Test2.txt"
        # 4 digit converted test files
        self.test1_4digit = "test1_4digit.txt"
        self.test2_4digit = "test2_4digit.txt"
        with open(self.test1_4digit, 'w') as f:
            f.write("+01007\n+01008\n+02007\n+02008\n+02109\n+01109\n+04300\n+00000\n+00000\n+00000\n-99999")
        with open(self.test2_4digit, 'w') as f:
            f.write("+01009\n+01010\n+02009\n+03110\n+04107\n+01109\n+04300\n+01110\n+04300\n+00000\n+00000\n-99999")

    def test_memory_size(self):
        # Load a file to ensure there's an instance to check
        self.uv.load(self.test1)
        # Ensure the file instance exists
        self.assertIn(self.test1, self.uv.instances)
        # Assert the memory size for the file instance
        self.assertEqual(len(self.uv.instances[self.test1]['memory']), 250)

    def test_load(self):
        # Test loading the first file
        self.uv.load(self.test1)
        self.assertIn(self.test1, self.uv.instances)
        expected_memory1 = [+1007, +1008, +2007, +2008, +2109, +1109, +4300, +0000, +0000, +0000, -99999]
        for index, value in enumerate(expected_memory1):
            self.assertEqual(self.uv.instances[self.test1]['memory'][index], value)
        # Test loading the second file
        self.uv.load(self.test2)
        self.assertIn(self.test2, self.uv.instances)
        expected_memory2 = [+1009, +1010, +2009, +3110, +4107, +1109, +4300, +1110, +4300, +0000, +0000, -99999]
        for index, value in enumerate(expected_memory2):
            self.assertEqual(self.uv.instances[self.test2]['memory'][index], value)

    def test_fetch(self):
        # Load test1 and test2
        self.uv.load(self.test1)
        self.uv.load(self.test2)
        # Fetch the first instruction from test1
        self.uv.fetch(self.test1)
        first_instruction_test1 = +1007
        # Calculate operation_code and operand
        expected_op_code_test1 = first_instruction_test1 // 100
        expected_operand_test1 = first_instruction_test1 % 100
        # Print the expected and actual values
        print(f"For {self.test1_4digit}:")
        print(f"Expected operation_code: {expected_op_code_test1}, Actual: {self.uv.instances[self.test1]['operation_code']}")
        print(f"Expected operand: {expected_operand_test1}, Actual: {self.uv.instances[self.test1]['operand']}")
        # Assert the operation_code and operand
        self.assertEqual(self.uv.instances[self.test1]['operation_code'], expected_op_code_test1)
        self.assertEqual(self.uv.instances[self.test1]['operand'], expected_operand_test1)
        # Fetch the first instruction from test2
        self.uv.fetch(self.test2)
        first_instruction_test2 = +1009
        # Calculate operation_code and operand
        expected_op_code_test2 = first_instruction_test2 // 100
        expected_operand_test2 = first_instruction_test2 % 100
        # Print the expected and actual values
        print(f"For {self.test2_4digit}:")
        print(f"Expected operation_code: {expected_op_code_test2}, Actual: {self.uv.instances[self.test2]['operation_code']}")
        print(f"Expected operand: {expected_operand_test2}, Actual: {self.uv.instances[self.test2]['operand']}")
        # Assert the operation_code and operand
        self.assertEqual(self.uv.instances[self.test2]['operation_code'], expected_op_code_test2)
        self.assertEqual(self.uv.instances[self.test2]['operand'], expected_operand_test2)

    def test_set_user_input(self):
        self.uv.load(self.test1)
        # Ensure the file instance exists
        self.assertIn(self.test1, self.uv.instances)
        test_input = 12345
        self.uv.set_user_input(self.test1, test_input)
        # Verify the user input was correctly set
        self.assertEqual(self.uv.instances[self.test1]['user_input_from_gui'], test_input)

    def test_close(self):
        self.uv.load(self.test2)
        # Ensure the file instance exists
        self.assertIn(self.test2, self.uv.instances)
        # Close the file instance
        self.uv.close(self.test2)
        # Verify the file instance was removed
        self.assertNotIn(self.test2, self.uv.instances)

    def test_convert_file(self):
        # Convert test1 and test2
        converted_test1 = self.uv.convert_file(self.test1)
        converted_test2 = self.uv.convert_file(self.test2)
        # Verify the filenames
        self.assertEqual(converted_test1, f"{os.path.splitext(self.test1)[0]}_converted{os.path.splitext(self.test1)[1]}")
        self.assertEqual(converted_test2, f"{os.path.splitext(self.test2)[0]}_converted{os.path.splitext(self.test2)[1]}")
        # Verify the content of the converted files
        with open(self.test1_4digit, 'r') as f1, open(converted_test1, 'r') as f2:
            content1_4digit = f1.read().strip()
            content_converted_test1 = f2.read().strip()
            self.assertEqual(content1_4digit, content_converted_test1)
        with open(self.test2_4digit, 'r') as f1, open(converted_test2, 'r') as f2:
            content2_4digit = f1.read().strip()
            content_converted_test2 = f2.read().strip()
            self.assertEqual(content2_4digit, content_converted_test2)


    def test_execute(self):
        # Output functions to store messages in a list
        self.messages = []

        def output_function(x):
            self.messages.append(x)

        self.uv.output_instruction_process = output_function
        self.uv.output_accumulator = output_function

        # test1_4digit
        self.uv.execute(self.test1_4digit)
        self.assertIn("Waiting for user input...", self.messages)
        
        self.assertIn("Waiting for user input...", self.messages)
        self.assertIn("Triggered LOAD, operand 7", self.messages)
        self.assertIn("Triggered LOAD, operand 8", self.messages)
        self.assertIn("Triggered STORE, operand 9", self.messages)
        self.assertIn("Triggered WRITE, operand 9", self.messages)
        self.assertIn("Program halted.", self.messages)
        # Not finished more checks need to be added

        self.messages.clear()
        # test2_4digit
        self.uv.execute(self.test2_4digit)
        self.assertIn("Waiting for user input...", self.messages)
        self.assertIn("Waiting for user input...", self.messages)
        self.assertIn("Triggered LOAD, operand 9", self.messages)
        self.assertIn("Triggered SUBTRACT, operand 10", self.messages)
        self.assertIn("Triggered BRANCHNEG, operand 7", self.messages)
        self.assertIn("Triggered WRITE, operand 9", self.messages)
        self.assertIn("Program halted.", self.messages)

    

    def tearDown(self):
        # Remove dummy data files after tests
        if os.path.exists(self.test1_4digit):
            os.remove(self.test1_4digit)
        if os.path.exists(self.test2_4digit):
            os.remove(self.test2_4digit)
        '''converted_filename = f"{os.path.splitext(self.filename_4digit)[0]}_converted.txt"
        if os.path.exists(converted_filename):
            os.remove(converted_filename)'''

if __name__ == "__main__":
    unittest.main()
