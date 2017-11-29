import pygame
from pygame.locals import *
import sys
from random import randint
from enemy_tank import EnemyTank
from my_tank import MyTank
from tank import *
from pygame.time import Clock
from pygame.sprite import Group
from bomb import Bomb


class Game(object):
    def __init__(self, width=400, height=300, bgColor=(0, 0, 0)):
        self.width = width
        self.height = height
        self.bgColor = bgColor
        self.enemyFireId = pygame.USEREVENT+1
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.myTank = MyTank(self.screen)

        self.bullets = Group()
        self.clock = Clock()
        self.enemys = Group()
        self.enemyBullets = Group()
        for i in range(1, 5):
            enemy = EnemyTank(75 * i, 30)
            self.enemys.add(enemy)
        self.bomb = Bomb()

        # 游戏结束的标志
        self.stop = False

        # 设置定时器
        pygame.time.set_timer(self.enemyFireId,800)

        # 游戏结束显示的文字
        myFont = pygame.font.SysFont("simhei", 24)
        self.fontImage = myFont.render("游戏结束！", True, (0, 255, 0))

    # 事件处理
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
                # 开始游戏
            elif event.type == self.enemyFireId:
                for enemy in self.enemys:
                    self.enemyBullets.add(enemy.fire())
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    self.myTank.setDirection(-1)
                elif event.key == K_d or event.key == K_RIGHT:
                    self.myTank.setDirection(1)
                elif event.key == K_w or event.key == K_UP:
                    self.myTank.move()
                elif event.key == K_SPACE:
                    self.bullets.add(self.myTank.fire())

    def run(self):
        while True:
            self.clock.tick(15)
            self.handleEvent()
            self.screen.fill(self.bgColor)
            if not self.stop:
                self.myTank.update(self.screen)
                if len(self.enemys.sprites()) < 4:
                    enemy = EnemyTank(80 * randint(1,4), 30)
                    self.enemys.add(enemy)

                self.enemys.update(self.screen)
                for enemy in self.enemys:
                    enemy.random_move()
                self.enemyBullets.update(self.screen)
                self.enemyBullets.update(self.screen)
                self.bullets.update(self.screen)
                # self.bomb.update(self.screen,30,30)
                pygame.sprite.groupcollide(self.bullets, self.enemyBullets, True, True)
                collisions = pygame.sprite.groupcollide(self.bullets, self.enemys, True, True)
                for bullet in collisions.keys():
                    bomb_rect = bullet.rect
                    self.bomb.update(self.screen,bomb_rect.x,bomb_rect.y)
                if pygame.sprite.spritecollideany(self.myTank,self.enemyBullets):
                    self.bomb.update(self.screen, self.myTank.rect.x, self.myTank.rect.y)
                    self.myTank.kill()
                    self.enemys.empty()
                    self.enemyBullets.empty()
                    self.bullets.empty()
                    self.stop = True
                if pygame.sprite.spritecollideany(self.myTank, self.enemys):
                    self.bomb.update(self.screen, self.myTank.rect.x, self.myTank.rect.y)
                    self.myTank.kill()
                    self.enemys.empty()
                    self.enemyBullets.empty()
                    self.bullets.empty()
                    self.stop = True

            else:
                self.screen.blit(self.fontImage,(self.screen.get_rect().centerx
                                 -self.fontImage.get_rect().centerx,self.screen.get_rect().centery
                                 -self.fontImage.get_rect().centery))
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
