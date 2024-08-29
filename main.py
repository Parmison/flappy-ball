import pgzrun

WIDTH = 600
HEIGHT = 400

titlebox = Rect((0,0),(600,80))
a = 2000

class Circle:
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 200
        self.vy = 0
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)

ball1 = Circle(300,200,50,"coral")
ball2 = Circle(300,200,30,"purple")


def draw():
    screen.fill("black")
    ball1.draw()
    ball2.draw()
    screen.draw.filled_rect(titlebox,"black")
    title = "ball bounce!"
    screen.draw.textbox(title,titlebox,color = "white")


def update(dt):
    titlebox.x -= 2
    if titlebox.right<0:
        titlebox.left = WIDTH
    #v = u + at
    uy = ball1.vy
    uy = ball2.vy

    ball1.vy += a*dt
    ball2.vy += a*dt

    #s = ((u+v)/2)*t

    ball1.y +=(uy + ball1.vy)*0.5*dt
    ball2.y +=(uy + ball2.vy)*0.5*dt

    #velocity in x direction
    
    ball1.x += ball1.vx * dt
    ball2.x += ball1.vx * dt

    #detect touch with boundry

    if ball1.y >= HEIGHT-50:
        ball1.y = HEIGHT-50
        ball1.vy =- ball1.vy * 0.9
    if ball1.x >= WIDTH-50:
        ball1.vx =- ball1.vx
    if ball1.x <= 50:
        ball1.vx =- ball1.vx

    if ball2.y >= HEIGHT-50:
        ball2.y = HEIGHT-50
        ball2.vy =- ball2.vy * 0.7
    if ball2.x >= WIDTH-50:
        ball2.vx =- ball2.vx
    if ball2.x <= 50:
        ball2.vx =- ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -800
        ball2.vy = -600

 

pgzrun.go()