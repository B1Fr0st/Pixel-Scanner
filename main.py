from PIL import Image
import time
import pyperclip
from os import remove
from functools import cache
#the only modules required are pyperclip and Pillow
#currently, 400x400 corrupts on row 27. [Reproduced twice.]
<<<<<<< HEAD:main.py
#TODO:Make the user experience more friendly(Make url an input at beginning?)FINISHED
#TODO:Add way to copy raw data while using replit.https://art.pixilart.com/c78901132398980.png
import requests,shutil




def download_image(image,name):
	response = requests.get(image,stream=True)
	file = open("./"+name,"wb")

	response.raw.decode_content = True
	shutil.copyfileobj(response.raw,file)
	del response
=======
#TODO:Make the user experience more friendly(Make url an input at beginning?)FINISHED
#TODO:Add way to copy raw data while using replit.
import requests,shutil
>>>>>>> origin/main:PixScanner.py




def download_image(image,name):
	response = requests.get(image,stream=True)
	file = open("./"+name,"wb")

	response.raw.decode_content = True
	shutil.copyfileobj(response.raw,file)
	del response


@cache
def get_pixel(img_path,x,y):
  im = Image.open(img_path).convert('RGBA')
    


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
<<<<<<< HEAD:main.py
    while pixel < width:
			
      r,g,b,a = img.getpixel((pixel,row))
      pixCol = (r,g,b,a)
      if pixCol in colors:
        pass
      elif pixCol not in colors:
        colors[pixCol] = str(len(colors))
          
      pushArray += colors[pixCol]
      pixel += pixSize
      
    if len(pushArray) == pSize:
      row += pixSize
      bitmap.append(pushArray)
    pixel = 0
    pushArray = ""
      
    printProgressBar((row-pixSize/2),width,prefix="Scanning:",suffix="Complete",length = 50)
=======
      
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
>>>>>>> origin/main:PixScanner.py
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
  print("Total time taken to compile image:"+str(elapsed))
  copier = input("Copy data to clipboard? [Y\\N]")
  if copier == "N":
    print(finalString)

  elif copier == "Y":
	  pyperclip.copy(finalString)

		


oss = input("Are you using a windows installed code runner? (no online IDES) [Y\\N]")
if oss == "N":
	exit()
elif oss == "Y":
	pass
else:
	print("Invalid response.")
	exit()
isUrl = input("Did you download the image already or are you going to use a url? [True/False; True for downloaded]")
deleteImg = input("Would you like to delete the image after it is converted?[True\\False]")
if isUrl == "True":
	pass
else:
	url = input("URL:")#this is the image I am trying to use.
	download_image(url,"PixelArt.png")
pxSize = int(input("Pixel size specified on Pixilart:"))
imgPath = "PixelArt.png"
<<<<<<< HEAD:main.py
=======
start = time.time()
for i in range(0,pxSize):
	get_pixel(imgPath,0,0)

finish = time.time()
elapse = finish-start
print("Time taken to read %i pixels:%i seconds"%(pxSize,elapse))
print("Estimated image conversion time:%i minutes"%(elapse*pxSize/60))
>>>>>>> origin/main:PixScanner.py
imgg = Image.open(imgPath).convert("RGB")
width,height = imgg.size
pixSize = width/pxSize
ReturnColors(imgPath,pixSize,pxSize)
if deleteImg == "True":
	remove("PixelArt.png")