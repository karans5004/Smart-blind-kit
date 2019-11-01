from PIL import Image
import pytesseract
from gtts import gTTS 
import os
import threading
language = 'en'

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


text =  pytesseract.image_to_string(Image.open('text.jpg'))

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
print(text)
os.system("mpg321 welcome.mp3")

