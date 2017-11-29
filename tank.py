import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class Tank(Sprite):
    def __init__(self, x, y, direction):  # dirction  0：D 1:U 2:L 3:R
        super().__init__()
        self.direction = direction
        self.x = x
        self.y = y
        self.speed = 10
        self.ff = False
        # 初始化图片
        self.images = []
        dList = ["U", "R", "D", "L"]
        count = 0
        for d in dList:
            img = pygame.image.load("images\\tank%s.gif" % d)
            self.images.append(img)
        self.image = self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def setDirection(self,offset): # -1 逆时针 1 顺时针
        self.direction += offset
        if self.direction<0:
            self.direction = 3
        elif self.direction >3:
            self.direction = 0

    def move(self):
        if self.direction == 0:
            self.y -= self.speed
            if self.y < self.rect.height/2:
                self.y = self.rect.height/2
        if self.direction == 1:
            self.x += self.speed
            if self.x > 400 - self.rect.width/2:
                self.x = 400 - self.rect.width/2
        if self.direction == 2:
            self.y += self.speed
            if self.y > 300 - self.rect.height/2:
                self.y = 300 - self.rect.height/2
        if self.direction == 3:
            self.x -= self.speed
            if self.x < self.rect.width/2:
                self.x = self.rect.width/2

    def update(self, screen):
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.center = [self.x,self.y]
        self.draw(screen)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def fire(self):
        if self.direction == 0:
            return Bullet(self.rect.left+ self.rect.width / 2, self.rect.top, self.direction)
        elif self.direction == 1:
            return Bullet(self.rect.right ,self.rect.top + self.rect.height / 2, self.direction)
        elif self.direction == 2:
            return Bullet(self.rect.left+ self.rect.width / 2, self.rect.bottom, self.direction)
        elif self.direction == 3:
            return Bullet(self.rect.left, self.rect.top +self.rect.height / 2, self.direction)
