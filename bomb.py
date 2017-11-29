import pygame
from pygame.sprite import Sprite
class Bomb(Sprite):
    def __init__(self):
        super().__init__()
        self.order = 0
        # 加载爆炸效果所需的图片
        self.imgs = []
        for i in range(0, 11):
            img = pygame.image.load("images\\%s.gif" % i)
            self.imgs.append(img)
        self.image = self.imgs[self.order]
        self.rect = self.image.get_rect()

    def update(self,screen,x,y):
        if self.order >= 10:
            self.order = -1
        self.order += 1
        self.image = self.imgs[self.order]
        self.draw(screen,x,y)

    def draw(self,screen,x,y):
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        screen.blit(self.image,self.rect)