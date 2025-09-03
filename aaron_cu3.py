

import turtle
import math
import random

# ---------- Configuration ----------
SCREEN_SIZE = 1000
CENTER = (0, 0)
BG_COLOR = "#FFF7FB"  
NUM_LAYERS = 10      
SEED = 42            
RANDOM = random.Random(SEED)

turtle.title("AaronPaul_2025_MEC")
screen = turtle.Screen()
screen.setup(SCREEN_SIZE + 50, SCREEN_SIZE + 50)
screen.bgcolor(BG_COLOR)
#screen.tracer(0, 0)  

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ---------- Utility functions ----------
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


turtle.colormode(255)

def set_fill_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    t.fillcolor((r, g, b))
    t.pencolor((r, g, b))

def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def circle_at(x, y, radius):
    goto(x, y - radius)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


PINK_PALETTE = [
    "#FFF0F6",  
    "#FFD6E8",  
    "#FFC1DB",  
    "#FF9ECF",  
    "#FF77B6", 
    "#FF4D9D",  
    "#FF1F7A",  
    "#E6006F", 
    "#C41B6B",  
    "#A01259",  
]


def pick_color(i, offset=0):
    return PINK_PALETTE[(i + offset) % len(PINK_PALETTE)]

# ---------- Basic Motifs ----------
def draw_petal(radius, width_factor=0.6):
    
    
    t.begin_fill()
    heading = t.heading()
    t.left(45)
    t.circle(radius * width_factor, 90)
    t.right(90)
    t.circle(radius * width_factor, 90)
    t.setheading(heading)
    t.end_fill()

def draw_ring_of_petals(ring_radius, petal_length, petal_count, color_index, rotation=0):
    
    angle_step = 360 / petal_count
    for i in range(petal_count):
        angle = rotation + i * angle_step
        
        x = ring_radius * math.cos(math.radians(angle))
        y = ring_radius * math.sin(math.radians(angle))
        goto(x, y)
        t.setheading(angle + 90)  # orient petal outward
        set_fill_color(pick_color(color_index + i, offset=2))
        t.pendown()
        draw_petal(petal_length, width_factor=0.7)
        t.penup()

def draw_lotus(center_x, center_y, outer_radius, layers=3):
    for layer in range(layers):
        petal_count = 8 + layer * 4
        ring_radius = outer_radius * (1 - layer * 0.25)
        petal_length = outer_radius * (0.35 - layer * 0.07)
        color = pick_color(layer + 3)
        set_fill_color(color)
        draw_ring_of_petals(ring_radius, petal_length, petal_count, color_index=layer*2, rotation=layer*10)
    # center circle
    set_fill_color(pick_color(7))
    goto(center_x, center_y)
    t.begin_fill()
    t.circle(outer_radius * 0.12)
    t.end_fill()

def draw_mango_leaf(x, y, heading, size, color):
    goto(x, y)
    t.setheading(heading)
    set_fill_color(color)
    t.begin_fill()
    t.forward(size * 0.2)
    t.left(40)
    t.circle(size * 0.6, 80)
    t.left(100)
    t.circle(size * 0.6, 80)
    t.left(40)
    t.forward(size * 0.2)
    t.end_fill()

def draw_vallam(x, y, heading, scale, color):
    goto(x, y)
    t.setheading(heading)
    set_fill_color(color)
    t.begin_fill()
    t.forward(scale * 1.2)
    t.left(25)
    t.circle(scale * 1.5, 40)
    t.right(65)
    t.forward(scale * 0.6)
    t.right(115)
    t.circle(scale * 1.8, 50)
    t.left(160)
    t.forward(scale * 0.6)
    t.end_fill()

