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
                self.memory[i] = int(line)

    def fetch(self):
        '''Fetch Instructions From Memory'''
        self.instruction_register = self.memory[self.instruction_counter] # Fetch the instructions at instruction counter memory location
        self.operation_code = self.instruction_register // 100 # Discard last two digits so we just have the first two (opcode)
        self.operand = self.instruction_register % 100 # Discard first two digits so we just have the last two (operand)
        

    def execute(self):
        '''Execute Instructions'''
        if self.operation_code == 10: # READ
            pass
        elif self.operation_code == 11: # WRITE
            pass
        elif self.operation_code == 20: # LOAD
            pass
        elif self.operation_code == 21: # STORE
            pass
        elif self.operation_code == 30: # ADD
            pass
        elif self.operation_code == 31: # SUBTRACT
            pass
        elif self.operation_code == 32: # DIVIDE
            pass
        elif self.operation_code == 33: # MULTIPLY
            pass
        elif self.operation_code == 40: # BRANCH
            pass
        elif self.operation_code == 41: # BRANCHNEG
            pass
        elif self.operation_code == 42: # BRANCHZERO
            pass
        elif self.operation_code == 43: # HALT
            pass
        

def main():
    pass
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


#first pr