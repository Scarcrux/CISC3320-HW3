Mutexes Design Documentation

In the Thread Manager CLI, modify thread creation to append threads to a list. Then use join() to wait on completion of all threads before displaying the menu again.

Import the threading class and set a global variable to create an instance of the Lock class. Use "with global_variable_name:" to acquire and release locks for the calls to PID Manager within the PID Cycle function.
