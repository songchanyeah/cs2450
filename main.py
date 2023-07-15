import tkinter as tk
from tkinter import *
import os
from myClasses.UVSim_Class import UVSim

class UVSimGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.uvsim = UVSim(self.output_instruction_process, self.output_accumulator)
        self.create_widgets()
        self.user_input_ready = tk.BooleanVar(value=False)

    def create_widgets(self):
        ##### Filename #####
        self.filename_label = tk.Label(self.master, text="Enter the filename:")
        self.filename_label.grid(row=0, column=0, sticky=W)

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
        justfilename = self.entry1.get()
        current_dir = os.getcwd()
        current_dir = current_dir + "\Test Files\\"
        filename = current_dir + justfilename

        # if filename:
        if os.path.exists(filename):
            self.output_label.config(text = justfilename + " loaded successfully.")
            self.entry1.delete(0, tk.END)
            print(self.uvsim.memory)
            self.uvsim.execute(filename)
            self.display_memory()
        else:
            self.output_label.config(text = justfilename + " does not exist.")
            self.entry1.delete(0, tk.END)


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
        self.user_input_from_gui = int(self.user_input_entry.get())
        self.user_input_entry.delete(0, tk.END)
        self.uvsim.user_input_from_gui = self.user_input_from_gui  # Set the user_input_from_gui variable in UVSim

        return self.user_input_from_gui

    

if __name__ == "__main__":
    root = tk.Tk()
    app = UVSimGUI(root)
    app.mainloop()




# self.load_button = tk.Button(self.master, text="Load File", command=self.load_file)
# self.load_button.pack()

# def load_file(self):
#     filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#     if filename:
#         self.entry.delete(0, tk.END)
#         self.entry.insert(tk.END, filename)
#         self.uvsim.load(filename)
#         self.output_text.insert(tk.END, "File loaded successfully.\n")

# from myClasses.UVSim_Class import UVSim

# #this file is to run the main python program.

# def main():
#     uvsim = UVSim()
#     uvsim.execute()

# if __name__ == "__main__":
#     main()

