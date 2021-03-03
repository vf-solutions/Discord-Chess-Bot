import json
from PIL import Image
from urllib.request import urlopen
import requests
import time
from colorama import Fore, Back, Style 
foundcards = ""
#https://github.com/public-apis/public-apis/blob/master/README.md


with open("url.txt") as file:
  site = file.readline()

#this will be modified with the text
r = requests.get(site)
text = r.text
cards = json.loads(text)