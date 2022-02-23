import pygame
from pygame import gfxdraw
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU # 1AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distanceToSun = 0

        self.xVel = 0
        self.yVel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        pygame.gfxdraw.aacircle(win, int(x), int(y), self.radius, self.colour)
        pygame.gfxdraw.filled_circle(win, int(x), int(y), self.radius, self.colour)

def main():
    run = True
    planets = []
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, (255, 255, 0), 1.98892 * 10**30)
    sun.sun = True
    planets.append(sun)

    earth = Planet(-1 * Planet.AU, 0, 16, (100, 149, 237), 5.9742 * 10**24)
    planets.append(earth)
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, (207, 119, 87), 6.39 * 10**23)
    planets.append(mars)

    mercury = Planet(0.387 * Planet.AU, 0, 8, (80, 78, 81), 3.30 * 10**23)
    planets.append(mercury)

    venus = Planet(0.723 * Planet.AU, 0, 14, (255, 255, 255), 4.8685 * 10**24)
    planets.append(venus)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)
        
        pygame.display.update()

    pygame.quit()

main()
