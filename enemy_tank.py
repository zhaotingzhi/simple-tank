from tank import Tank
from random import randint
class EnemyTank(Tank):
    def __init__(self,x,y):
        self.direction = self.get_random_direction()
        super().__init__(x,y,self.direction)
        self.speed = 4
        self.step = 6

    def get_random_direction(self):
        self.direction = randint(1,3)
        return self.direction

    def random_move(self):
        if self.step == 0:
            self.get_random_direction()
            self.step = 6
        else:
            self.move()
            self.step -= 1

    def move(self):
        if self.direction == 0:
            self.y -= self.speed
            if self.y < 0 - self.rect.height/2:
                self.kill()
        if self.direction == 1:
            self.x += self.speed
            if self.x > 400 + self.rect.width/2:
                self.kill()
        if self.direction == 2:
            self.y += self.speed
            if self.y > 300 + self.rect.height/2:
                self.kill()
        if self.direction == 3:
            self.x -= self.speed
            if self.x < 0 - self.rect.width/2:
                self.kill()