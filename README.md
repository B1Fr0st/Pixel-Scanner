# Pixel-Scanner
Takes in a pixel art image, scans it, gets all the colors, scans it again , and translates it into a bitmap with palette.


USAGE:

Open the PixScanner.py file in an IDE of your choice (IDLE, VSC, etc.)
Go to Pixilart online.
Either create your own pixel art or download one. 

NOTE: There is a new option to use a url. Right click the image you wish to use on Pixilart gallery, and select "Open Image in New Tab". Copy the url and go to "Run the python program". Also make not of the size.

INSTRUCTIONS ON DOWNLOADING:
Click on the pixel art
Right above where it says download, it should have a size. Currently, the program only supports 1:1 image ratios. Make note of the width.
Download the pixel art.

INSTRUCTIONS ON CREATING:
Basically, the same steps, but you make it yourself.

Find the exact path of the file. You will need to rename this to "PixelArt.png". For example:
C:\Users\Mugman\Downloads\9d9k0duj73j.png

becomes:

C:\Users\Mugman\Downloads\PixelArt.png

Run the python program. It should ask you for the size, and the path of the file.

(If you are using a URL, say that you are using a url in the question asked, and paste the url in. Then put in the size.) 

Put these in.
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
