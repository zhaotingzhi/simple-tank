import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 3
        # 加载图片
        dList = ["U","R","D","L"]
        self.image = pygame.image.load("images\\missile%s.gif"%dList[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self,screen):
        if self.direction == 0:
            self.y -= self.speed
            if self.y < self.rect.height / 2:
                self.kill()
        if self.direction == 1:
            self.x += self.speed
            if self.x > 400 - self.rect.width / 2:
                self.kill()
        if self.direction == 2:
            self.y += self.speed
            if self.y > 300 - self.rect.height / 2:
                self.kill()
        if self.direction == 3:
            self.x -= self.speed
            if self.x < self.rect.width / 2:
                self.kill()
        self.rect.center = [self.x, self.y]
        self.draw(screen)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