def draw_nilavilakku(x, y, scale, color_lower, color_flame):
    # base
    goto(x, y)
    set_fill_color(color_lower)
    t.begin_fill()
    t.setheading(0)
    t.forward(scale * 0.5)
    t.left(90)
    t.circle(scale * 0.5, 90)
    t.left(90)
    t.forward(scale)
    t.left(90)
    t.circle(scale * 0.5, 90)
    t.left(90)
    t.forward(scale * 0.5)
    t.end_fill()
    # stem
    goto(x + scale * 0.5, y)
    t.setheading(90)
    t.pensize(2)
    set_fill_color(color_lower)
    t.pendown()
    t.forward(scale * 1.2)
    t.penup()
    t.pensize(1)
    # flame
    goto(x + scale * 0.5, y + scale * 1.2)
    set_fill_color(color_flame)
    t.begin_fill()
    t.circle(scale * 0.2, steps=30)
    t.end_fill()


def draw_pookalam():
    # central lotus
    draw_lotus(0, 0, outer_radius=80, layers=4)

    # inner decorative rings (tiny dots, stars)
    for i in range(4):
        r = 120 + i * 20
        dots = 18 + i * 6
        color_idx = (i + 4)
        for k in range(dots):
            angle = 360.0 * k / dots
            x = r * math.cos(math.radians(angle))
            y = r * math.sin(math.radians(angle))
            goto(x, y)
            set_fill_color(pick_color(color_idx + k, offset=1))
            t.begin_fill()
            t.circle(6 + i*2)
            t.end_fill()

    # mango-leaf
    toran_radius = 220
    leaf_count = 20
    for i in range(leaf_count):
        angle = 360 * i / leaf_count
        x = toran_radius * math.cos(math.radians(angle))
        y = toran_radius * math.sin(math.radians(angle))
        heading = angle + 90
        c = pick_color(3 + (i % len(PINK_PALETTE)))
        draw_mango_leaf(x, y, heading, size=60, color=c)

    # ring of boats
    boat_radius = 360
    boat_count = 12
    for i in range(boat_count):
        angle = 360 * i / boat_count
        x = boat_radius * math.cos(math.radians(angle))
        y = boat_radius * math.sin(math.radians(angle))
        heading = angle - 90
        color = pick_color(5 + (i % 4))
        draw_vallam(x, y, heading, scale=18, color=color)

    # outer petals
    outer_ring_radius = 470
    outer_petals = 48
    for i in range(outer_petals):
        angle = i * 360 / outer_petals
        x = outer_ring_radius * math.cos(math.radians(angle))
        y = outer_ring_radius * math.sin(math.radians(angle))
        goto(x, y)
        t.setheading(angle + 100)
        set_fill_color(pick_color(2 + (i % 6)))
        t.begin_fill()
        # draw elongated petals
        t.forward(40)
        t.left(30)
        t.forward(30)
        t.left(150)
        t.forward(40)
        t.end_fill()

    # decorative small circles
    for i in range(outer_petals * 2):
        angle = i * 360.0 / (outer_petals * 2)
        r = outer_ring_radius + 30 + (6 * math.sin(math.radians(i*10)))
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        goto(x, y)
        set_fill_color(pick_color(1 + (i % 5)))
        t.begin_fill()
        t.circle(6)
        t.end_fill()

    #lamps
    lamp_radius = 260
    lamp_positions = 6
    for i in range(lamp_positions):
        angle = i * 360 / lamp_positions - 90
        x = lamp_radius * math.cos(math.radians(angle))
        y = lamp_radius * math.sin(math.radians(angle))
        draw_nilavilakku(x - 30, y - 15, scale=20, color_lower=pick_color(6), color_flame=pick_color(4))



def draw_spiral_dots():
    # outward spiral of tiny dots (like rice/petal freckles)
    dots = 120
    for i in range(dots):
        angle = i * 20
        r = 10 + 3.8 * i
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        goto(x, y)
        set_fill_color(pick_color((i*3) % len(PINK_PALETTE)))
        t.begin_fill()
        t.circle(3)
        t.end_fill()



def build_pookalam_all():
    draw_pookalam()
    draw_spiral_dots()

# Run build
build_pookalam_all()

# Final update and hold
#screen.update()

# Keep window open until closed
#screen.update()
turtle.done()

