import os

class UVSim:

    def __init__(self, output_function, output_accumulator):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.output_instruction_process = output_function
        self.output_accumulator = output_accumulator
        # self.output_user_input = output_user_input
        # self.user_input_from_gui = user_input
        self.user_input_from_gui = 0

    def load(self, filename):
        '''Load Instructions Into Memory'''
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return
        
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                # Check if the number is negative
                sign = -1 if line[0] == '-' else 1
                # Convert the number to an integer and store it in memory
                self.memory[i] = int(line[1:]) * sign
        # print(self.memory)
        

    def fetch(self):
        '''Fetch Instructions From Memory'''
        self.instruction_register = self.memory[self.instruction_counter]  # Fetch the instructions at instruction counter memory location
        # Discard last two digits so we just have the first two (opcode)
        self.operation_code = self.instruction_register // 100
        # Discard first two digits so we just have the last two (operand)
        self.operand = self.instruction_register % 100
    
    def halt_program(self):
        print("Program halted.")
        return "Program halted."

    def read_input(self):
        print("Triggered READ")
        try:
            user_input = int(input("Enter an integer between -9999 and 9999: "))
            if not -9999 <= user_input <= 9999:
                raise ValueError("Input must be between -9999 and 9999")
            self.memory[self.operand] = user_input
        except ValueError as e:
            print(e)

    def write_output(self):
        print("Triggered WRITE")
        print(f"Memory[{self.operand}]: {self.memory[self.operand]}")

    def load_word(self):
        print("Triggered LOAD")
        self.accumulator = self.memory[self.operand]

    def store_word(self):
        print("Triggered STORE")
        self.memory[self.operand] = self.accumulator

    def add_word(self):
        print("Triggered ADD")
        self.accumulator += self.memory[self.operand]

    def subtract_word(self):
        print("Triggered SUBTRACT")
        self.accumulator -= self.memory[self.operand]

    def divide_word(self):
        print("Triggered DIVIDE")
        if self.memory[self.operand] != 0:
            self.accumulator /= self.memory[self.operand]
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def multiply_word(self):
        print("Triggered MULTIPLY")
        self.accumulator *= self.memory[self.operand]

    def branch_memory(self):
        print("Triggered BRANCH")
        self.instruction_counter = self.operand

    def branch_negative(self):
        print("Triggered BRANCHNEG")
        if self.accumulator < 0:
            self.instruction_counter = self.operand

    def branch_zero(self):
        print("Triggered BRANCHZERO")
        if self.accumulator == 0:
            self.instruction_counter = self.operand

    def invalid_operation(self):
        print("Invalid operation code.")

    def execute(self, filename):
        '''Execute Instructions'''
        
        self.load(filename)
        
        while True:
            self.fetch()
<<<<<<< HEAD
            if self.operation_code == 43: # HALT
                '''Halt the program'''
                self.output_instruction_process("Program halted.")
                break  
            
            elif self.operation_code == 10:  # READ
                '''Gets user input and stores it in memory specified by the operand value'''
                self.output_instruction_process("Triggered READ, operand 10")
                try:
                    # user_input = int(input("Enter an integer between -9999 and 9999: "))
                    user_input = self.user_input_from_gui
                    if not -9999 <= user_input <= 9999:
                        raise ValueError("Input must be between -9999 and 9999")
                    self.memory[self.operand] = user_input
                except ValueError as e:
                    print(e)
                        
            elif self.operation_code == 11: # WRITE
                '''Write a word from a specific location in memory to screen'''
                self.output_instruction_process("Triggered WRITE, operand 11")
                print(f"Memory[{self.operand}]: {self.memory[self.operand]}")

            elif self.operation_code == 20:  # LOAD
                '''Load a word from a specific location in memory into the accumulator'''
                self.output_instruction_process("Triggered LOAD, operand 20")
                self.accumulator = self.memory[self.operand]
                self.output_accumulator(self.accumulator)

            elif self.operation_code == 21:  # STORE
                '''Store a word from the accumulator into a specific location in memory'''
                self.output_instruction_process("Triggered STORE, operand 21")
                self.memory[self.operand] = self.accumulator

            elif self.operation_code == 30:  # ADD
                '''Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered ADD, operand 30")
                self.accumulator += self.memory[self.operand]

            elif self.operation_code == 31: # SUBTRACT
                '''Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered SUBTRACT, operand 31")
                self.accumulator -= self.memory[self.operand]

            elif self.operation_code == 32:  # DIVIDE
                '''Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered DIVIDE, operand 32")
                if self.memory[self.operand] != 0:
                    self.accumulator /= self.memory[self.operand]
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
                
            elif self.operation_code == 33:# MULTIPLY
                '''Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.output_instruction_process("Triggered MULTIPLY, operand 33")
                self.accumulator *= self.memory[self.operand]

            elif self.operation_code == 40:# BRANCH
                '''Branch to a specific location in memory'''
                self.output_instruction_process("Triggered BRANCH, operand 40")
                self.instruction_counter = self.operand
                
            elif self.operation_code == 41: # BRANCHNEG
                '''Branch to a specific location in memory if the accumulator is negative'''
                self.output_instruction_process("Triggered BRANCHNEG, operand 41")
                if self.accumulator < 0:
                    self.instruction_counter = self.operand
                    continue
                
            elif self.operation_code == 42: # BRANCHZERO
                '''Branch to a specific location in memory if the accumulator is zero'''
                self.output_instruction_process("Triggered BRANCHZERO, operand 42")
                if self.accumulator == 0:
                    self.instruction_counter = self.operand
                    continue
            else:
                self.output_instruction_process("Invalid operation code.")
            
=======
            if self.operation_code == 43:  # HALT
                self.halt_program()
                break

            elif self.operation_code == 10:  # READ
                self.read_input()

            elif self.operation_code == 11:  # WRITE
                self.write_output()

            elif self.operation_code == 20:  # LOAD
                self.load_word()

            elif self.operation_code == 21:  # STORE
                self.store_word()

            elif self.operation_code == 30:  # ADD
                self.add_word()

            elif self.operation_code == 31:  # SUBTRACT
                self.subtract_word()

            elif self.operation_code == 32:  # DIVIDE
                self.divide_word()

            elif self.operation_code == 33:  # MULTIPLY
                self.multiply_word()

            elif self.operation_code == 40:  # BRANCH
                self.branch_memory()

            elif self.operation_code == 41:  # BRANCHNEG
                self.branch_negative()

            elif self.operation_code == 42:  # BRANCHZERO
                self.branch_zero()

            else:
                self.invalid_operation()
                
>>>>>>> 20d0843b0056497b1208d0cf65462e6b5f0e20eb
            self.instruction_counter += 1

    