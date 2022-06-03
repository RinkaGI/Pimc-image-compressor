from PIL import Image
from tqdm import tqdm
import os, sys, time

print(' -- WELCOME TO PIMC - RINKADEV -- ')
print('Write your image directory')

originalImageText = input('-> ')

image = Image.open(originalImageText)

print("")
print("")

print('Detecting your Operating System...')

operatingSystem = sys.platform

windowsName = {"win32", "cygwin"}
linuxMacName = {"linux", "linux2", "linux3", "darwin", "aix"}


def clearTerminal():
    if operatingSystem is windowsName:
        os.system('cls')
    elif operatingSystem is linuxMacName:
        os.system('clear')
    else:
        os.system('clear')

clearTerminal()

print('Compressing image...')

for i in tqdm(range(100)):
    image = image.convert('RGB')
    image.save('image_compressed.jpg', quality=15)

print('Finished!')
