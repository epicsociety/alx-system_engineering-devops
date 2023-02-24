cat /proc/PID/cmdline displays name of the command (along with any options and arguments) that the process was started with

cat /proc/PID/status display the contents of the status file for the given PID

We can access process environment in C through:
           the global variable ‘extern char **environ;
	   the third argument to the main() function ‘char *envp[]’

getenv – Get value of a particular environment variable
setenv – Set a new value to an environment variable


man 7 signal
A signal is just like an interrupt; when it is generated at the user level, a call is made to the kernel of the OS, which then acts accordingly.

There are two types of signals:

Maskable: signals which can be changed or ignored by the user (e.g., Ctrl+C).
Non-Maskable: signals which cannot be changed or ignored by the user. These typically occur when the user is signaled for non-recoverable hardware errors
