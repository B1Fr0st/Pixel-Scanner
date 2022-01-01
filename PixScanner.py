from PIL import Image
import time

#this is really inefficent, so only use it on pixel arts 100 or smaller, anything above that:
# A:Takes forever
# B:Corrupts
# C:Does both




def get_pixel(img_path,x,y):
    im = Image.open(img_path).convert('RGBA')
    r,g,b,a = im.getpixel((x,y))
    return (r,g,b,a)


#progressbar designed by @greenstick on Stack Exchange
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
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
    colors = []
    row = pixSize/2
    pixel = pixSize/2
    printProgressBar(0,width,prefix="Scanning:",suffix="Complete",length = 50)
    start = time.time()
    while row < height:
        while pixel < width:
            pixCol = get_pixel(img_path,pixel,row)
            if pixCol in colors:
                pass
            elif pixCol not in colors:
                colors.append(pixCol)
            pixel += pixSize
        pixel = 0
        row += pixSize
        printProgressBar((row-pixSize/2),width,prefix="Scanning:",suffix="Complete",length = 50)
    end = time.time()
    elapsed = end-start
    print("Number of colors in image:"+str(len(colors)))
    print("Time taken to map colors:%i secs." %(elapsed))
    colorDict = {}
    i = 0
    while i < len(colors):
        colorDict[colors[i]] = str(i)
        i += 1
    print("Colors mapped and converted to dictionary. Returning colorDict")
    return colorDict







def returnMap(img_path,pixSize,pSize):
    print("Beginning translation of image into bitmap.")
    img = Image.open(img_path).convert("RGBA")
    width,height = img.size
    colors = ReturnColors(img_path,pixSize,pSize)
    row = pixSize/2
    pixel = pixSize/2
    bitmap = []
    pushArray = ""
    printProgressBar(0,width,prefix="Mapping:",suffix="Mapped",length=50)
    start = time.time()
    while row < height:
        while pixel < width:
            pixCol = get_pixel(img_path,pixel,row)#Gets current pixel
            bit = colors[pixCol]
            pushArray += bit
            pixel+= pixSize
        pixel = 0
        if len(pushArray) == pSize:
            row += pixSize
            bitmap.append(pushArray)
        else:
            print("Image corruption on row %i.\n" % ((row-pixSize/2)/pixSize))
        pushArray = ""
        
        printProgressBar((row-pixSize/2),width,prefix="Mapping:",suffix="Mapped",length=50)
    use_map = {v:k for k,v in colors.items()}
    print("\n\n\n\n\n\n\n\n\n\n\n\nvar scene = {\nart:")
    print(str(bitmap)+",")
    print("palette:{")
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
        print(item)
    print("},")
    print("pixSize:"+str(pixSize))
    print("};")
    end = time.time()
    elapsed = end-start
    print("Time taken to convert image:%i secs." %(elapsed))

pxSize = int(input("Pixel size specified on Pixilart:"))
imgPath = input("File Path:")
if imgPath == "DEFAULT":
    imgPath = "PixelArt.png"

imgg = Image.open(imgPath).convert("RGB")
width,height = imgg.size
pixSize = width/pxSize
returnMap(imgPath,pixSize,pxSize)