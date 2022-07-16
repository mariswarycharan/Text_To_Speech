from cProfile import label
from logging import root
from tkinter import *
from turtle import speed
import pyttsx3
from tkinter.ttk import Combobox
from tkinter.font import BOLD, ITALIC
root = Tk()
root.configure(background="#33ccff")

engine = pyttsx3.init()
l1 = Label(root,padx=250,pady=10,background="#33ccff")
l1.grid(row=1,column=1)

title = Label(root,text="TEXT TO SPEEECH",font = ("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",40,BOLD,ITALIC), foreground="red",background="black",padx=85,pady=5)
title.grid(row=1,column=2,columnspan=5)

# l1 = Label(root,padx=250,pady=10,background="#33ccff")
# l1.grid(row=2,column=2)

text = Text(root,width=75,height=25,font=("C:/Users/USER/Downloads/poppins/Poppins-Medium.otf",10,ITALIC),borderwidth=15,relief="ridge")
text.grid(row=2,column=3)

l1 = Label(root,padx=100,pady=800,background="#33ccff")
l1.grid(row=1,column=2,rowspan=20)

photo = PhotoImage(file="C:\\Users\\USER\\Downloads\\speechnew3.png")
l_ima = Label(root,image=photo)
l_ima.grid(row=1,column=1,rowspan=6)


label_rate = Label(root,text="Speed",font=("ALGERIAN",30),foreground="red")
label_rate.grid(row=3,column=2)
rate = Spinbox(root,from_= 1,to=300,width=4,font=("ALGERIAN",30))
rate.grid(row=4,column=2) 

gender = Label(root,text="Voice",font=("ALGERIAN",30),foreground="red")
gender.grid(row=3,column=5)
list = ["male","female"]
genderbox = Combobox(root,width=10,font = ("ALGERIAN",20,ITALIC), foreground="red",background="black")
genderbox['values'] = list
genderbox.grid(row = 4,column = 5)
genderbox.set("gender")

def main():
    speed = int(rate.get())
    voice = str(genderbox.get())
    engine.setProperty("rate",speed)
    voice_id = engine.getProperty("voices")

    para = str(text.get(1.0,END))
    if voice == "male":
        engine.setProperty("voice",voice_id[0].id)
        
    if voice == "female":
        engine.setProperty("voice",voice_id[1].id)
    engine.say(para)
    # engine.save_to_file(para,"speech.mp3")
    engine.runAndWait()
    
def clear():
    text.delete(1.0,END)

Button_speech = Button(root,text="SPEECH",font = ("ALGERIAN",20,ITALIC),foreground="red",background="black",padx=20,command=main)
Button_speech.grid(row=3,column=3)

Button = Button(root,text="CLEAR",font = ("ALGERIAN",20,ITALIC),foreground="red",background="black",padx=20,command=clear)
Button.grid(row=4,column=3)

root.mainloop()