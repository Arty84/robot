#import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import *
#import picamera

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#Constroling Robor movements:
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
#output for camera UP and DOWN:
#GPIO.setup(12, GPIO.OUT)
#Output for camera LEFT and RIGHT:
#GPIO.setup(16, GPIO.OUT)

#camera = picamera.PiCamera()

#making buttons for camera movement control
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid(row=2, column=4,rowspan=3)
        self.bttn_up_down = 0.0015
        self.bttn_left_right=0.0015
        self.create_widget()

    def create_widget(self):
        self.bttnu = Button(self, width=9)
        self.bttnu['text'] = "Upwards"
        self.bttnu['command'] = self.update_up
        self.bttnu.grid(row=0, column=1)
        self.bttnd = Button(self, width=9)
        self.bttnd['text'] = "Downward"
        self.bttnd['command'] = self.update_down
        self.bttnd.grid(row=2, column=1)
        self.bttnl = Button(self, width=9)
        self.bttnl['text'] = "Left"
        self.bttnl['command'] = self.update_left
        self.bttnl.grid(row=1, column=0)
        self.bttnr = Button(self, width=9)
        self.bttnr['text'] = "Right"
        self.bttnr['command'] = self.update_right
        self.bttnr.grid(row=1, column=2)
        self.bttnrs = Button(self, width=9)
        self.bttnrs['text'] = "Reset"
        self.bttnrs['command'] = self.update_reset
        self.bttnrs.grid(row=1, column=1)
                
    def update_up(self):
        if self.bttn_up_down>0.0007:
            self.bttn_up_down -= 0.00005
        else:
            self.bttn_up_down=0.0007
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(12, True)
            time.sleep(self.bttn_up_down)
            GPIO.output(12, False)
            time.sleep(0.015)
        GPIO.output(12, False)
        print(self.bttn_up_down)
                
    def update_down(self):
        if self.bttn_up_down<0.002:
            self.bttn_up_down += 0.00005
        else:
            self.bttn_up_down=0.002
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(12, True)
            time.sleep(self.bttn_up_down)
            GPIO.output(12, False)
            time.sleep(0.015)
        GPIO.output(12, False)
        print(self.bttn_up_down)

    def update_left(self):
        if self.bttn_left_right<0.0024:
            self.bttn_left_right += 0.00005
        else:
            self.bttn_left_right=0.0024
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(16, True)
            time.sleep(self.bttn_left_right)
            GPIO.output(16, False)
            time.sleep(0.015)
        GPIO.output(16, False)
        print(self.bttn_left_right)
        
    def update_right(self):
        if self.bttn_left_right>0.0008:
            self.bttn_left_right -= 0.00005
        else:
            self.bttn_left_right=0.0008
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(16, True)
            time.sleep(self.bttn_left_right)
            GPIO.output(16, False)
            time.sleep(0.015)
        GPIO.output(16, False)
        print(self.bttn_left_right)
    def update_reset(self):
        self.bttn_up_down = 0.0015
        self.bttn_left_right=0.0015
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(12, True)
            time.sleep(self.bttn_up_down)
            GPIO.output(12, False)
            time.sleep(0.015)
        GPIO.output(12, False)
        cycles=5
        while cycles>0:
            cycles = cycles - 1
            GPIO.output(16, True)
            time.sleep(self.bttn_left_right)
            GPIO.output(16, False)
            time.sleep(0.015)
        GPIO.output(16, False)
        print("camera in the center")
        

class Power(Frame):

    def __init__(self, master):
        super(Power, self).__init__(master)
        self.grid(row=6, column=0, columnspan = 4, rowspan=2)
        self.main_power="green2"
        self.battery_power="dark green"
        self.position="main power"
        self.test="not tested"
        self.create_widget()

    def create_widget(self):

        self.bttntest = Button(self, width=9)
        self.bttntest['text'] = "checking"
        self.bttntest['command'] = self.checking
        self.bttntest.grid(row=0, column=0, rowspan=2)
        
        self.bttnchange = Button(self, width=9)
        self.bttnchange['text'] = "change"
        self.bttnchange['command'] = self.change
        self.bttnchange.grid(row=0, column=1, rowspan=2)
        
        self.sw1status= Canvas(self, height=30, width=30)
        self.sw1status.create_oval(2, 2, 28, 28, fill=self.main_power)
        self.sw1status.grid(row=0, column=2)
        self.sw2status= Canvas(self, height=30, width=30)
        self.sw2status.create_oval(2, 2, 28, 28, fill=self.battery_power)
        self.sw2status.grid(row=1, column=2)
        self.mains_power_label=Label(self, text = "Mains power", width="12", height="1")
        self.mains_power_label.grid(row=0, column=3)
        self.battery_power_label=Label(self, text = "Battery power", width="12", height="1")
        self.battery_power_label.grid(row=1, column=3)
