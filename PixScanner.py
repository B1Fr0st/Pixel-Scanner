from PIL import Image
import time
import pyperclip

#the only modules required are pyperclip and Pillow.
#currently, 400x400 corrupts on row 27. [Reproduced twice.]
#TODO:Make the user experience more friendly(Make url an input at beginning?)
from bs4 import BeautifulSoup
import requests,urllib.request,shutil


url = "https://art.pixilart.com/00b57f7cf75c5de.png"#this is the image I am trying to use.

def download_image(image):
	response = requests.get(image,stream=True)
	file = open("./PixelArt.png","wb")

	response.raw.decode_content = True
	shutil.copyfileobj(response.raw,file)
	del response
download_image(url)



def get_pixel(img_path,x,y):
    im = Image.open(img_path).convert('RGBA')
    r,g,b,a = im.getpixel((x,y))
    return (r,g,b,a)


#progressbar designed by @greenstick on Stack Exchange
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()




def ReturnColors(img_path,pixSize,pSize):

    print("Scanning all pixels to grab all possible colors.")
    img = Image.open(img_path).convert('RGBA')
    width,height = img.size
    colors = {}
    row = pixSize/2
    pixel = pixSize/2
    bitmap = []
    pushArray = ""
    printProgressBar(0,width,prefix="Scanning:",suffix="Complete",length = 50)
    start = time.time()
    while row < height:
        while pixel < width:
            pixCol = get_pixel(img_path,pixel,row)
            if pixCol in colors:
                pass
            elif pixCol not in colors:
                colors[pixCol] = str(len(colors))
            bit = colors[pixCol]
            pushArray += bit
            pixel += pixSize
        pixel = 0
        if len(pushArray) == pSize:
            row += pixSize
            bitmap.append(pushArray)
        else:
          print("Image corruption on row %i.\n" % ((row-pixSize/2)/pixSize))



        pushArray = ""
        printProgressBar((row-pixSize/2),width,prefix="Scanning:",suffix="Complete",length = 50)
    end = time.time()
    elapsed = end-start
    use_map = {v:k for k,v in colors.items()}
    #final string making a comeback
    finalString = "var scene = {\nart:\n"
    finalString += str(bitmap)+",\n"
    finalString += "palette:{"
    #here is going to be the code for making the colors not need adding "color", and if they do, it'll make it easier
    for item in use_map.items():
        itemm = item
        #so, what we want to do is a few things.
        #1:Add in a newline character between each "item"
        #2:Add in a "color" before each set of RGB items.
        #we can accomplish 1 and 2 with this code:
        item = "" #defines the item as a string
        item += "'"+itemm[0]+"':" # adds in the key
        item += "color"+str(itemm[1]) #adds in the value.
        item += ","
        finalString += item+"\n"
    finalString += "},\n"
    finalString += "pixSize:"+str(pixSize)
    finalString += "\n};"
    copier = input("Copy data to clipboard? [Y\\N]")
    if copier == "Y":
        pyperclip.copy(finalString)
        print("Data copied to clipboard.")
pxSize = int(input("Pixel size specified on Pixilart:"))
imgPath = input("File Path:")
if imgPath == "DEFAULT":
    imgPath = "PixelArt.png"
start = time.time()
for i in range(0,pxSize):
	get_pixel(imgPath,0,0)

finish = time.time()
elapse = finish-start
print("Time taken to read %i pixels:%i seconds"%(pxSize,elapse))
print("Estimated image conversion time:%i minutes"%(elapse*pxSize/60))
imgg = Image.open(imgPath).convert("RGB")
width,height = imgg.size
pixSize = width/pxSize
ReturnColors(imgPath,pixSize,pxSize)