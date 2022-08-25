import math
import random
import time

import arcade 
from Bullet import Bullet
from Enemy import Enemy
from SpaceCraft import SpaceCraft
#=======================================================================================#

# کلاس بازی
class Game(arcade.Window):
    def __init__(self):
        self.w = 800          # x
        self.h = 600          # y
        super().__init__(width=self.w , height=self.h , title='Silver SpaceCraft') # سایز و عنوان
        arcade.set_background_color(arcade.color.BLACK) # ضمینه 
        self.background_image = arcade.load_texture(':resources:images/backgrounds/stars.png') # بک گراند
        self.spacecraft = SpaceCraft(self.w, self.h)    # صدا زدن سفینه
        self.enemy_list = []
        self.start_time = time.time()
        #-----------------------------#
        self.joon_image = arcade.load_texture('j.png')
        self.bullet_sound = arcade.load_sound(':resources:sounds/laser1.wav')    # صدای شلیک
        self.enemy_explosion = arcade.load_sound(':resources:sounds/explosion2.wav') # صدای انفجار

#======================================#
# ترسیم
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h, self.background_image)  # نمایش صفحه بازی
        self.spacecraft.draw()    # نمایش سفینه
        arcade.draw_text('score: '+str(self.spacecraft.score), 710 , 40 , arcade.color.WHITE, 12, font_name='arial')

        for i in range (self.spacecraft.joon):
            arcade.draw_lrwh_rectangle_textured((i*10)+ 40 + i*10 , 40, 20, 20 , self.joon_image)

        for i in range(len(self.spacecraft.bullet_list)):
            self.spacecraft.bullet_list[i].draw()   # نمایش گلوله 

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()    # نمایش دشمن

        if self.spacecraft.joon <= 0:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text('GAME OVER', 250, 300, arcade.color.RED, 50)
            arcade.exit()

#======================================#
# منطق بازی 
    def on_update(self, delta_time):   
        self.end_time = time.time()     #زمان 
        random_time = random.randint(2,6) # محدوده زمان 
        enemy = Enemy(self.w , self.h)
        if self.end_time - self.start_time > random_time : 
            self.enemy_list.append(enemy)  # اضافه کردن دشمن
            self.start_time = time.time()    # محدوده زمان وارد شدن دشمن

        self.spacecraft.rotate()      # چرخش سفینه


        for i in range(len(self.spacecraft.bullet_list)):
            self.spacecraft.bullet_list[i].move()     # حرکت گلوله 

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()   # حرکت دشمن
                        
        #-----------------------------# برخورد گلوله و دشمن
        for enemy in self.enemy_list:
                if enemy.center_y <= 0 :
                    self.enemy_list.remove(enemy)
                    self.spacecraft.joon -= 1
        
        for i in self.enemy_list :
                for j in self.spacecraft.bullet_list :
                    if arcade.check_for_collision(i , j):
                        arcade.play_sound(self.enemy_explosion)
                        self.enemy_list.remove(i)
                        self.spacecraft.bullet_list.remove(j)
                        self.spacecraft.score += 1      

#======================================#
# عملیات 
    def on_key_press(self, key , modifiers):
        if key == arcade.key.RIGHT:
            self.spacecraft.change_angle = -1
        elif key == arcade.key.LEFT:
            self.spacecraft.change_angle = 1
        elif key == arcade.key.SPACE:
            self.spacecraft.fire()
            #-----------------------------#
            arcade.play_sound(self.bullet_sound)

    def on_key_release(self, key, modifiers):
        self.spacecraft.change_angle = 0 
#=======================================================================================#
game = Game()
arcade.run()



