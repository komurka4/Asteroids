import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        ship.update(dt)
        ship.draw(screen)

        pygame.display.flip() # update the display
        dt = clock.tick(60) / 1000 # limit to 60 fps and convert to seconds
        
if __name__ == "__main__":
    main()
