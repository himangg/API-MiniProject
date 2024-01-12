## Speech recognition ##
print('Speak stock name')

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2,duration=0.2)
    audio2=r.listen(source2)
    MyText=r.recognize_google(audio2)
    MyText=MyText.lower()
    print(MyText)
print('Speak time series')
r = sr.Recognizer()
with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2,duration=0.2)
    audio2=r.listen(source2)
    timelimit=r.recognize_google(audio2)
    timelimit=timelimit.lower()
    print(timelimit)

# MyText='reliance'
# timelimit='DAILY'

import requests
import json
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timelimit}_ADJUSTED&symbol={MyText}.BSE&outputsize=full&apikey=X6IQZUMIBD421RAY'
r = requests.get(url)
data = r.json()
print(data)
date=input('Enter the date in the format(yyyy-mm-dd):')
print(list(list(data.values()))[1][date])


Buttons
from tkinter import *   
top = Tk()  
top.geometry("100x300")  
def open():
    print(list(data.values())[1][date]['1. open'])
def high():
    print(list(data.values())[1][date]['2. high'])
def low():
    print(list(data.values())[1][date]['3. low'])
def close():
    print(list(data.values())[1][date]['4. close'])
def volume():
    print(list(data.values())[1][date]['6. volume'])
b1 = Button(top,text = "OPEN",command = open,activeforeground = "black",activebackground = "pink",pady=10)  
b2 = Button(top, text = "HIGH",command = high,activeforeground = "black",activebackground = "pink",pady=10)  
b3 = Button(top, text = "LOW",command = low,activeforeground = "black",activebackground = "pink",pady = 10)  
b4 = Button(top, text = "CLOSE",command = close,activeforeground = "black",activebackground = "pink",pady = 10)  
b5 = Button(top, text = "VOLUME",command = volume,activeforeground = "black",activebackground = "pink",pady = 10)
b1.pack()  
b2.pack()  
b3.pack()  
b4.pack()  
b5.pack()
top.mainloop()