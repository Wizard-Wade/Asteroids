import pygame
from constants import *

screen = pygame.Surface((0,0))

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameloop()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def gameloop():
    while(True):
        if window_close(): return
        screen.fill(pygame.Color(0,0,0))
        
        pygame.display.flip()
        
def window_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

if __name__ == "__main__":
    main()