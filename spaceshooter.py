"""
spaceshooter.py
Author: James Eiler
Credit: Source code Example, Teachers
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
b=0
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame
import math, random
from time import time
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        for i in range (1,10):
            white=Color(0xbbbb00,1)
            starline=LineStyle(2,white)
            star_asset =RectangleAsset(10, 10, starline, white)
            star = Sprite(star_asset, ((random.randint(0,1000)),(random.randint(0,500))))
        self.spaceship=SpaceShip((100,100))
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(400,800),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        asteroid((random.randint(0,400),random.randint(0,200)), self.spaceship)
        
            

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(asteroid):
            ship.step()
        for ship in self.getSpritesbyClass(bullet):
            ship.step()
        for ship in self.getSpritesbyClass(ExplosionSmall):
            ship.step()
            

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, (400,400))
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotationlefton)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.rotationleftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotationrighton)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rotationrightoff)
        SpaceGame.listenKeyEvent("keydown", "space",self.shooton)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.y += self.vy
        """
        if self.thrust == 1 and self.rotation ==0 :
            self.x += 0
            self.y += -1
        if self.thrust == 1 and self.rotation == 1:
            self.x += -1
            self.y += -1
        if self.thrust == 1 and self.rotation ==-1:
            self.x += 1
            self.y += -1
        if self.thrust == 1 and self.rotation ==-2:
            self.x += 1
            self.y += 1
        if self.thrust == 1 and self.rotation ==2:
            self.x += -1
            self.y += 1
            """
        if self.thrust == 1:
            self.x += -2*(math.sin(self.rotation))
            self.y += -2*(math.cos(self.rotation))
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        if self.collidingWithSprites(asteroid) and self.visible==True:
            self.visible=False
            ExplosionSmall(self.position)
            print('you lose')
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def rotationleftoff(self, event):
        if self.rotation==0:
            self.rotation = 0
            b=0
        elif self.rotation==1:
            self.rotation = 1
            b=1
    
    def rotationlefton(self,event):
        self.rotation = self.rotation+1
        b= 1
    def rotationrightoff(self,event):
        if self.rotation==0:
            self.rotation = 0
            b=0
        elif self.rotation==1:
            self.rotation = 1
            b=1
    def rotationrighton(self,event):
        self.rotation = self.rotation-1
        k=1
    def shooton(self,event):
        print("Bang")
        bullet((self.x,self.y),self)
print(b)
class bullet(Sprite):
    grey=Color(0xbebebe,1)
    bulletline=LineStyle(2,grey)
    bullet_asset =RectangleAsset(4, 4, bulletline, grey)
    def __init__(self, position, spaceship):
        super().__init__(bullet.bullet_asset, position)
        self.vx = 0
        self.vy = 0
        self.thrust = 2
        self.spaceship=spaceship
    def step(self):
        self.x += 1
        self.y += 1
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.thrust = 1
        if self.thrust == 1:
            self.x += -4*(math.sin(self.spaceship.rotation))
            self.y += -4*(math.cos(self.spaceship.rotation))
        self.visible=True
class asteroid(Sprite):
    grey=Color(0xbebebe,1)
    asteroidline=LineStyle(2,grey)
    asteroid_asset =RectangleAsset(30, 30, asteroidline, grey)
    def __init__(self, position, spaceship):
        super().__init__(asteroid.asteroid_asset, position)
        self.vx = 0
        self.vy = 0
        self.thrust=1
        self.spaceship=spaceship
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.thrust == 1 and self.visible==True:
            self.x += 0
            self.y += 1
            if self.y>600:
                print("you lose")
        if self.visible==False:
            pass
        if self.collidingWithSprites(bullet) and self.visible==True:
            self.visible=False
            ExplosionSmall(self.position)
            self.destroy()
            print("good job")

class ExplosionSmall(Sprite):
    ExplosionSmall_asset = ImageAsset("images/explosion1.png", 
    Frame(0,0,128,128), 10)
    def __init__(self, position):
        super().__init__(ExplosionSmall.ExplosionSmall_asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.image=0
    def step(self):    
        self.setImage(self.image)
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()
        



myapp = SpaceGame()
myapp.run()


