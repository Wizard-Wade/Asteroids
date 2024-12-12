import pygame
from constants import *
from player import Player

class asteroids_game():
    def __init__(self):
        print("Starting asteroids!")
        pygame.init()
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        Player.containers = (self.updatable, self.drawable)
        self.__fps = game_clock()
        
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.gameloop()
    
    def gameloop(self):
        while(True):
            if self.window_close(): return
            self.__screen.fill(pygame.Color(0,0,0))
            
            for obj in self.updatable:
                obj.update(self.__fps.dt)
            
            for obj in self.drawable:
                obj.draw(self.__screen)
            
            pygame.display.flip()
            self.__fps.addframe()
            
    def window_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

class game_clock():
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.dt = 0
    
    def addframe(self):
        self.dt = self.__clock.tick(60)/1000

def main():
    asteroids_game()
    print("closing Asteroids")

if __name__ == "__main__":
    main()