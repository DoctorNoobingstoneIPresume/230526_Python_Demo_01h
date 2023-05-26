from tkinter import *
import time
import random

print ('Hello, World !\n')
sys.stdout.flush ()

tk = Tk ()
tk.title ('Demo 1')
tk.geometry ('400x400')
#tk.state ('zoomed')

canvas = Canvas (tk, width = 400, height = 400, background = 'white')
canvas.pack (fill = 'both', expand = True)

images = [
	PhotoImage (file = 'Graphics/Sphere_Magenta_03h_t.png'),
	PhotoImage (file = 'Graphics/Sphere_Blue_03h_t.png'   ),
	PhotoImage (file = 'Graphics/Sphere_Green_03h_t.png'  )
]

image = images [1]

class Thing:
	def __init__ (self, x, y, vx, vy):
		self.x  = x
		self.y  = y
		self.vx = vx
		self.vy = vy
		self.ax = 0
		self.ay = -1/4
		
		self.id = -1
		self.image = random.choice (images)

dt_update = 10

thing = Thing (0, 0, 1/4, 1/4)

things = []
n_things = 10
for i in range (n_things):
	things.append (
		Thing (
			x  = i * 2 / n_things - 1,
			y  = -1,
			vx = (random.random () * 2 - 1) * 1/8,
			vy = (random.random () + 3) * 1/4
		)
	)

t0 = time.monotonic ()

def convert_x (x):
	sx = canvas.winfo_width ()
	return (  x + 1) * sx / 2 - image.width  () / 2

def convert_y (y):
	sy = canvas.winfo_height ()
	return (- y + 1) * sy / 2 - image.height () / 2

def update_partially (thing, dt):
	thing.x += thing.vx * dt + thing.ax * dt * dt
	thing.y += thing.vy * dt + thing.ay * dt * dt
	
	thing.vx += thing.ax * dt
	thing.vy += thing.ay * dt
	
	if thing.x <= -1 and thing.vx < 0 or thing.x >= +1 and thing.vx > 0:
		thing.vx = - thing.vx
	
	if thing.y <= -1 and thing.vy < 0: # or thing.y >= +1 and thing.vy > 0:
		thing.vy = - thing.vy
	
	if thing.id >= 0:
		canvas.delete (thing.id)
	
	global images
	thing.id = canvas.create_image (convert_x (thing.x), convert_y (thing.y), anchor = NW, image = thing.image)

def update ():
	global thing, t0
	t1 = time.monotonic ()
	dt = t1 - t0
	
	for thing in things:
		update_partially (thing, dt)
	
	t0 = t1
	tk.after (dt_update, update)

tk.after (dt_update, update)
tk.mainloop ()
