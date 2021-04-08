Mutexes Design Documentation

Import the threading class and set a global variable to create an instance of the Lock class. Use "with global_variable_name:" wrapping to acquire and release locks for initialization of a PID as well as termination.

Create a PID counter class with a count variable and increment member function. Move the PID cycle function to become a member function of the PID thread class. Move the PID allocation functionality into the run member function. Wrap the starting thread output and PID allocation with a mutex. Rename the PID cycle function to PID sleep due to its more limited functionality.

Create an instance of the PID counter class within the Thread Manager CLI and use the counter variable in calls to create PID Thread instances. Increment the counter after every call.

In the Thread Manager CLI, modify thread creation to append threads to a list. Then use join() to wait on completion of all threads before displaying the menu again.

