import pygame, sys, pyganim
from pygame.locals import *
from const import *



# Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        #initiate run animation
        self.runAnim = pyganim.PygAnimation([('playerSprites/run/run_1.png', 100),
                                        ('playerSprites/run/run_2.png', 100),
                                        ('playerSprites/run/run_3.png', 100),
                                        ('playerSprites/run/run_4.png', 100),
                                        ('playerSprites/run/run_5.png', 100),
                                        ('playerSprites/run/run_6.png', 100),
                                        ('playerSprites/run/run_7.png', 100),
                                        ('playerSprites/run/run_8.png', 100),
                                        ('playerSprites/run/run_9.png', 100),
                                        ('playerSprites/run/run_10.png', 100)]) 
        self.runAnim.play()

        #initiate running left
        self.runLeft = self.runAnim.getCopy()
        self.runLeft.flip(True, False)
        self.runLeft.play()

        #initiate idle animation
        self.idleAnim = pyganim.PygAnimation([('playerSprites/idle/idle_1.png', 100),
                                         ('playerSprites/idle/idle_2.png', 100),
                                         ('playerSprites/idle/idle_3.png', 100),
                                         ('playerSprites/idle/idle_4.png', 100)])
        self.idleAnim.play()

        #left
        self.idleLeft = self.idleAnim.getCopy()
        self.idleLeft.flip(True, False)
        self.idleLeft.play()

        #initiate jump
        self.jumpAnim = pyganim.PygAnimation([('playerSprites/jump/jump_1.png', 10), ('playerSprites/jump/jump_3.png', 5000)])

        #left
        self.jumpLeft = self.jumpAnim.getCopy()
        self.jumpLeft.flip(True, False)
        self.jumpLeft.play()

        #initiate fall
        self.fallAnim = pyganim.PygAnimation([('playerSprites/jump/jump_4.png', 100)])
        self.fallAnim.play()

        #left
        self.fallLeft = self.fallAnim.getCopy()
        self.fallLeft.flip(True, False)
        self.fallLeft.play()

        #mass
        self.m = 2

        #velocity
        self.xvelocity = 10
        self.yvelocity = jumpPower

        #position
        self.x = 0
        self.y = ground

        #states
        self.jumping = False
        self.falling = False
        self.facingLeft = False

        self.image = self.idleAnim

    def update(self, str):
        if self.jumping:
            # F = ma
            F = self.m * self.yvelocity
            self.y -= F

            self.yvelocity -= gravity

            # 'falling' occurs at the apex of the jump
            if self.yvelocity <= 0:
                self.falling = True

            # once the ground is reached, reset variables
            if self.y >= ground:
                self.y = ground
                self.yvelocity = jumpPower
                self.jumping = False
                self.falling = False

        # change animations accordingingly
        if str == 'jump':
            self.jumpAnim.play()
            if self.facingLeft:
                self.image = self.jumpLeft
            else:
                self.image = self.jumpAnim
        
        if self.falling:
            if self.facingLeft:
                self.image = self.fallLeft
            else:
                self.image = self.fallAnim

        if str == 'right':
            self.x += self.xvelocity
            self.facingLeft = False
            if not self.falling and not self.jumping: # making sure not to override the jump/fall animation
                self.image = self.runAnim

        elif str == 'left':
            self.x -= self.xvelocity
            self.facingLeft = True
            if not self.falling and not self.jumping:
                self.image = self.runLeft
        
        elif str == 'idle':
            if not self.falling and not self.jumping:
                if self.facingLeft:
                    self.image = self.idleLeft
                else:
                    self.image = self.idleAnim
        