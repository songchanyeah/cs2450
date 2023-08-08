import tkinter as tk
from tkinter import *
from tkinter import ttk, colorchooser
import os
from myClasses.UVSim_Class import UVSim
import tkinter.filedialog as filedialog

class UVSimInstance:
    def __init__(self, filepath):
        self.filepath = filepath
        self.simulator = UVSim(
            output_function=self.output_function,
            output_accumulator=self.output_accumulator,
            output_instruction_process=self.output_instruction_process,
            handle_user_input=self.handle_user_input,
        )
        self.user_input = ""
        self.output_text = ""

    def output_function(self, message):
        self.output_text += message + "\n"

    def output_accumulator(self, value):
        self.output_text += "Accumulator: " + str(value) + "\n"

    def output_instruction_process(self, message):
        self.output_text += "Instruction Process: " + message + "\n"

    def handle_user_input(self, filename):
        if self.user_input.strip() == "":
            return 0 
        return int(self.user_input)

class UVSimGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.current_instance = None
        self.instances = {}  # attribute to hold all instances
        self.instance_var = tk.StringVar()  # attribute to hold the current instance
        self.instance_var.trace('w', self.switch_instance)  # Listen for changes in instance_var
        self.uvsim = UVSim(
            output_function=self.output_instruction_process,
            output_accumulator=self.output_accumulator,
            output_instruction_process=self.output_instruction_process,
            handle_user_input=self.handle_user_input,
        )
        self.user_input_ready = tk.BooleanVar(value=False)
        self.primary_color = (76, 114, 29)
        self.off_color = (255, 255, 255)
        self.load_color_scheme()
        self.create_widgets()
        self.apply_color_scheme()

    def load_color_scheme(self):
        try:
            with open("config.txt") as file:
                lines = file.readlines()
                self.primary_color = tuple(int(value) for value in lines[0].strip().split(","))
                self.off_color = tuple(int(value) for value in lines[1].strip().split(","))
        except FileNotFoundError:
            # Default color scheme
            self.primary_color = (76, 114, 29)
            self.off_color = (255, 255, 255)

    def save_color_scheme(self):
        config = f"{','.join(str(value) for value in self.primary_color)}\\n{','.join(str(value) for value in self.off_color)}"
        with open("config.txt", "w") as file:
            file.write(config)

    def rgb_to_hex(self, r, g, b):
        return '#%02x%02x%02x' % (r, g, b)
    
    def apply_color_scheme(self):
        primary_color_hex = self.rgb_to_hex(*self.primary_color)
        self.master.configure(background=primary_color_hex)

    ### Change Background Color
    def change_primary_color(self):
        color = colorchooser.askcolor()[0]
        if color:
            self.primary_color = tuple(int(value) for value in color)
            self.apply_color_scheme()

    def create_widgets(self):
        # Configure the primary color for the UI
        style = ttk.Style()
        primary_color_hex = self.rgb_to_hex(*self.primary_color)
        style.configure("TButton", background=primary_color_hex)
        self.change_color_button = tk.Button(self.master, text="Change Primary Color", command=self.change_primary_color)
        self.change_color_button.grid(row=4, column=3, sticky=tk.W)

        ##### Save File Button #####
        self.save_button = tk.Button(self.master, text="Save", command=self.save_file)
        self.save_button.grid(row=0, column=0, sticky=W)

        ##### Load File Button #####
        self.load_button = tk.Button(self.master, text="Load", command=self.load_file)
        self.load_button.grid(row=0, column=0, sticky=E)

        ##### Instance Switcher Dropdown Menu #####
        self.instance_menu = tk.OptionMenu(self.master, self.instance_var, '')  # Create a dropdown menu
        self.instance_menu.grid(row=0, column=1, sticky=W)  # Position the dropdown menu

        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row=0, column=2, sticky=W)

        self.execute_button = tk.Button(self.master, text="Execute", command=self.execute_program)
        self.execute_button.grid(row=0, column=2, sticky=E)
        
        self.output_label = tk.Label(self.master, text="")
        self.output_label.grid(row=0, column=3, sticky=W)

        ### < For UVSim Class > ###
        ##### User Input for Read Operation #####
        self.user_input_for_read_label = tk.Label(self.master, text="Enter an integer between -9999 and 9999:")
        self.user_input_for_read_label.grid(row=1, column=0, sticky=W)

        self.user_input_entry = tk.Entry(self.master)
        self.user_input_entry.grid(row=1, column=2, sticky=W)

        self.user_input_button = tk.Button(self.master, text="Enter", command=self.get_user_input)
        self.user_input_button.grid(row=1, column=2, sticky=E)

        ### < For UVSim Class > ###
        ##### Accumulator #####
        self.accumulator_label = tk.Label(self.master, text="Accumulator: ")
        self.accumulator_label.grid(row=2, column=0, sticky=W)

        self.accumulator_entry = tk.Entry(self.master)
        self.accumulator_entry.grid(row=2, column=2, sticky=W)

        ##### Memory #####
        self.listbox_for_memory = tk.Listbox(self.master)
        self.listbox_for_memory.grid(row=3, column=0, sticky=tk.NSEW)

        self.scrollbar_for_memory = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.scrollbar_for_memory.grid(row=3, column=1, sticky=tk.NS)

        self.listbox_for_memory.config(yscrollcommand=self.scrollbar_for_memory.set)
        self.scrollbar_for_memory.config(command=self.listbox_for_memory.yview)

        ### < For UVSim Class > ###
        ##### Instructions Run #####
        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.grid(row=3, column=2)

    def execute_program(self):
        if self.current_instance and os.path.exists(self.current_instance.filepath):
            self.output_label.config(text=self.current_instance.filepath + " executed successfully.")
            self.current_instance.simulator.execute(self.current_instance.filepath)
            self.display_memory()
            self.output_text.delete(1.0, tk.END)  # Clear the output text
            self.output_text.insert(tk.END, self.current_instance.output_text)  # Display the output text
        else:
            self.output_label.config(text="No file is currently loaded.")

    
    def switch_instance(self, *args):
        print("Switched instance.")  # To verify that switch_instance is being called
        filepath = self.instance_var.get()
        instance = self.instances[filepath]
        self.current_instance = instance
        self.user_input_entry.delete(0, tk.END)
        self.user_input_entry.insert(0, instance.user_input)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, instance.output_text)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            self.instances[filepath] = UVSimInstance(filepath)
            self.instance_menu["menu"].add_command(label=filepath, command=tk._setit(self.instance_var, filepath))
            self.instance_var.set(filepath)

    def display_memory(self):
        self.listbox_for_memory.delete(0, tk.END)  # Clear the listbox before displaying memory
        for item in self.current_instance.simulator.instances[self.current_instance.filepath]['memory']:
            self.listbox_for_memory.insert(tk.END, item)

    ##### Passed to UVsim class in UVSim_Class.py #####
    def output_instruction_process(self, text):
        self.output_text.insert(tk.END, text + "\\n")

    def output_user_input_for_read(self, text):
        self.user_input_entry.delete(0, tk.END)  # Clear the entry field
        self.user_input_entry.insert(tk.END, text) 

    def output_accumulator(self, text):
        self.accumulator_entry.delete(0, tk.END)
        self.accumulator_entry.insert(tk.END, text)

    def get_user_input(self):
        user_input = self.user_input_entry.get()
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            self.current_instance.simulator.set_user_input(self.current_instance.filepath, int(user_input))
            self.output_user_input_for_read(user_input)  # Display the user input
            self.user_input_entry.delete(0, tk.END)
        else:
            self.output_label.config(text="Invalid input. Please enter an integer.")

    def handle_user_input(self):
        # when user input is needed
        self.user_input_button.config(state=tk.NORMAL)  # Enable the user input button
        self.master.wait_variable(self.user_input_ready)  # Wait for user input
        self.user_input_ready.set(False)  # Reset the user input flag in the GUI

    def update_user_input_ready(self):
        self.user_input_ready.set(True)

    def output_instruction_process(self, text):
        self.output_text.insert(tk.END, text + "\n")

    def save_file(self):
        selected_file = filedialog.asksaveasfilename()
        if not selected_file:
            return  # User canceled the folder selection
        file_content = '\n'.join(str(item) for item in self.current_instance.simulator.files[self.current_instance.filepath]['memory'])
        try:
            with open(selected_file, 'w') as file:
                file.write(file_content)
            self.output_label.config(text="File saved successfully.")
        except Exception as e:
            self.output_label.config(text="Error occurred while saving the file.")

    def load_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return  # User canceled the file selection
        if os.path.exists(filepath):
            filename = os.path.basename(filepath)
            self.output_label.config(text=filename + " loaded successfully.")
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, filename)  # Update entry1 with the loaded filename
            # Create a new UVSimInstance without executing it.
            if filepath in self.instances:
                self.current_instance = self.instances[filepath]
            else:
                self.current_instance = UVSimInstance(filepath)
                # Update the drop-down menu
                self.instances[filepath] = self.current_instance
                self.instance_menu["menu"].add_command(label=filepath, command=tk._setit(self.instance_var, filepath))
            self.instance_var.set(filepath)
        else:
            self.output_label.config(text="File does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UVSimGUI(root)
    app.mainloop()
