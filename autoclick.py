import ctypes
from ctypes import windll,Structure, c_ulong, byref
import time
import datetime
import sys
import tkinter as tk
#from tkinter import *
from functools import partial

numclicks = 0



class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.sv = tk.StringVar()

        self.label = tk.StringVar()
        self.label.set("Enter number below and click button")

        w = tk.Label(self, textvariable=self.label)
        w.pack()

        e = tk.Entry(self, textvariable=self.sv)
        e.pack()
        e.insert(0,numclicks)
        button = tk.Button(self, text="GO", command=self.goclick, height=10, width=50)
        button.pack()
        
    def goclick(self):

        global numclicks
        numclicks=int(self.sv.get())*40
        print("goclick",numclicks)

        for x in range(-3,0):
            print(x)
            self.label.set(x)
            self.update()
            time.sleep(1)

        a = datetime.datetime.now()

        pos = queryMousePosition()

        for x in range(0,numclicks):
            if pos != queryMousePosition():break

            self.label.set("click "+str(x+1)+"/"+str(numclicks)+" ("+str(round(((x+1)/numclicks)*100,1))+"%)")
            self.update()
            click()

        b = datetime.datetime.now()
        print(b-a)
        self.label.set("stopped after "+str(b-a))
        self.update()


def click():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left upctypes.windll.user32.SetCursorPos(100, 20)
    time.sleep(0.025)



class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x":pt.x, "y":pt.y }


def main(args):

    duration = 30

    if len(args) > 1:
        duration = int(args[1])

    global numclicks
    numclicks = duration*40

    print("run for",duration,"seconds, i.e.",numclicks,"clicks")

    root = tk.Tk()
    root.wm_title("Autoclicker")
    MainWindow(root).pack()

    root.mainloop()
       




if __name__ == "__main__":
    main(sys.argv)
