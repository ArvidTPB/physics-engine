import tkinter
import math
from random import *

GRAVITY = 0
WIDTH = 100
HEIGHT = 100
OBJECTS = 0

class box:
    def __init__(self, x, y, velx=0, vely=0, dim=(0,0,100,100)):
        self.x=x
        self.y=y
        self.velx=velx
        self.vely=vely
        self.dim=dim
    def create(self):
        return
    def move(self):
        self.vely+=GRAVITY
        self.x+=self.velx
        self.y+=self.vely

class physics:
    def __init__(self, WIDTH=500, HEIGHT=500):
        self.root=tkinter.Canvas()
        objects = box.create()
    def update(self):
        for object in :

            self.root.after(50, )
