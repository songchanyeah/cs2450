import tkinter as tk
from tkinter import *
from tkinter import ttk, colorchooser
import os
from myClasses.UVSim_Class import UVSim
import tkinter.filedialog as filedialog

class UVSimGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.uvsim = UVSim(self.output_instruction_process, self.output_accumulator, self.output_instruction_process, self.handle_user_input)
        self.user_input_ready = tk.BooleanVar(value=False)
        self.primary_color = (76, 114, 29)
        self.off_color = (255, 255, 255)
        self.load_color_scheme()
        self.create_widgets()
        self.apply_color_scheme()
        self.file_paths = []

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
        config = f"{','.join(str(value) for value in self.primary_color)}\n{','.join(str(value) for value in self.off_color)}"
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

        # self.filename_label = ttk.Label(self.master, text="Enter the filename:")
        # self.filename_label.grid(row=4, column=0, sticky=tk.W)
        
        # self.entry1 = ttk.Entry(self.master)
        # self.entry1.grid(row=4, column=0, sticky=tk.E)

        ##### Save Color Scheme Button #####
        # self.save_color_scheme_button = tk.Button(self.master, text="Save Color Scheme", command=self.save_color_scheme)
        # self.save_color_scheme_button.grid(row=4, column=4, sticky=tk.W+tk.E)

        self.change_color_button = tk.Button(self.master, text="Change Primary Color", command=self.change_primary_color)
        self.change_color_button.grid(row=8, column=4, sticky=tk.W)


         ##### Save File Button #####
        self.save_button = tk.Button(self.master, text="Save", command=self.save_file)
        self.save_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        ##### Load File Button #####
        self.load_button = tk.Button(self.master, text="Load", command=self.load_file)
        self.load_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ##### Filename Entry #####
        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.execute_button = tk.Button(self.master, text="Execute", command=self.execute_program)
        self.execute_button.grid(row=1, column=4, padx=5, pady=5, sticky="e")

        self.output_label = tk.Label(self.master, text="")
        self.output_label.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="w")

        ### < For UVSim Class > ###
        ##### User Input for Read Operation #####
        self.user_input_for_read_label = tk.Label(self.master, text="Enter an integer between -9999 and 9999:")
        self.user_input_for_read_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.user_input_entry = tk.Entry(self.master)
        self.user_input_entry.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

        self.user_input_button = tk.Button(self.master, text="Enter", command=self.get_user_input)
        self.user_input_button.grid(row=2, column=4, padx=5, pady=5, sticky="e")

        ### < For UVSim Class > ###
        ##### Accumulator #####
        self.accumulator_label = tk.Label(self.master, text="Accumulator: ")
        self.accumulator_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.accumulator_entry = tk.Entry(self.master)
        self.accumulator_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        ##### Memory #####
        self.listbox_for_memory = tk.Listbox(self.master)
        self.listbox_for_memory.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")

        self.scrollbar_for_memory = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.scrollbar_for_memory.grid(row=5, column=1, padx=5, pady=5, sticky="ns")

        self.listbox_for_memory.config(yscrollcommand=self.scrollbar_for_memory.set)
        self.scrollbar_for_memory.config(command=self.listbox_for_memory.yview)

        ### < For UVSim Class > ###
        ##### Instructions Run #####
        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        ### Notebook for tabs ###
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")


    def execute_program(self):
        # Get the currently selected tab index in the notebook
        current_tab_index = self.notebook.index(self.notebook.select())

        # Check if the selected tab index is within the range of available file paths
        if 0 <= current_tab_index < len(self.file_paths):
            filename = self.file_paths[current_tab_index]

            if os.path.exists(filename):
                self.output_label.config(text=filename + " loaded successfully.")
                self.uvsim.execute(filename)
                self.display_memory()
            else:
                self.output_label.config(text=filename + " does not exist.")


    def display_memory(self):
        for item in self.uvsim.memory:
            self.listbox_for_memory.insert(tk.END, item)

    ##### Passed to UVsim class in UVSim_Class.py #####
    def output_instruction_process(self, text):
        self.output_text.insert(tk.END, text + "\n")

    # def output_user_input_for_read(self, text):
    #     self.user_input_entry.insert(tk.END, text)

    def output_accumulator(self, text):
        self.accumulator_entry.insert(tk.END, text)

    def get_user_input(self):
        # self.user_input_from_gui = int(self.user_input_entry.get())
        # self.user_input_entry.delete(0, tk.END)
        # self.uvsim.user_input_from_gui = self.user_input_from_gui  # Set the user_input_from_gui variable in UVSim

        # return self.user_input_from_gui
        user_input = self.user_input_entry.get()
        if user_input:
            self.uvsim.set_user_input(int(user_input))
            self.user_input_entry.delete(0, tk.END)

    def handle_user_input(self):
        # This method is called by UVSim class when user input is needed
        self.user_input_button.config(state=tk.NORMAL)  # Enable the user input button
        self.master.wait_variable(self.user_input_ready)  # Wait for user input
        self.user_input_ready.set(False)  # Reset the user input flag in the GUI

    def update_user_input_ready(self):
        # This method is called by the user input button's command
        self.user_input_ready.set(True)

    def output_instruction_process(self, text):
        self.output_text.insert(tk.END, text + "\n")

    def output_accumulator(self, text):
        self.accumulator_entry.delete(0, tk.END)
        self.accumulator_entry.insert(tk.END, text)

    def save_file(self):
        selected_file = filedialog.asksaveasfilename()
        if not selected_file:
            return  # User canceled the folder selection

        try:
            with open(selected_file, 'w') as file:
                # Write the data to the file
                file.write("Your data to be saved")

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
            self.file_paths.append(filepath)  # Add the file path to the list
            self.create_new_tab(filepath)
            self.uvsim.execute(filepath)
            self.display_memory()
        else:
            self.output_label.config(text="File does not exist.")

    def create_new_tab(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()

        text_widget = tk.Text(self.notebook)
        text_widget.insert("1.0", content)
        text_widget.config(wrap="none")
        text_widget.grid(row=0, column=0, sticky="nsew")

        self.notebook.add(text_widget, text=os.path.basename(filepath))
        text_widget.bind("<FocusIn>", self.on_tab_focus)
    
    def on_tab_focus(self, event):
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        self.current_tab_index = self.notebook.index(self.notebook.select())

if __name__ == "__main__":
    root = tk.Tk()
    app = UVSimGUI(root)
    app.mainloop()


