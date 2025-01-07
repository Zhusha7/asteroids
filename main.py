import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                return
        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(FRAME_RATE)/1000

if __name__ == "__main__":
    main()