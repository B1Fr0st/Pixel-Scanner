# Pixel-Scanner
Takes in a pixel art image, scans it, gets all the colors, scans it again , and translates it into a bitmap with palette.


USAGE:

Open the PixScanner.py file in an IDE of your choice (IDLE, VSC, etc.)
Go to Pixilart online.
Either create your own pixel art or download one. 

Publish the pixel art, then open the post and right click on the image. It should show a context menu, select "copy image address". Don't close the pixilart post, as you'll need it later.

Run the program. It should ask you for the image address. Right click the program, select "paste", then press enter.

Go back to the pixilart post. Find where it says the image size. Remember it,and then put it into the program.

NOTE: As of right now, certain artworks do not convert. This is most likely an issue with gradating colors interfering with the reader. If this happens, I'm sorry, but there is no way to convert it AORN.


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
