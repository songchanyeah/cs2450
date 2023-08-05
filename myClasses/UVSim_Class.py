import os

class UVSim:
    def __init__(self, output_function, output_accumulator, output_instruction_process, handle_user_input):
        self.instances = {}  # Instances of UVSim for each file
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

        memory = [0] * 250
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if i >= 250:
                    raise ValueError("File contains more than 250 lines.")
                sign = -1 if line[0] == '-' else 1
                memory[i] = int(line[1:]) * sign

        self.instances[filename] = {
            'memory': memory,
            'accumulator': 0,
            'instruction_counter': 0,
            'instruction_register': 0,
            'operation_code': 0,
            'operand': 0
        }

    def fetch(self, filename):
        '''Fetch Instructions From Memory'''
        data = self.instances[filename]
        instruction_line = data['memory'][data['instruction_counter']]
        instruction = int(instruction_line)
        data['operation_code'] = instruction // 100
        data['operand'] = instruction % 100

    def set_user_input(self, filename, user_input):
        self.instances[filename]['user_input_from_gui'] = user_input

    def close(self, filename):
        '''Remove a file and its program data from the dictionary'''
        if filename in self.instances:
            del self.instances[filename]

    def convert_file(self, filename):
        '''Converts 4-digit file to 6-digit file format'''
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist.")
            return

        converted_lines = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
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
        if filename not in self.instances:
            self.load(filename)
        data = self.instances[filename]
        while True:
            self.fetch(filename)
            if data['operation_code'] == int('043', 10): # HALT
                self.output_instruction_process("Program halted.")
                break  
            elif data['operation_code'] == int('010', 10):  # READ
                self.output_instruction_process("Waiting for user input...")
                self.handle_user_input(filename)
                if 'user_input_from_gui' in data and data['user_input_from_gui'] is not None:
                    data['memory'][data['operand']] = data['user_input_from_gui']

            elif data['operation_code'] == int('011', 10): # WRITE
                self.output_instruction_process(f"Triggered WRITE, operand {data['operand']}")
                self.output_accumulator(data['memory'][data['operand']])

            elif data['operation_code'] == int('020', 10):  # LOAD
                self.output_instruction_process(f"Triggered LOAD, operand {data['operand']}")
                data['accumulator'] = data['memory'][data['operand']]
                self.output_accumulator(data['accumulator'])

            elif data['operation_code'] == int('021', 10):  # STORE
                self.output_instruction_process(f"Triggered STORE, operand {data['operand']}")
                data['memory'][data['operand']] = data['accumulator']

            elif data['operation_code'] == int('030', 10):  # ADD
                self.output_instruction_process(f"Triggered ADD, operand {data['operand']}")
                data['accumulator'] += data['memory'][data['operand']]
                self.output_accumulator(data['accumulator'])

            elif data['operation_code'] == int('031', 10): # SUBTRACT
                self.output_instruction_process(f"Triggered SUBTRACT, operand {data['operand']}")
                data['accumulator'] -= data['memory'][data['operand']]
                self.output_accumulator(data['accumulator'])

            elif data['operation_code'] == int('032', 10):  # DIVIDE
                self.output_instruction_process(f"Triggered DIVIDE, operand {data['operand']}")
                if data['memory'][data['operand']] != 0:
                    data['accumulator'] /= data['memory'][data['operand']]
                    self.output_accumulator(data['accumulator'])
                else:
                    raise ZeroDivisionError("Cannot divide by zero")

            elif data['operation_code'] == int('033', 10): # MULTIPLY
                self.output_instruction_process(f"Triggered MULTIPLY, operand {data['operand']}")
                data['accumulator'] *= data['memory'][data['operand']]
                self.output_accumulator(data['accumulator'])

            elif data['operation_code'] == int('040', 10): # BRANCH
                self.output_instruction_process(f"Triggered BRANCH, operand {data['operand']}")
                data['instruction_counter'] = data['operand']
                continue

            elif data['operation_code'] == int('041', 10): # BRANCHNEG
                self.output_instruction_process(f"Triggered BRANCHNEG, operand {data['operand']}")
                if data['accumulator'] < 0:
                    data['instruction_counter'] = data['operand']
                    continue

            elif data['operation_code'] == int('042', 10): # BRANCHZERO
                self.output_instruction_process(f"Triggered BRANCHZERO, operand {data['operand']}")
                if data['accumulator'] == 0:
                    data['instruction_counter'] = data['operand']
                    continue

            else:
                self.output_instruction_process("Invalid operation code.")

            data['instruction_counter'] += 1
