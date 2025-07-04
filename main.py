import pygame
import sys
from constants import *
from player import Player, Bullet
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Bullet.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    flying_stones = AsteroidField()
    player_ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    #GameLoop
    while 0 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = (Clock.tick(60) / 1000)
        Clock.tick(60)
        updatable.update(dt)
        for sprite in asteroids:
            if sprite.collision_check(player_ship) == True:
                raise sys.exit("Game over")
            for bullet in shots:
                if sprite.collision_check(bullet) == True:
                    sprite.split()
                    bullet.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        



if __name__ == "__main__":
    main()
