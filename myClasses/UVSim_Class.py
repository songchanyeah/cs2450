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

    def load(self, filename):
        '''Load Instructions Into Memory'''
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                # Check if the number is negative
                sign = -1 if line[0] == '-' else 1
                # Convert the number to an integer and store it in memory
                self.memory[i] = int(line[1:]) * sign
        print(self.memory)

    def fetch(self):
        '''Fetch Instructions From Memory'''
        self.instruction_register = self.memory[self.instruction_counter]  # Fetch the instructions at instruction counter memory location
        # Discard last two digits so we just have the first two (opcode)
        self.operation_code = self.instruction_register // 100
        # Discard first two digits so we just have the last two (operand)
        self.operand = self.instruction_register % 100

    def execute(self):
        '''Execute Instructions'''
        filename = input("Please enter the name of your text file to be read in: ")
        # use filename "Test Files/Test1.txt" to run
        self.load(filename)
        match self.operation_code:
            case 10:  # READ
                '''Gets user input and stores it in memory specified by the operand value'''
                self.memory[self.operand] = int(
                    input(("Type the value to be READ in console: ")))
            case 11:  # WRITE
                # Write a word from a specific location in memory to screen
                print(self.memory[self.operand])
            case 20:  # LOAD
                '''Load a word from a specific location in memory into the accumulator'''
                #self.accumulator = self.register[self.register_index]
            case 21:  # STORE
                '''Store a word from the accumulator into a specific location in memory'''
                #self.register[self.register_index] = self.accumulator
            case 30:  # ADD
                '''Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                #self.accumulator = self.accumulator + \
                   # self.register[self.register_index]
            case 31:  # SUBTRACT
                '''Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)'''
               # self.accumulator = self.accumulator - \
                    #self.register[self.register_index]
            case 32:  # DIVIDE
                '''Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)'''
                #self.accumulator = self.accumulator / \
                    #self.register[self.register_index]
            case 33:  # MULTIPLY
                '''Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                #self.accumulator = self.accumulator * \
                    #self.register[self.register_index]
            case 40:  # BRANCH
                '''Branch to a specific location in memory'''
                self.instruction_counter = self.operand
            case 41:  # BRANCHNEG
                '''Branch to a specific location in memory if the accumulator is negative'''
                if self.accumulator < 0:
                    self.instruction_counter = self.operand
            case 42:  # BRANCHZERO
                '''Branch to a specific location in memory if the accumulator is zero'''
                if self.accumulator == 0:
                    self.instruction_counter = self.operand
            case 43:  # HALT
                '''Halt the program'''
                print("Program halted.")
                return "Program halted."
            
            