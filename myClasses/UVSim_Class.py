import os
from pathlib import Path

class UVSim:

    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.register = 0 #This will need to be fixed, there was no class object being referenced here.
        self.register_index = 0 #This will need to be fixed, there was no class object being referenced here.
        self.operation_codes = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]

    def load(self, filename):
        '''Load Instructions Into Memory'''
        current_dir = os.getcwd()
        current_dir = current_dir + "\Test Files\\"
        relative_path = current_dir + filename

        # print(relative_path)

        if not os.path.exists(relative_path):
            print(f"File '{relative_path}' does not exist.")
            return
        
        with open(relative_path, 'r') as file:
            for i, line in enumerate(file):
                # Check if the number is negative
                sign = -1 if line[0] == '-' else 1
                # Convert the number to an integer and store it in memory
                self.memory[i] = int(line[1:]) * sign
        ###################        
        print("self.memory: ", self.memory)
        ###################

    def fetch(self):
        '''Fetch Instructions From Memory'''
        self.instruction_register = self.memory[self.instruction_counter]  # Fetch the instructions at instruction counter memory location
        # Discard last two digits so we just have the first two (opcode)
        self.operation_code = self.instruction_register // 100
        # Discard first two digits so we just have the last two (operand)
        self.operand = self.instruction_register % 100
        self.instruction_counter += 1

    def execute(self):
        '''Execute Instructions'''
        filename = input("Please enter the name of your text file to be read in: ")
        # use filename "Test Files/Test1.txt" to run
        self.load(filename)

        self.fetch()
        ###################
        print("operation code: ", self.operation_code)
        print("operand: ", self.operand)
        ###################
        while self.operation_code != 43:
            match self.operation_code:
                case 10:  # READ
                    '''Gets user input and stores it in memory specified by the operand value'''
                    user_input = int(input("Enter an integer between -9999 and 9999: "))
                    try:
                        if not -9999 <= user_input <= 9999:
                            raise ValueError("Input must be between -9999 and 9999")
                        else:
                            self.memory[self.operand] = user_input
                    except ValueError as e:
                        print(e)
                    self.fetch()

                case 11:  # WRITE
                    '''Write a word from a specific location in memory to screen'''
                    print(f"Memory[{self.operand}]: {self.memory[self.operand]}")
                    self.fetch()

                case 20:  # LOAD
                    '''Load a word from a specific location in memory into the accumulator'''
                    self.accumulator = self.memory[self.operand]
                    self.fetch()

                case 21:  # STORE
                    '''Store a word from the accumulator into a specific location in memory'''
                    self.memory[self.operand] = self.accumulator
                    self.fetch()

                case 30:  # ADD
                    '''Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                    self.accumulator += self.memory[self.operand]
                    self.fetch()

                case 31:  # SUBTRACT
                    '''Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)'''
                    self.accumulator -= self.memory[self.operand]
                    self.fetch()

                case 32:  # DIVIDE
                    '''Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)'''
                    if self.memory[self.operand] != 0:
                        self.accumulator /= self.memory[self.operand]
                    else:
                        raise ZeroDivisionError("Cannot divide by zero")
                    self.fetch()

                case 33:  # MULTIPLY
                    '''Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                    self.accumulator *= self.memory[self.operand]
                    self.fetch()

                case 40:  # BRANCH
                    '''Branch to a specific location in memory'''
                    self.instruction_counter = self.operand
                    self.fetch()

                case 41:  # BRANCHNEG
                    '''Branch to a specific location in memory if the accumulator is negative'''
                    if self.accumulator < 0:
                        self.instruction_counter = self.operand
                    self.fetch()

                case 42:  # BRANCHZERO
                    '''Branch to a specific location in memory if the accumulator is zero'''
                    if self.accumulator == 0:
                        self.instruction_counter = self.operand
                    self.fetch()

                case 43:  # HALT
                    '''Halt the program'''
                    print("Program halted.")
                    self.operation_code = 43
                    self.fetch()

                    return self.operation_code 
        ###################
        print("self.memory: ", self.memory)
        ###################
            
            