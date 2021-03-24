import pid_manager
import threading
import time
from threading import Thread
from random import randrange

# Create global variable for the mutex class
mutex = threading.Lock()

# Track number of PID threads created
class PidCounter:
    # Initial value reflects PID range of 300-5000
    def __init__(self):
        self.count = 300

    # Increase the count by 1
    def increment(self):
        self.count += 1

# Create a PID thread instance
class PidThread(Thread):
    # Assign variables from parameters
    def __init__(self, thread_id, name, sleep):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.sleep = sleep

    # Start thread, call PID sleep function, and end thread
    def run(self):
        # Acquire and release mutex lock
        with mutex:
            print("\nStarting " + self.name + " %d" %self.thread_id)
            # Begin the PID process simulation: allocate PID
            pid_status = pid_manager.allocate_pid()
            if pid_status == -1:
                print("\nError: Could not allocate a PID")
            else:
                print("\nAllocated PID %d" %self.thread_id)
        self.pid_sleep()
        print ("\nExiting " + self.name + " %d" %self.thread_id)

    # Continue PID process simulation: sleep for a random
    # period of time then release PID
    def pid_sleep(self):
        time.sleep(self.sleep)
        # Acquire and release mutex lock for function call
        with mutex:
            pid_manager.release_pid(self.thread_id)

# Thread Manager Command Line Interface
# Return -1 on PID map allocation error
def main():
    # Loop until the quit option is selected
    while True:
        try:
            print("\nThread Manager Menu\n")
            print("1: Allocate PID Threads")
            print("2: Quit\n")
            menu = int(input("Menu Selection: "))

            if (menu == 1):
                # Attempt to allocate PID map
                return_value = pid_manager.allocate_map()
                if (return_value == 1):
                    print("\nPID Map successfully initialized")
                else:
                    print("\nError: PID Map initialization failed")
                    return -1

                # Get user input for PID threads to create
                pid_cycles = int(input("\nEnter number of PID threads to create: "))
                threads = []
                # Create an instance of the PID Counter
                counter = PidCounter()
                for i in range(300, 300 + pid_cycles):
                    # Create a PidThread with a random value
                    # set for the sleep parameter
                    thread = PidThread(counter.count, "PID Thread", randrange(10,60))
                    counter.increment()
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
                print("\nPID threads completed")

            elif (menu == 2):
                break
            else:
                print("\nError: Please enter a valid menu option")
        # Handle non-integer input
        except ValueError:
            print("\nError: Please enter a valid menu option or number of threads")

if __name__ == '__main__':
    main()
