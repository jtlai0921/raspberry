from tkinter import *
import requests
import json
from gpiozero import LED
import threading
import datetime
import time

class App:
    led = LED(25);
    ledState = "";
    firebase_url = "https://raspberryfirebase.firebaseio.com/"
    
    def __init__(self,master):
        master.title("LED Control");
        master.option_add("*Font",("Verdana",18,"bold"));
        self.ledText = StringVar();
        f = Frame(master);
        xf = Frame(f,relief=GROOVE,borderwidth=2);
        titleLabel = Label(f,text="LED control").place(relx=0.05,rely=0.025,anchor=NW);
        button = Button(xf,textvariable=self.ledText,command=lambda:self.userClick()).pack(expand=YES,fill=BOTH,padx=50,pady=50);
        self.ledText.set("LED OPEN");
        xf.pack(fill=BOTH,expand=20, padx=20,pady=20);
        f.pack(fill=BOTH,expand=YES);
        self.getFirebaseData();
    
    def userClick(self):
       if self.led.is_lit == True:
           self.ledState = "CLOSE";
       else:
           self.ledState = "OPEN";

       t = time.time();
       date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S");
       data = {'date':date,'LED25':self.ledState};
       result = requests.put(self.firebase_url + "raspberrypi/LED_Control.json",data=json.dumps(data));
       print("status code =%s, Response=%s" % (str(result.status_code),result.text));
       

    def getFirebaseData(self):
        r = requests.get(self.firebase_url + "raspberrypi/LED_Control.json");
        if r.status_code == 200 :
            self.ledState = r.json()["LED25"];
            if self.ledState == "OPEN":
                self.led.on();
                self.ledText.set("LED CLOSE");
            elif self.ledState == "CLOSE":
                self.led.off();
                self.ledText.set("LED OPEN");
        threading.Timer(0.1,self.getFirebaseData).start();
                

root = Tk();
root.geometry("400x300");
display = App(root);
root.mainloop();
