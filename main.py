class UVSim:
    def __init__(self):
        self.memory = [0] * 100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0

    def load(self, filename):
        pass

    def execute(self):
        pass

#jfbvhjbdfivbiwenc

def main():
    #first commit
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