"""
Environment Variables
=====================

Operating systems often contain a lot of application programs that require
different software to run, e.g. a programming language or an additional
library. System variables have been created to speed up communication
between software and to speed up the way a user runs software. A variable in
its definition is a certain object in which we can store a value.


Windows Environment Variables
-----------------------------
%USERNAME%      name of the current user
%HOMEPATH%      name of the user's home directory
%COMPUTERNAME%  computer name

The %% character are representative of Windows environment variables.
To display an environment variable:
echo %COMPUTERNAME%

We can use the command line to set the environment variables. Note,
this setting is only active when using the command line:
C:\Users\john.doe>set MY_VARIABLE="TEST"


Linux/macOS Environment Variables
---------------------------------
The purpose of environment variables on Linux/macOS is identical to Windows.
The big difference in Unix systems is the way environment variables are
defined and stored. On Unix-derived systems, environment variables are
stored in a special .bashrc hidden file. By default, this file is located in
the user's home directory, which is accessed by the $ HOME environment
variable.

The file can also be opened in any text editor. It is not recommended to
edit the file without admin knowledge as it may crash your system.

 $HOME      path to your home directory
 $HOSTNAME  the computer name
 $OSTYPE    the type of operating system

An important difference from the Windows family is that the variables
contain a dollar sign and the variable name.

To display a variable name in Linux:
echo $OSTYPE

To set the environment variable, we can run the command export.
export $HOSTNAME="the_machine_of_a_dream"

Again, setting the environment variable like this is only active when using
the terminal. To set an environment variable permanently, you need to edit
the .bashrc file by adding a new line.
"""