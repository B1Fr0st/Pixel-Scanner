from PIL import Image
import time
import pyperclip
from os import remove
#the only modules required are pyperclip and Pillow

#TODO:Make the user experience more friendly(Make url an input at beginning?)FINISHED
#TODO:Add way to copy raw data while using replit.[Temp fix using print, only works on smaller images before it hits the print limit.]
import requests,shutil




def download_image(image,name):
    response = requests.get(image,stream=True)
    file = open("./"+name,"wb")
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw,file)
    del response


def get_pixel(x,y,img):
  try:
    r,g,b = img.getpixel((x,y))
    return (r,g,b)
  except IndexError:
    return (255,255,255,255)
    
    
def aliased_pixel(x,y,img,pixelSize):
    pixs = [
    get_pixel(x,y-pixelSize,img),
    get_pixel(x-pixelSize,y,img),
    get_pixel(x,y,img),
    get_pixel(x+pixelSize,y,img),
    get_pixel(x,y+pixelSize,img)
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
  img = Image.open(img_path).convert('RGB')
  width,height = img.size
  colors = {}
  row = 0
  pixel = 0
  bitmap = []
  pushArray = ""
  printProgressBar(0,width,prefix="Scanning:",suffix="Complete",length = 50)
  start = time.time()
  while row < height:
    while pixel < width:
      pixCol = get_pixel(pixel,row,img)
      if pixCol not in colors:
        colors[pixCol] = str(len(colors))
          
      pushArray += colors[pixCol]
      pixel += pixSize
      
    
    row += pixSize
    bitmap.append(pushArray)

    pixel = 0
    pushArray = ""
      
    printProgressBar((row-pixSize/2),width,prefix="Scanning:",suffix="Complete",length = 50)
  end = time.time()
  elapsed = end-start
  use_map = {v:k for k,v in colors.items()}
  finalString = "var scene = {\nart:\n"
  finalString += str(bitmap)+",\n"
  finalString += "palette:{"
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
  print("Total time taken to compile image:"+str(elapsed))
  copier = input("Copy data to clipboard? [Y\\N]")
  if copier == "N":
    print(finalString)

  elif copier == "Y":
	  pyperclip.copy(finalString)

		




	

print("Welcome to the Pixel-Scanner project!")
time.sleep(1)
print("Please have your image address copied and ready to go.")
time.sleep(1)
print("Please input your image address.")
url = input("Image Address:")#this is the image I am trying to use.
download_image(url,"PixelArt.jpeg")
pxSize = int(input("Pixel size specified on Pixilart:"))
imgPath = "PixelArt.jpeg"
imgg = Image.open(imgPath).convert("RGB")
width,height = imgg.size
pixSize = width/pxSize
ReturnColors(imgPath,pixSize,pxSize)
remove("PixelArt.png")
