import RPi.GPIO as gpio
from tkinter import *

from board import SCL, SDA
import busio
import time

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo


i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)
pca.frequency = 50


control_pins1 = [7,11,16,18]
control_pins2 = [18,16,11,7]

for pin in control_pins1:
    gpio.setup(pin,gpio.OUT)

sequence1 = [
[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1],
[1,0,0,1]
]

sequence2 = [
[1,0,0,1],
[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1]
]


class EezyBotArm():

    def __init__(self,master):
        self.label = Label(master,text = "Servo Sliders")
        self.label.grid(row = 1,column = 3,columnspan = 4,pady = 5)
        self.label1 = Label(master,text = "Step Buttons")
        self.label1.grid(row = 3,column = 3,columnspan = 4,pady =10)
        self.label2 = Label(master,text = "CCW")
        self.label2.grid(row = 4,column = 2,pady =10)
        self.label3 = Label(master,text = "CW")
        self.label3.grid(row = 5,column = 2,pady =10)
        self.slider = Scale(master,from_ = 0 ,to = 180,command = self.update1)
        self.slider.grid(column =2,row = 2)
        self.slider1 = Scale(master,from_ = 0 ,to = 180,command = self.update2)
        self.slider1.grid(column =3,row = 2)
        self.slider2 = Scale(master,from_ = 0 ,to = 180,command = self.update3)
        self.slider2.grid(column =4,row = 2)
        self.slider2 = Scale(master,from_ = 0 ,to = 180,command = self.update2)
        self.slider2.grid(column =5,row = 2)
        self.button = Button(master,text = "1",command = self.ClockWise)
        self.button.grid(row = 4,column = 3,pady = 5,padx = 20)
        self.button1 = Button(master,text = "3")
        self.button1.grid(row = 4,column = 5,pady = 5,padx = 20)
        self.button2 = Button(master,text = "2")
        self.button2.grid(row = 4,column = 4,pady = 5,padx = 20)
        self.button3 = Button(master,text = "1",command = self.CounterClockWise)
        self.button3.grid(row = 5,column = 3,pady = 5,padx = 20)
        self.button4 = Button(master,text = "3")
        self.button4.grid(row = 5,column = 5,pady = 5,padx = 20)
        self.button5 = Button(master,text = "2")
        self.button5.grid(row = 5,column = 4,pady = 5,padx = 20)
        
    def update1(self,ang):
        servos = servo.Servo(pca.channels[0],min_pulse=580, max_pulse=2480)
        servos.angle = int(ang)
        
    def update2(self,ang):
        servos = servo.Servo(pca.channels[1],min_pulse=580, max_pulse=2480)
        servos.angle = int(ang) 
    
    def update3(self,ang):
        
        servos = servo.Servo(pca.channels[2],min_pulse=580, max_pulse=2480)
        servos.angle = int(ang)
    
        
    def CounterClockWise(self):
        for i in range(512):
            for seq2 in sequence2:
                for pin2 in range(4):
                    gpio.output(control_pins2[pin2],seq2[pin2])
                time.sleep(0.001)
        
    def ClockWise(self):
        for i in range(512):
            for seq1 in sequence1:
                for pin1 in range(4):
                    gpio.output(control_pins1[pin1],seq1[pin1])
                time.sleep(0.001)


root = Tk()
app = EezyBotArm(root)
root.geometry("290x270+0+0")
