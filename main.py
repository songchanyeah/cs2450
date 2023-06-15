from myClasses.UVSim_Class import UVSim
import subprocess
#this file is to run the main python program.

def main():
    subprocess.run(['/usr/local/bin/python3', 'reset_script.py'])
    uvsim = UVSim()
    uvsim.execute()

if __name__ == "__main__":
    main()
