"""
NAVIGATING THROUGH DIRECTORIES
==============================

One of the most frequently performed operations in operating systems are the
ones done on files and directories. Those actions may include creating,
editing, or deleting files and directories. However, before we move on to
file operations, you should navigate through directories in a relatively
efficient way. There are two ways to accomplish this:
 - via the graphical interface
 - via a text interface (by using a command line terminal)

Graphical User Interface
------------------------

Navigating the graphical user interface is very intuitive. The user switches
between directories using the keyboard or mouse and specialized auxiliary
icons. In Windows, the user can:
 - use shortcuts to the most frequently used directories (Quick Access)
 - use shortcuts in the toolbar (moving, copying, deleting, opening,
 editing, changing the properties of files and directories)
 - use the search engine

 The user can view the properties of a file/directory through the context
 menu (Right Mouse Button -> Properties - depending on the language version
 of the operating system), here you can preview such items as:
 - the file type/extension - including which computer program supports it
 - the file/directory location
 - the file/directory size
 - the date of creation/modification/last access
 - the attributes - whether it's a read-only file or hidden file

Navigating the graphical interface in Linux is very similar.
 - use shortcuts to the most frequently used directories
 - use the shortcuts in the toolbar
 - use the search engine

Context menu in Linux - access to properties.

The macOS system differs from other systems mainly in the graphical
interface, but the principle of operation remains the same:
 - use the shortcuts to the most frequently used directories
 - use the shortcuts in the toolbar
 - use the search engine


 Text Interface
 --------------
 The second way to navigate through directories (and not only to navigate
 through directories, but also to manage the entire system) is through the
 text interface. This is where the user can issue commands to the operating
 system in text form. Current operating system are graphics based, but for
 quite a long time a text interface was the only way to issue commands to
 the operating system and get feedback.

 A text interface (it is also graphical) is often called a shell because it
 is an intermediary between the user and the operating system or the
 applications. There are very large number of text interfaces, but the most
 popular are:
  - Windows - Command Line / Powershell (blue command line)
  - Linux, MacOS - Terminal

The commands issued in the text interface consists of the following elements:
 - Command - make a directory
 - Option - make it read-only
 - Argument - directory name

 $ mkdir -m 777 first_directory
 $ ls -la

In the example above, the command to create a directory was invoked,
with permissions to read/modify/write the directory by all users, named "first
-directory". Then the "ls" command was called, which is responsible for
displaying the contents of the directory in which we are currently located.
The result of the command can be seen on the screen. Finally, the same
command was called, only in long form.

 $ mkdir --mode 777 second_directory

Windows Command Line Commands
-----------------------------
 - cd will allow to display or specify the current working directory
 - dir - will display all files and directories from the directory in which
 we are currently located
 - echo 'Test' - will display the selected text on the screen, most commonly
 used to display environment variables
 - mkdir - allows you t create a new directory in the current location
 - rmdir - will allow you to delete the specified directory
 - del test.txt will delete the selected file

Options can be passed to Windows commands as well:
 rmdir /S  - will remove a directory even when the directory is not empty
 rmdir /?  - will display help on the rmdir command

Linux/MacOS Terminal Commands
-----------------------------
Linux and macOS commands are identical. They both come from the Unix family
of systems. They have many similar elements including the way to issue
commands using a text interface. On Linux/MacOS, the text interface is
called a "Terminal". It can be accessed in a similar way as in Windows.
 - pwd - display the current working directory
 - ls - display all files and directories from from the directory in which
 we are currently located
 - echo - used to display environment variables
 - cd - use this command to change the current directory
 - mkdir - create a directory
 - rmdir - delete a directory
 - rmdir --help -will display the documentation of the command
 - rm -f force delete a file
 - rm --force same command but in long form

Relative/absolute path
----------------------
Directories and files that exist in the operating system are represented by the
appropriate path:
WINDOWS - C:\Program Files\Google\Chrome\Application\chrome.exe
LINUX   - /opt/google/chrome/default_apps/gmail.crx

The first fundamental difference that appears in defining the path is the
way of saving - in the case of Windows systems we use the backslash \ to
separate specific directories, in the case of Unix systems we use the
standard / slash. The second difference is the lack of a drive letter on
Unix systems, this is how the operating system is built.

An absolute path describes the location of an item on the disk
unambiguously. It always starts with the topmost element, the root.
 - Windows - C:\Users\john.doe\Documents\file.txt
 - Linux   - /Users/john.doe/Documents/file.txt

A relative path points to a file or folder relative to the current location.
 - Windows - .\Documents\file.txt
 - Linux/Mac - ./john.doe/Documents/file.txt

Important Considerations
------------------------
 - the names of files and directories allow you to put spaces in the name,
 the path with a space is put in quotation marks, thanks to which we will
 avoid a situation that our terminal will misinterpret the name of our file
 or directory.
 Windows - "C:\Users\john.doe\text file.txt"
 Linux   - "./john.doe/Documents/text file.txt"

If we replace a space with a period or an underscore, there is no need to
use quotation marks. When creating files or directories, you need to
remember to create an easily identifiable name with no diacritics. In the
case of files, It is also worth taking care of the appropriate file
extensions. The operating system will automatically associate the created
file with the appropriate application software.


"""