MIN_PID = 300
MAX_PID = 5000

# Create and initialize a list data structure that represents PIDs.
# 0 indicates PID availability and 1 indicates the PID is in use.
# Return 1 on successful list initialization.
# Return -1 on list initialization error.
def allocate_map():
    global pid_list
    # Initializes a list with index range of 0 to 4700
    pid_list = [0 for i in range(4701)]
    if (pid_list):
        return 1
    else:
        return -1

# Allocate the next available PID.
# Return 1 on successful PID allocation..
# Return -1 on PID allocation error.
def allocate_pid():
    # Search pid_list for the first index with an element value of zero.
    try:
        index = pid_list.index(0)
        pid_list[index] = 1
        return index + 300
    # Catch error for attempting to access pid_list global if it does not exist.
    except NameError:
        print("\nError: Please initialize the PID map")
        return -1
    # Catch error for no PIDs being available from pid_list.
    except ValueError:
        print("\nError: PID Map not initialized or all PIDs in use")
        return -1

# Release a specific PID in the inclusive range of 300 to 5000.
def release_pid(pid):
    # Parse an integer from callee and set the pid_list index's element to zero.
    try:
        pid = int(pid)
        if (pid < MIN_PID):
            print("\nError: Cannot release a PID value less than 300")
        elif (pid > MAX_PID):
            print("\nError: Cannot release a PID value greater than 5000")
        else:
            pid_list[pid - 300] = 0
            print("\nPID %d has been released" %pid)
    # Catch error for attempting to access pid_list global if it does not exist.
    except NameError:
        print("\nError: Please initialize the PID map")

# PID Manager Command Line Interface
def main():
    while True:
        try:
            print("\nPID Manager Menu\n")
            print("1: Allocate Map")
            print("2: Allocate PID")
            print("3: Release PID")
            print("4: Quit\n")
            menu = int(input("Menu Selection: "))

            if (menu == 1):
                return_value = allocate_map()
                if (return_value == 1):
                    print("\nPID Map successfully initialized")
                else:
                    print("\nError: PID Map initialization failed")
            elif (menu == 2):
                return_value = allocate_pid()
                if (return_value != -1):
                    print("\nAllocated PID %d" %return_value)
            elif (menu == 3):
                release_pid(int(input("Enter PID to be released: ")))
            elif (menu == 4):
                break
            else:
                print("\nError: Please enter a valid menu option")
        except ValueError:
            print("\nError: Please enter a valid menu option or PID value")

if __name__ == '__main__':
    main()
