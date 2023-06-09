class UVSim:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0

    def load(self, filename):
        '''Load Instructions Into Memory'''
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                sign = -1 if line[0] == '-' else 1 # Check if the number is negative
                self.memory[i] = int(line[1:]) * sign # Convert the number to an integer and store it in memory
        print(self.memory)

    def fetch(self):
        '''Fetch Instructions From Memory'''
        self.instruction_register = self.memory[self.instruction_counter]  # Fetch the instructions at instruction counter memory location
        # Discard last two digits so we just have the first two (opcode)
        self.operation_code = self.instruction_register // 100
        # Discard first two digits so we just have the last two (operand)
        self.operand = self.instruction_register % 100

    def execute(self, each_register):
        '''Execute Instructions'''
        match self.operation_code:
            case 10:  # READ
                '''Gets user input and stores it in memory specified by the operand value'''
                self.memroy[self.operand] = int(input(("Type the value to be READ in console: ")))
            case 11:  # WRITE
                # Write a word from a specific location in memory to screen
                print(self.memory[self.operand])
            case 20:  # LOAD
                '''Load a word from a specific location in memory into the accumulator'''
                self.accumulator = self.register[self.register_index]
            case 21:  # STORE
                '''Store a word from the accumulator into a specific location in memory'''
                self.register[self.register_index] = self.accumulator
            case 30:  # ADD
                '''Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.accumulator = self.accumulator + \
                    self.register[self.register_index]
            case 31:  # SUBTRACT
                '''Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)'''
                self.accumulator = self.accumulator - \
                    self.register[self.register_index]
            case 32:  # DIVIDE
                '''Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator)'''
                self.accumulator = self.accumulator / \
                    self.register[self.register_index]
            case 33:  # MULTIPLY
                '''Multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)'''
                self.accumulator = self.accumulator * \
                    self.register[self.register_index]
            case 40:  # BRANCH
                '''Branch to a specific location in memory'''
                each_register = self.register[self.register_index]
            case 41:  # BRANCHNEG
                '''Branch to a specific location in memory if the accumulator is negative'''
                if self.accumulator < 0:
                    each_register = self.register[self.register_index]
            case 42:  # BRANCHZERO
                '''Branch to a specific location in memory if the accumulator is zero'''
                if self.accumulator == 0:
                    each_register = self.register[self.register_index]
            case 43:  # HALT
                '''Pause the program'''
                self.halt = True



def main():
    testFile = "Test1.txt"
    uvsim = UVSim()
    uvsim.load(testFile)
    #uvsim.execute()

    #return 1


if __name__ == "__main__":
    main()


# address 00 ~ 99
# list

# put values in the list and parse the first character
# if it is not minus,
#   if it is plus sign,
#   parse the first two characters after the plus sign
#   else, parse the first two characters and check if they are instructions
#
# else they are data so they can be minus
#
# when each index of the list is executed, put it in a variable called accumulator
