import pygame
from constants import *

class asteroids_game():
    def __init__(self):
        print("Starting asteroids!")
        pygame.init()
        self.__fps = game_clock()
        
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameloop()
    
    def gameloop(self):
        while(True):
            if self.window_close(): return
            self.__screen.fill(pygame.Color(0,0,0))
            
            pygame.display.flip()
            self.__fps.addframe()
            
    def window_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

class game_clock():
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__dt = 0
    
    def addframe(self):
        self.__dt = self.__clock.tick(60)/1000

def main():
    asteroids_game()
    print("closing Asteroids")

if __name__ == "__main__":
    main()