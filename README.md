# Pixel-Scanner
Takes in a pixel art image, scans it, gets all the colors, scans it again , and translates it into a bitmap with palette.


USAGE:

Open the PixScanner.py file in an IDE of your choice (IDLE, VSC, etc.)
Go to Pixilart online.
Either create your own pixel art or download one

INSTRUCTIONS ON DOWNLOADING:
Click on the pixel art
Right above where it says download, it should have a size. Currently, the program only supports 1:1 image ratios. Make note of the width.
Download the pixel art.

INSTRUCTIONS ON CREATING:
Basically, the same steps, but you make it yourself.

Find the exact path of the file, for example
C:\Users\Mugman\Downloads\9d9k0duj73j.png

Run the python program. It should ask you for the size, and the path of the file. Put these in.
It should eventually output a bitmap in this format:

var scene = {
art:
[

],
palette:{

},
pixSize:100

};

Next, copy the program Translator into a new Khan Academy JS project.
There should be a dummy "scene" var. Copy the scene var provided by PixScanner over that variable, and the program should display the pixel art.
