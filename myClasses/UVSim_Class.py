import os

class UVSim:

    def __init__(self, output_function, output_accumulator, output_instruction_process, handle_user_input):
        self.memory = [0] * 250
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.output_instruction_process = output_function
        self.output_accumulator = output_accumulator
        self.user_input_from_gui = 0
        self.output_instruction_process = output_instruction_process
        self.handle_user_input = handle_user_input

    def load(self, filename):
        '''Load Instructions Into Memory'''
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return

        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if i >= 250:
                    raise ValueError("File contains more than 250 lines.")
                sign = -1 if line[0] == '-' else 1
                self.memory[i] = int(line[1:]) * sign

    def fetch(self):
        '''Fetch Instructions From Memory'''
        # Read the instruction from memory at the location specified by the instruction counter
        instruction_line = self.memory[self.instruction_counter]
        # Convert the instruction line (a string) to an integer
        instruction = int(instruction_line)
        # Operation code is the first three digits of the instruction
        self.operation_code = instruction // 100
        # Operand is the last two digits of the instruction
        self.operand = instruction % 100
        #print(f"Instruction Register: {self.instruction_register}")

    def set_user_input(self, user_input):
        self.user_input_from_gui = user_input


    def convert_file(self, filename):
        '''Converts 4-digit file to 6-digit file format'''
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return

        converted_lines = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # remove newline characters
                if line[0] in ['+', '-']:  # if the line starts with '+' or '-'
                    sign = line[0]
                    converted_lines.append(sign + line[1:].zfill(5))
                else:  # if the line doesn't start with '+' or '-'
                    converted_lines.append(line.zfill(6))

        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_converted{ext}"
        with open(new_filename, 'w') as file:
            file.write('\n'.join(converted_lines))
        return new_filename


    def execute(self, filename):
        '''Execute Instructions'''
        self.load(filename)
        while True:
            self.fetch()
            if self.operation_code == int('043', 10): # HALT
                '''Halt the program'''
                self.output_instruction_process("Program halted.")
                break  
            elif self.operation_code == int('010', 10):  # READ
                '''Gets user input and stores it in memory specified by the operand value'''
                self.output_instruction_process("Waiting for user input...")
                # Call the handle_user_input method provided by the GUI to wait for user input
                self.handle_user_input()
                if self.user_input_from_gui is not None:
                    self.memory[self.operand] = self.user_input_from_gui

            elif self.operation_code == int('011', 10): # WRITE
                '''Write a word from a specific location in memory to screen'''
                self.output_instruction_process("Triggered WRITE, operand 011")
                # print(f"Memory[{self.operand}]: {self.memory[self.operand]}")

            elif self.operation_code == int('020', 10):  # LOAD
                '''Load a word from a specific location in memory into the accumulator'''
                self.output_instruction_process("Triggered LOAD, operand 020")
                self.accumulator = self.memory[self.operand]
                self.output_accumulator(self.accumulator)

            elif self.operation_code == int('021', 10):  # STORE
                '''Store a word from the accumulator into a specific location in memory'''
                self.output_instruction_process("Triggered STORE, operand 021")
                self.memory[self.operand] = self.accumulator

            elif self.operation_code == int('030', 10):  # ADD
                '''Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered ADD, operand 030")
                self.accumulator += self.memory[self.operand]

            elif self.operation_code == int('031', 10): # SUBTRACT
                '''Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered SUBTRACT, operand 031")
                self.accumulator -= self.memory[self.operand]

            elif self.operation_code == int('032', 10):  # DIVIDE
                '''Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered DIVIDE, operand 032")
                if self.memory[self.operand] != 0:
                    self.accumulator /= self.memory[self.operand]
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
                
            elif self.operation_code == int('033', 10):# MULTIPLY
                '''Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered MULTIPLY, operand 033")
                self.accumulator *= self.memory[self.operand]

            elif self.operation_code == int('040', 10):# BRANCH
                '''Branch to a specific location in memory'''
                self.output_instruction_process("Triggered BRANCH, operand 040")
                self.instruction_counter = self.operand
                
            elif self.operation_code == int('041', 10): # BRANCHNEG
                '''Branch to a specific location in memory if the accumulator is negative'''
                self.output_instruction_process("Triggered BRANCHNEG, operand 041")
                if self.accumulator < 0:
                    self.instruction_counter = self.operand
                    continue
                
            elif self.operation_code == int('042', 10): # BRANCHZERO
                '''Branch to a specific location in memory if the accumulator is zero'''
                self.output_instruction_process("Triggered BRANCHZERO, operand 042")
                if self.accumulator == 0:
                    self.instruction_counter = self.operand
                    continue
            else:
                self.output_instruction_process("Invalid operation code.")
        
            self.instruction_counter += 1

'''    
def output_function(message):
    print(message)

def output_accumulator(value):
    print("Accumulator:", value)

def output_instruction_process(message):
    print("Instruction Process:", message)

def handle_user_input():
    return 10

# Instantiate UVSim
sim = UVSim(output_function, output_accumulator, output_instruction_process, handle_user_input)

# Convert the file to 6-digit format
new_filename = sim.convert_file('Test1.txt')

# Load and execute the converted file
sim.execute('Test1_converted.txt')
'''