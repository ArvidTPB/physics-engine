import tkinter
from math import pi, sin, cos, sqrt
from random import randint
from time import sleep

GRAVITY = 0.8
COF=0.8
COB = 0.75
WIDTH = 600
HEIGHT = 500
OBJECTS = 1

"""         def X(v, a, b, x):
            return (a*cos(v)-b*sin(v))+x

        def Y(v, a, b ,y):
            return (a*sin(v)+b*cos(v))+y
 """

def rotate(v, a, b, x, y):
    return a*cos(v)-b*sin(v)+x, a*sin(v)+b*cos(v)+y

class Box:
    def __init__(self, canvas, x, y, v, dim=(100, 100)):
        self.x=x
        self.y=y
        self.v=v
        self.dim=dim
        self.linewidth=5
        self.velx=0#-10
        self.vely=0
        self.velv=0#randint(-100, 100)/1000
        self.canvas = canvas
        self.offsets = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        self.id = self.canvas.create_polygon(0, 0, outline='white', width=self.linewidth)
        
    def move(self):
        self.vely += GRAVITY
        self.x += self.velx
        self.y += self.vely
        self.v += self.velv
        self.points = [rotate(self.v, ox * self.dim[0] / 2, oy * self.dim[1] / 2, self.x, self.y) for ox, oy in self.offsets]
        self.collision()
        self.canvas.coords(self.id, tuple(val for point in self.points for val in point))#self.id, self.x, self.y, self.x, self.y+100, self.x+100, self.y+100, self.x+100, self.y+0)
    
    def collision(self):
        points = [val for point in self.points for val in point]

        for point in points[::2]: #handles collision with x-values
            if point <= 0 or point + self.linewidth >= WIDTH:
                self.velx =- self.velx*COF
                self.x = max(self.x-min(x for x in points[::2])+self.linewidth, min(self.x-max(x for x in points[::2])+WIDTH-self.linewidth, self.x))
                self.velv += None

        for point in points[1::2]: #and conversely, handles collision for y-values
            if point <= 0 or point + self.linewidth >= HEIGHT:
                self.vely *= -COB
                self.velx *= COF
                self.y = max(min(self.y-max(y for y in points[1::2])+HEIGHT-self.linewidth, self.y), min(self.y-max(y for y in points[1::2])+HEIGHT-self.linewidth, self.y))
                

class Physics:
    def __init__(self, root):
        self.root=root
        self.canvas = tkinter.Canvas(self.root, background='black', width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.objects = [Box(self.canvas, WIDTH/2, HEIGHT-100*sqrt(2), v=pi/4, dim=(100, 100)) for i in range(OBJECTS)] #create an instance of a Box object for every simulated shape.
        self.speed=20
        self.update()

    def update(self):
        for obj in self.objects:
            obj.move()
        self.canvas.after(self.speed, self.update)

def main():
    root = tkinter.Tk()
    root.wm_geometry(f'{WIDTH}x{HEIGHT}+0+0')
    Physics(root)
    root.mainloop()

if __name__=='__main__':
    main()
