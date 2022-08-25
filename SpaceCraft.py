import arcade

from Bullet import Bullet

# سفینه
class SpaceCraft(arcade.Sprite):
    def __init__(self, w , h):
        super().__init__(':resources:images/space_shooter/playerShip1_green.png')
        self.width = 48
        self.height = 48
        self.center_x = w // 2
        self.center_y = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 10
        self.joon = 3
        self.score = 0

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))