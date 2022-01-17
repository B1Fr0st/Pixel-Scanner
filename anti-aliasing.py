
#This program is intended to experiment with anti-aliasing.
#What it should do is return a function that takes a set of coordinates on a image capture (x,y,img_var), get the average color of the pixels in a radius of 2, then return that color.
from PIL import Image

def get_pixel(x,y,img_var):
    r,g,b,a = img_var.getpixel((x,y))
    return (r,g,b,a)

def aliased_pixel(x,y,img_var,pixelSize):
    pixs = [
    get_pixel(x,y-pixelSize,img_var),
    get_pixel(x-pixelSize,y,img_var),
    get_pixel(x,y,img_var),
    get_pixel(x+pixelSize,y,img_var),
    get_pixel(x,y+pixelSize,img_var)
    ]
    r = 0
    g = 0
    b = 0
    a = 0
    for pixel in pixs:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]
        a += pixel[3]
    r = r/len(pixs)
    g = g/len(pixs)
    b = b/len(pixs)
    a = a/len(pixs)
    return (r,g,b,a)
    

print(aliased_pixel(0,0,Image.open("").convert("RGBA"),1))