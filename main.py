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
        '''Load Instructions Into Memory'''
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                self.memory[i] = int(line)

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
                # type something in the console, input()
                # then update that info in the register address following the operation_code
                # for example 1007 -> read from console then put that info in register[07]
                readVal = 0
                readVal = input("Type the value to be READ in console: ")
                self.register[self.register_index] = int(readVal)  # parse
            case 11:  # WRITE
                print(self.register[self.register_index])
            case 20:  # LOAD
                self.accumulator = self.register[self.register_index]
            case 21:  # STORE
                self.register[self.register_index] = self.accumulator
            case 30:  # ADD
                self.accumulator = self.accumulator + \
                    self.register[self.register_index]
            case 31:  # SUBTRACT
                self.accumulator = self.accumulator - \
                    self.register[self.register_index]
            case 32:  # DIVIDE
                self.accumulator = self.accumulator / \
                    self.register[self.register_index]
            case 33:  # MULTIPLY
                self.accumulator = self.accumulator * \
                    self.register[self.register_index]
            case 40:  # BRANCH
                
                each_register = self.register[self.register_index]
            case 41:  # BRANCHNEG
                if self.accumulator < 0:
                    each_register = self.register[self.register_index]
            case 42:  # BRANCHZERO
                if self.accumulator == 0:
                    each_register = self.register[self.register_index]
            case 43:  # HALT
                self.halt = True


    def parse(self, testFile):
        self.halt = False
        # 100 registers
        self.register = [each_register for each_register in testFile]
        # each register of registers which has the word (4 digit integer)
        for each_register in self.register:
            if self.halt == True:
                break
            else:
                # it could be plus or number, either way it is a plus
                if each_register[0] != "-":
                    # the 0th index is not a number, the 1st index is a number
                    if each_register[0] == "+":
                        if int(each_register[1:3]) in self.operation_codes:
                            self.operation_code = int(each_register[1:3])
                            # self.register[register_index]
                            self.register_index = int(each_register[3:5])
                            self.execute()
                    else:  # the 0th index is a number
                        if each_register[0:2] in self.operation_codes:
                            self.operation_code = each_register[0:2]
                            # self.register[register_index]
                            self.register_index = each_register[2:4]
                            # how to pass by reference in python
                            self.execute(each_register)
                else:  # when the first character is a minus
                    # just a data, what do you do
                    pass


def main():
    testFile = open("test1.txt", "r")
    uvsim = UVSim()
    uvsim.parse(testFile)
    uvsim.execute()

    return 1


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
