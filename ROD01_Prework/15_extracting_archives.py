"""
EXTRACTING ARCHIVES
===================

An archive is a special type of file that contains files and directories.
Why can't we actually keep files in a folder? The problem arises when our
set of files take up a lot of space or the files and folders themselves are
just big. In the case of copying/sending such a data set, it is much easier
to send one simple file, which compressed, will take up less space on the
hard disk. The archive can be created using dedicated application software.
Archive files can have different file extensions, e.g. in Windows systems (
file.zip, file.7z, file.rar), and in Linux systems (file.tar, file.tar.gz,
file.tar.xz, file.bz2, file.tgz, file.gz).

Working with archives - LINUX/macOS only
----------------------------------------
In the case of Unix systems, we can use the terminal and specially designed
commands for creating archives:

- creating a .zip file
zip-r  my_archive /path/to/my_archive.zip

- creating a .tar file without compression
tar -cvf my_archive /path/to/my_archive.tar

- compressing a .tar file => .tar.gz
tar czvf my_archive /path/to/my_archive.tar

- compressing a .tar file to a .bzip2.gz file
tar -cjvf my_archive /path/to/my_archive.tar


Extracting archives:
- extracting the .zip archive
unzip my_archive.zip

- extracting the tar archive
tar -xvf my_archive.tar

- extracting the .tar.gz archive
tar -xzvf my_archive.tar.gz

- extracting the .tar.bz2 archive
tar -xjvf my_archive.tar.bz2
"""