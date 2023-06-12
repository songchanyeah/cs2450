from UVSim_Class import UVSim

#this file is to run the main python program.

def main():
    testFile = "Test1.txt"
    uvsim = UVSim()
    uvsim.load(testFile)
    uvsim.execute()

if __name__ == "__main__":
    main()
