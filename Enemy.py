import random
import arcade


# دشمن
class Enemy(arcade.Sprite):
    def __init__(self, w , h):
        super().__init__(':resources:images/space_shooter/playerShip2_orange.png')
        self.speed = 4
        self.center_x = random.randint(0,w)
        self.center_y = h
        self.angle = 180
        self.width = 48
        self.height = 48

    def move(self):
        self.center_y -= self.speed
