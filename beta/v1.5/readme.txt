----------------------Readme TXT File------------------------------

----------------------File Organizer------------------------------

Welcome to Image Organizer, an official open-source program by
Programming Tube(TM).
This is a cross-platform program!
This is a light-weight, superquick and stable version of File
Organizer build completely using python 3.

Find great Tutorials @ www.youtube.com/c/programmingtubetuts
Walk throught www.iprogrammingtube.blogspot.com for cool stuffs.
__________________________________________________________________
|                                                                |
|      **Note:                                                   |
|             Kindly Run fix_dependencies.bat file before        |
|             using the software for first time                  |
__________________________________________________________________
--------------------------Usage------------------------------------

You can also run the 'reg_organize_files.reg' file to register the
program in windows registry and use the same program from context
menu.

The usage of this software is very user friendly and convenient.
--- 1. Locating the Program using CMD/Terminal--------------------
1. Just Open the Command Prompt.
2. Locate the Directory where the program exists using cd command.
  e.g. If you have stored the program on Desktop, toogle using
      X:> cd Desktop
--- 2. Running the Program using CMD/Terminal---------------------
1. To execute the program, simply write python followed with
  program name.
  e.g. X:\\Desktop> python organize_files.py

2. You must have python3 installed on your system before using the
  program as this program is completely dependent upon python.

------------ Discussing the parameters --------------------------

There are two simple parameters in the program.

1. -f/--folder -> Folder , Not Compulsory.
  This argument takes in the folder on which the program has to
  work.
  By Default, the Folder is set to Current Working Folder where
  the program exists
  If you want to explicitly declare the folder you can use the
  following syntax:
    e.g. X:\\Desktop> python organize_images.py -wf TargetFolder

2. -o/--output -> Output Folder, Not Compulsory.
  This argument is not compulsory, But you can set your own Output
  Directory. The default directory is -> organize_images

    e.g. X:\\Desktop> python organize_images.py -wf Images -of Output

------------------- Dependencies --------------------------------
1. Software:
  a. Python3
2. Modules:
  a. argparse
  b. os
  c. shutil

* In case any import module error arises you can simple install the
modules using following commands in cmd.
  a. argparse
    e.g. X:> pip install argparse

* The later two i.e. os and shutil are inbuilt modules. Hence they
need not to be installed via pip.

-------------------------- License --------------------------------
This program comes with a freeware open source License. Any Usage
or changes with the program is legal!

Find great Tutorials @ www.youtube.com/c/programmingtubetuts
Walk throught www.iprogrammingtube.blogspot.com for cool stuffs.

---------------- END OF README FILE ------------------------------
