from turtle import *
import tkinter
state={'turn':0}
def spinner():
    clear()
    angle=state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'blue')

    back(100)
    right(120)
    forward(100)
    dot(120, 'red')

    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate,20)

def flip():
    state['turn']+=10
setup (420,420,370,0)
tracer(False)
width(20)
onkey(flip,'space')
listen()
animate()
done()
