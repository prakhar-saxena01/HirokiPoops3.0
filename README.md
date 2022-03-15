# HirokiPoops ![](icon.ico)

This game is Hiroki's Poops.
Hiroki's Poops is a game where you fly around and dodge poops.

[![Run on Repl.it](https://repl.it/badge/github/mak448a/HirokiPoops3.0)](https://repl.it/github/mak448a/HirokiPoops3.0)

## Website
https://t.googleplay.repl.co


## Releases
You can download any one of the releases at the website above.


## Compiling
### Requirements
1. Python 3.8 or above
2. Pygame 2.0 or above
3. Pyinstaller

### Install dependencies
Install Python from <a href="python.org">python.org</a>.

To install pygame and Pyinstaller, use these commands.

#### Windows

`pip install pygame pyinstaller`

If the above command does not work, try checking if Python is on your path.

#### Mac and Linux
`pip3 install pygame pyinstaller`

### Commands
To compile for any platform, run the following command in the terminal or Command Prompt.

`pyinstaller HirokiPoops.spec`

After the command has completed, there will be two new folders: "dist" and "build."
You may delete the build folder. The compiled version will be in the folder: "dist/HirokiPoops."
