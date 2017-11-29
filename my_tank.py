from tank import Tank

class MyTank(Tank):
    def __init__(self,screen,direction = 0):
        self.screen_rect = screen.get_rect()
        super().__init__(self.screen_rect.centerx,self.screen_rect.bottom-30,direction)