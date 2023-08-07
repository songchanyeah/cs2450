# cs2450
CS2450 Software Engineering Group Project

To run Pytest in the terminal run the command:
Python3 -m pytest


# UVSimGUI 

UVSimGUI is a graphical user interface (GUI) for the UVSim. It provides an easy-to-use interface for loading and executing assembly programs, as well as interacting with the UVSim's memory and accumulator.

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python except for python 3.11 and above needs manual tkinter instilation)

## Getting Started

1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install tkinter if it's not already installed. Most Python installations come with tkinter by default.
4. Open a terminal or command prompt and navigate to the directory where you downloaded/cloned the repository.

## Running the Application

To start the UVSim application, execute the following command in the terminal/command prompt when you have navigated to the cs2450 file:

```
python main.py
```

## Using the Application

### Color Scheme

- To change the primary background color of the application, click the "Change Primary Color" button. A color picker dialog will appear, allowing you to choose a new color.

### File Operations

- **Load**: Click the "Load" button to open a file dialog and select an assembly program file (.txt) to load into the UVSim.

- **Save**: Click the "Save" button to save the contents of the currently selected tab to a new file. A file dialog will appear, allowing you to choose the save location and filename.

### Tabs

- The application uses a tab-based interface to handle multiple assembly program files. Each tab represents a different program file that has been loaded and user is able to edit the files when wanted.

### Execution

- To execute the assembly program in the currently focused tab, first ensure that the tab is focused (click on the tab if it is not focused), and then click the "Execute" button. The program will be loaded into the UVSim and executed, displaying the output in the "Instructions Run" section and updating the "Accumulator" and "Memory" sections.

### User Input

- During program execution, the UVSim may prompt for user input (e.g., for a "READ" operation). When this happens, the "Enter an integer between -9999 and 9999" label and an input entry box already there you can put input into. Enter an integer value within the specified range and click the "Enter" button to provide the input to the UVSim.

### Exiting the Application

- To close the application, simply close the window by clicking the close (X) button.

## Credits

- Daniel Wilsher

- Jordan Convey

- Chan Song

- Denis Davis

---