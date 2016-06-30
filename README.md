# pyGreek-Prank

pyGreek-Prank is a python script to replace all semicolons(;) in a file to greek question marks(;) . 
You can replace all spaces with "FOUR-PER-EM SPACE" . Run this script on your friends code and watch them pull their hair out  

### Usage

    Problem.py prank <FILENAME>... [-vds]
    Problem.py deprank <FILENAME>... [-vds]
    Problem.py (-h | --help)
    Problem.py --version


    Options:
      -s --space    Also changes the space to different whitespace
      -h --help     Show this screen.
      -d --dest     Does not save backup of text
      --version     Show version.

### Dependences
* [docopt][do1]
* [PyInstaller][pi1] (To Create An Executable)

### How to contribute
All contributions are welcome, from code to documentation to bug reports. Please use GitHub to its fullest-- contribute Pull Requests, contribute tutorials or other wiki content-- whatever you have to offer, we can use it!

### Creating an Executable
To create an executable for your operating system

Install PyInstaller

    pip install pyinstaller

In the directory where the script is stored 

    pyinstaller pygreek.py -F


### License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

### Disclaimer
***I take no responsibility for any harm caused by this prank. Have fun!***

[do1]: http://docopt.org/
[pi1]: https://pythonhosted.org/PyInstaller/index.html