'''Monty the motivational penguin, a free tool for astrophysics students at Oxford to help them destress when coding.
Written by Sam Spencer 13/3/2018, provided as is.'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from PIL import Image,ImageFont,ImageDraw
import time
import psutil

filedir=os.path.dirname(os.path.abspath(__file__))
database=[]
with open(filedir+'/quotes_all.csv') as csvfile:
          quotesdat=csv.reader(csvfile,delimiter=';')
          for row in quotesdat:
              database.append(row[0])

while True:
    quote=''
    while len(quote)==0:
        randomnumber=np.random.randint(len(database))
        testquote=database[randomnumber]
        if len(testquote)<50:
            quote=testquote
        else:
            continue

    penguin=Image.open(filedir+'/penguin-funny-blue-water-86405.jpeg')
    draw = ImageDraw.Draw(penguin)
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    draw.text((0, 300),database[randomnumber],(255,255,255),font=fnt)
    
    penguin.show()
    time.sleep(30)
    penguin.close()
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    time.sleep(1200)
