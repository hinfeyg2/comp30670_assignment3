COMP30670: Software Engineering (Conversion) Semester II
========================================================
Assignment 3
============
LedSwitcher
===========

Git Repository
---------------
https://github.com/hinfeyg2/comp30670_assignment3

Purpose
-------

The Science Centre is installing a new display board which is constructed from LED lights.
The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain rectangular regions.

This program outputs the number of LEDs which are switched on after implementing a set of commands

Requirements
------------
* python 3
* unittest
* urllib

Installation
------------
python setup.py install

Usage
-----
LedSwitcher {input_command_file}
eg:
LedSwitcher http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt

Tests
-----
To run the tests run /test/tests.py
This will run all tests and will take a very long time.
I advise you to comment out tests which you do not need.

Structure
---------
The LedSwitcher class holds the complete program.
LedSwitcher.py is also the entry point.
The test folder contains all tests and includes the supplied test cases.
Tests are completed using unittest.

The LedSwitcher class has eight methods:

### Constructor ###

Takes an input file location.
Initializes lists and counters.

### parseFile ###
Opens the file containing the assigned data input.
It returns a list with each line in that file or url. It avoids empty lines.

### createTemplate ###
Create a tempate list of the size of the input.

### getParseLines ###
Takes each line from the in the input file and convert it to something readable.

### parseEachLine ###
Parses the data from each line and returns a list with the results.

### changeState ###
Changes the state of the ledStateList with and an input position and state.

### applyValues ###
Apply the valus in the parseList to the ledStateList

### getResult ###
Return the number of on LEDs
