"""
FILES AND DIRECTORIES
=====================
Data which is stored in operating systems has been organized into
appropriate files and folder structures.Working with them is made faster and
allows for the folders to be rearranged according to their purpose. The
setup of directories and files resembles a tree structure, it starts with
the main directory i.e. the root.

Depending on the operating system, directory names will vary. The directory
structure on different operating systems may depend on the name of the
currently logged-in user or the computer name.

A file is a collection of data that has a number of attributes and a
specific order. These files are used to store various types of content,
e.g. text, image, video. They can take on a variety of attributes, such as:
- the ability to read/edit/run
- become a  hidden file which is invisible with standard file browsing
methods,
- become system files that should not be deleted or modified without
appropriate knowledge, as their removal or incorrect modification may cause
a system failure.

Computer files often have an extension. It is an additional element in the
file name that identifies the type of data that is being stored. Often the
extension is associated with a specific computer program that can execute a
given file format, e.g.:
 - file.txt - text format
 - file.docx, file.xlsx, file.pptx - files created in Microsoft Office
 - file.pdf - Portable Document Format - a special format for storing
 text/graphics data
 - file.exe - an executable file - the file for a program (saved in the
 file) that will be executed
 - file.zip, file.rar, file.tar.gz, file.tar, file.7z - archives, i.e. files
 that are packaged in the form of an archive. They contain a set of folders
 and other files and allow for the reduction of the amount of physical
 memory used by the data. Special software is needed to open these files. It is
 often built into the operating system.
 - file.png, file.jpg, file.bmp - graphic files
 - file.mov, file.avi, file.mp4 - files that store video
 - file.java, file.py, file.sh, file.bat - special type of files that take
 their extension name from the programming language in which they were
 prepared.

 Windows
 -------
 In the Windows family, file systems are organized on disks marked with
 letters. The first drive letter is "C". The disks can be divided into
 physical (real devices) or logical disks (division of one physical disk
 into virtual partitions). The "disks" division is used to allocate one disk
 for the operating system and the required software, the next disks are used
 for data storage and organization.

 Directory structure on Windows 10 (systems prior to Windows 10) may have
 minimal differences, but the most important folders are the same on any
 Microsoft system).

 The following directories are distinguished:

  - PerfLogs - Windows event logs (related to Windows performance) are
  stored in this directory

  - Program Files, Program Files (x86)  - depending on the architecture of
  the central unit of our computer, they could use software prepared in the
  32-bit (x86) version or the 64-bit (x64) version. The user will not notice
  the difference in the appearance or behavior of the 32/64 bit software. It is
  a way for the processor to calculate the information. The application
  software is installed in Program Files and Program Files (x86)
  directories. Each program is installed in its own "working" directory,
  where source and configuration files are stored. Without extensive
  knowledge, you should not modify the contents of the Program Files
  directories by yourself - it may cause problems with the system functions.

  - ProgramData (hidden directory) - directories hidden in Windows are
  displayed in a specific way and are invisible to the other user until
  he/she allows them to be displayed. The ProgramData directory stores
  software data used by all system users. For example it can be the system
  Administrator or a user called John Doe. An example of such software is an
  antivirus program that must protect the entire system, regardless of the
  currently logged-in user.

  - Users\username\AppData - the path to the AppData folder will vary
  depending on the username
  The AppData folder stores the settings and applications installed for a
  specific user. These are subdirectories like Roaming, Local and LocalLow.
  Roaming is a directory intended for "network" users, Loca abd LocalLow
  directories are intended for users who are working "locally".

  - Windows - directory containing files related to the operating system,
  you should not modify the contents of this directory without prior knowledge.

  - Windows\System, Windows\System32, Windows\SysWOW64 - system directories
  that store system files, dll files (files that implement key Windows
  functionalities). Different folder names exist depending on the operating
  system. The 'System' directory only exists if there are files that are
  written in the 16-bit technology. System32 stores files prepared to
  support 32 or 64-bit technology. SysWOW directory only comes with 64-bit
  versions of Windows. As with other system directories, it is not
  recommended to modify the system directories by yourself.

LINUX
-----
In the Linux family, the folder structure looks very different than in the
Windows family. It was based on the FHS (Filesystem Hierarchy System)
standard. It all starts with the root directory marked with "/".

In the Linux systems there is the concept of "everything else is a file"
i.e. every element of the system, e.g. a device, the running application,
process, or driver is saved as a file.
 - /bin - binary (executable) files of the most basic system utilities
 - /boot - files needed to boot the system (kernel, initrd)
 - /dev - the files here are not actually files on the disk. They refer to
 devices - through them the system communicates with devices (low-level
 communication)
 - /etc - configuration files, system settings
 - /home - files specifying the settings of each user. I addition the
 directory is intended for saving data such as documents, pictures,
 music and any files we use every day programs
 - /lib - shared system libraries containing functions that are performed by
 others
 - /media - here we have access to removable media (it's a place for
 mounting removable media - e.g. a flash drive or a CD-ROM)
 - /mnt - the disks are "mounted" here (in distributions such as Ubuntu,
 the disks are mounted in /media)
 - /proc - virtual directory containing data about currently running processes
 - /root - root user settings - the root administrator of each Linux system
 with maximum permissions
 - /sbin - command executables that can only be run by the system administrator
 - /tmp - temporary files
 - /user - additional programs that allow a normal system user to work
 - /var - system files, whose contents change frequently, such as program
 /system event logs

 MacOS
 -----
 The directory structure on MacOS is similar to the directory structure on
 Linux. This is due to the fact that both operating systems are historically
 derived from Unix systems.

 The most commonly used directories on macOS are:
 - /Applications - this is the directory where the applications required by
 all system users are installed. When installing software purchased in the
 AppStore, the software is automatically installed in this directory. The
 additional subdirectory /Utilities is responsible for the applications that
 are used to manage the system.
 - /Library - This is the directory where all additional libraries (
 programs) required by others are stored for the software or the system.
 - /Network - directory that contains the list of computers visible in the
 local network. The directory may be empty.
 - /System - operating system files, do not modify the contents of this
 directory yourself.
 - /Users - the user's home directory where all user files are stored.
"""