#extra window for warning to check mains power supplay
    def testing(self):
        window = tk.Toplevel(my_window)
        window.title("warning")
        window.geometry("220x80")
        tk.Label(window, text="Check mains power supplay!!! \n press button checking").grid(row=0, column=0)
        tk.Button(window, text="ok", command=window.destroy).grid(row=1, column=0)
    def checking(self):
        self.test="tested"
        print("sw1 connected should see LED trough camera")
        time.sleep(2)
        print("sw1 disconnected on LED")
        print("You checked main power supplay trough cammera")
#function for changing power supplays        
    def change(self):
        if self.main_power=="green2" and self.battery_power=="dark green":
            self.battery_power="green2"
            self.position="to battery"
            self.test="not tested"
            print("bouth power supplays connected")

        elif self.main_power=="green2" and self.battery_power=="green2":
            if self.position=="to battery":
                self.main_power="dark green"
                print("only battery connected")
            else:
                self.battery_power="dark green"
                print("Only main power suppplay connected")
        elif self.main_power=="dark green" and self.battery_power=="green2":
            if self.test=="not tested":
                self.testing()
                print("warning, you need to check that main power supplay connected")
            else:
                self.main_power="green2"
                self.position="to mains power"
                print("bouth power supplays connected")
        else:
            print("else")
        self.create_widget() 



my_window = Tk()

#Creating maing window
my_window.geometry("650x280")
my_window.title("Kontroling robot")

app = Application(my_window)
powe = Power(my_window)

description=Label(my_window, text = "Kontroling robot", width="30", height="2")
description.grid(row=0, column=0,columnspan=6)
robot_movement=Label(my_window, text = "Kontroling robot movement", width="30", height="2")
robot_movement.grid(row=1, column=0,columnspan=3)

camera_movement=Label(my_window, text = "Kontroling camera movement", width="30", height="2")
camera_movement.grid(row=1, column=3,columnspan=3)

controling_camera=Label(my_window, text = "Kontroling camera", width="30", height="2")
controling_camera.grid(row=5, column=3,columnspan=3)

controling_power=Label(my_window, text = "Kontroling power", width="30", height="2")
controling_power.grid(row=5, column=0,columnspan=3)

#functions for robot movements
def hello_forward(event):
    print("Robot moving forward")
    GPIO.output(18, True)
    GPIO.output(23, False)
    GPIO.output(13, True)
    GPIO.output(22, False)
def quit_forward(event):                           
    print("Robot stoped moving forwards")
    GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(13, False)
    GPIO.output(22, False)
   
def hello_backward(event):
    print("Robot moving backward")
    GPIO.output(18, False)
    GPIO.output(23, True)
    GPIO.output(13, False)
    GPIO.output(22, True)
def quit_backward(event):                           
    print("Robot stoped moving backwards")
    GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(13, False)
    GPIO.output(22, False)
    
def hello_left(event):
    print("Robot moving left")
    GPIO.output(18, False)
    GPIO.output(23, True)
    GPIO.output(13, True)
    GPIO.output(22, False)
def quit_left(event):                           
    print("Robot stoped moving left")
    GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(13, False)
    GPIO.output(22, False)
   
def hello_right(event):
    print("Robot moving right")
    GPIO.output(18, True)
    GPIO.output(23, False)
    GPIO.output(13, False)
    GPIO.output(22, True)
    
def quit_right(event):                           
    print("Robot stoped moving right")
    GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(13, False)
    GPIO.output(22, False)

#functions for camera on and off buttons
def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(90,100, 320, 240)
    camera.resolution=(640,480)
    camera.rotation=180
    camera.start_preview()

def CameraOFF():
    camera.stop_preview()

#creating buttons for robot muvements
mooving_forward = Button(my_window, text='Forward', width=9)
mooving_forward.grid(row=2, column=1)
mooving_forward.bind('<Button-1>', hello_forward)
mooving_forward.bind('<ButtonRelease-1>', quit_forward)

mooving_backward = Button(my_window, text='Backwards', width=9)
mooving_backward.grid(row=4, column=1)
mooving_backward.bind('<Button-1>', hello_backward)
mooving_backward.bind('<ButtonRelease-1>', quit_backward)

mooving_left = Button(my_window, text='Left', width=9)
mooving_left.grid(row=3, column=0)
mooving_left.bind('<Button-1>', hello_left)
mooving_left.bind('<ButtonRelease-1>', quit_left)

mooving_right = Button(my_window, text='Right', width=9)
mooving_right.grid(row=3, column=2)
mooving_right.bind('<Button-1>', hello_right)
mooving_right.bind('<ButtonRelease-1>', quit_right)

#buttons for camera on an off
Camera_ON = Button(my_window, command=CameraON, text='Turn on Camera', width=15)
Camera_ON.grid(row=6, column=3, columnspan=3)

Camera_OFF = Button(my_window, command=CameraOFF, text='Turn off Camera', width=15)
Camera_OFF.grid(row=7, column=3, columnspan=3)

my_window.mainloop()
