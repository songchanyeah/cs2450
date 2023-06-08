class UVSim:
    def __init__(self):
        self.operation_codes = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        self.operation_code = 0
        self.register = [0] * 100
        self.register_index = 0
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operand = 0
        self.halt = False

    def load(self, filename):
<<<<<<< Updated upstream
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
=======
        '''Load Instructions Into register'''
        with open(filename, 'r') as file:
            for i, each_register in enumerate(file):
                self.register[i] = int(each_register)

    def fetch(self):
        '''Fetch Instructions From register'''
        self.instruction_register = self.register[self.instruction_counter] # Fetch the instructions at instruction counter register location
        self.operation_code = self.instruction_register // 100 # Discard last two digits so we just have the first two (opcode)
        self.operand = self.instruction_register % 100 # Discard first two digits so we just have the last two (operand)
        

    def execute(self, each_register):
        '''Execute Instructions'''
        if self.operation_code == 10: # READ
            # type something in the console, input()
            # then update that info in the register address following the operation_code
            # for example 1007 -> read from console then put that info in register[07]
            readVal = 0
            readVal = input("Type the value to be READ in console: ")
            self.register[self.register_index] = int(readVal) # parse
        elif self.operation_code == 11: # WRITE
            print(self.register[self.register_index])
        elif self.operation_code == 20: # LOAD
            self.accumulator = self.register[self.register_index]
        elif self.operation_code == 21: # STORE
            self.register[self.register_index] = self.accumulator
        elif self.operation_code == 30: # ADD
            self.accumulator = self.accumulator + self.register[self.register_index]
        elif self.operation_code == 31: # SUBTRACT
            self.accumulator = self.accumulator - self.register[self.register_index]
        elif self.operation_code == 32: # DIVIDE
            self.accumulator = self.accumulator / self.register[self.register_index]
        elif self.operation_code == 33: # MULTIPLY
            self.accumulator = self.accumulator * self.register[self.register_index]
        elif self.operation_code == 40: # BRANCH
            each_register = self.register[self.register_index]
        elif self.operation_code == 41: # BRANCHNEG
            if self.accumulator < 0:
                each_register = self.register[self.register_index]
        elif self.operation_code == 42: # BRANCHZERO
            if self.accumulator == 0:
                each_register = self.register[self.register_index]
        elif self.operation_code == 43: # HALT
            self.halt = True
    
    
    def parse(self, testFile):
        self.halt = False
        self.register = [each_register for each_register in testFile] # 100 registers
        for each_register in self.register: # each register of registers which has the word (4 digit integer)
            if self.halt == True:
                break
            else:
                if each_register[0] != "-": # it could be plus or number, either way it is a plus
                    if each_register[0] == "+": # the 0th index is not a number, the 1st index is a number
                        if int(each_register[1:3]) in self.operation_codes:
                            self.operation_code = int(each_register[1:3])
                            self.register_index = int(each_register[3:5]) # self.register[register_index]
                            self.execute()
                    else: # the 0th index is a number
                        if each_register[0:2] in self.operation_codes:
                            self.operation_code = each_register[0:2]
                            self.register_index = each_register[2:4] # self.register[register_index]
                            self.execute(each_register) # how to pass by reference in python
                else: # when the first character is a minus
                    # just a data, what do you do
                    pass
            



def main():
    testFile = open("test1.txt", "r")
    uvsim = UVSim()
    uvsim.parse(testFile)
    uvsim.execute()
            

    return 1


>>>>>>> Stashed changes
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

