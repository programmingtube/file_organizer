# File Organizer {Stable Build} Version -> 1.0

Welcome to File Organizer by <strong>Programming Tube(TM).</strong>

This is a very lightweight, superquick and user friendly program which allows you to organize files based on their file types in specific folders. This program is entirely written in <strong>Python3</strong> and completely depends on it and its modules/packages.

This is an open-source cross-platform tools, primarily built for <strong>Microsoft Windows</strong> users.

# Usage
_______________________________________________________________________________________
*<strong> Note: Kindly Run fix_dependencies.bat file before using the software for first time.</strong>
_______________________________________________________________________________________

<strong>You can also run the 'reg_organize_files.reg' file to register the program in windows registry and use the same program from context menu. You need to copy the script to drive "C:\" before registering it on your windows machine.</strong>

<h2>1. Locating the Program using CMD/Terminal</h2>
        1. Just Open the Command Prompt.<br>
        2. Locate the Directory where the program exists using cd command.<br>
        e.g. If you have stored the program on Desktop, toogle using<br>
        <strong>X:> cd Desktop</strong>
        
<h2>2. Running the Program using CMD/Terminal</h2>
      1. To execute the program, simply write python followed with program name.<br>
      e.g.<strong>X:\\Desktop> python organize_files.py</strong><br>
      2. You must have python3 installed on your system before using the program as this program is completely dependent upon python.
      
# Discussing the parameters
There are two simple parameters in the program.

<h3>1. -wf/--workingfolder -> Folder , Not Compulsory.</h3>
  This argument takes in the folder on which the program has to work.<br>
  <strong>By Default, the Folder is set to Current Working Folder where the program exists.</strong><br>
  If you want to explicitly declare the folder you can use the following syntax:<br>
    <strong>e.g. X:\\Desktop> python organize_images.py -wf TargetFolder</strong>

<h3>2. -of/--outputfolder -> Output Folder, Not Compulsory.</h3>
  This argument is not compulsory, But you can set your own Output Directory.<br>
  <strong>The default directory is -> organized_files.</strong><br>
    <strong>e.g. X:\\Desktop> python organize_images.py -wf Images -of Output</strong>
    
# Dependencies
<h3>1. Base Software:</h3>
  a. Python3
<h3>2. Packages/Modules:</h3>
  a. argparse<br>
  b. os<br>
  c. shutil<br>
  d. pathlib<br>
  e. time<br>
  f. sys<br>
  g. tempfile<br>
  
_____________________________________________________________________
 * In case any import module error arises you can simple install the
modules using following commands in cmd.
  e.g. <strong>X:> pip install <module/package></strong>
_____________________________________________________________________
 
______________________________________________________________________________________________________
 # License
This program comes with a freeware open source License. Any Usage or changes with the program is legal!
______________________________________________________________________________________________________

<strong>Find great Tutorials @ www.youtube.com/c/programmingtubetuts .<br>
Walk through. www.iprogrammingtube.blogspot.com for cool stuffs.</strong>
______________________________________________________________________________________________________
# END OF README FILE
______________________________________________________________________________________________________
    
