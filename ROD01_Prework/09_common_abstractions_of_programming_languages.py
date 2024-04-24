"""
Common Abstractions of Programming Languages
============================================

ABSTRACTIONS are a characteristic of high-level programming languages. They
are used to hide the details of the execution of our programs so that their
design and development is easier.

e.g. computers use only sequences of 0 and 1 that are not intuitive for us.

Variables
---------
Areas of the memory on our computer. Like a parking space for a value.
variable name:  ageOfFather
variable value: 67
memory address: 0x7FFFEB04, 0x7FFFEB05, 0x7FFFEB06, 0x7FFFEB07
content:        00000000,   00000000,   00000011,   00000000

Data Type
---------
Using a data type we determine the use of a variable allowing a compiler or
an interpreter to determine how it will be stored in the memory of our
computer.

e.g.
Boolean Value Type
Integers
Floating Point Numbers
Character Type
Text Type (usually referred to as string) => as a result we don't have to
worry about text encoding in our day-to-day work.

Complex Data Types
------------------
- Structures:
    - used to store related data, consists of fields of different types that we
     can name
    - structure Person could have the fields: first name (text), last name (
    text), age (number, integer)

- Arrays:
    - used to store sequences of data together, and offer mechanisms to
    access and modify the data

Operators
---------
Operators allow us to perform the most basic actions on our data
+, -, *, /

Control Instructions
--------------------
Give us the possibility to create programs that are not linear.

Conditional statements like: if, else
Loops - used to repeat a set of instructions from the program
e.g. counting down from a number, like from 100 to 0.

Procedures
----------
Also known as functions or methods, represent a program inside a program,
it executes a set of instructions (acting towards a common goal). It serves
to avoid duplication of code. It helps to organize code.
Procedures (functions) can accept values on which they perform operations.
These values are called parameters or arguments. They can return a value to
be placed in the code that calls them. 
"""