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

    def attraction(self, planet):
        planetX, planetY = planet.x, planet.y
        distanceX = planetX - self.x
        distanceY = planetY - self.y
        distance = math.sqrt(distanceX**2 + distanceY**2)
        if planet.sun:
            self.distanceToSun = distance

        force = (self.G * self.mass * planet.mass) / distance**2
        theta = math.atan2(distanceY, distanceX)
        forceX = math.cos(theta) * force
        forceY = math.sin(theta) * force

        return forceX, forceY

    def updatePos(self, planets):
        totalFx = totalFy = 0

        for planet in planets:
            if self == planet:
                continue

            fX, fY = self.attraction(planet)
            totalFx += fX
            totalFy += fY

        self.xVel += totalFx / self.mass * self.TIMESTEP
        self.yVel += totalFy / self.mass * self.TIMESTEP

        self.x += self.xVel * self.TIMESTEP
        self.y += self.yVel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    run = True
    planets = []
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, (255, 255, 0), 1.98892 * 10**30)
    sun.sun = True
    planets.append(sun)

    earth = Planet(-1 * Planet.AU, 0, 16, (100, 149, 237), 5.9742 * 10**24)
    earth.yVel = 29.783 * 1000
    planets.append(earth)
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, (207, 119, 87), 6.39 * 10**23)
    mars.yVel = 24.077 * 1000
    planets.append(mars)

    mercury = Planet(0.387 * Planet.AU, 0, 8, (80, 78, 81), 3.30 * 10**23)
    mercury.yVel = -47.4 * 1000
    planets.append(mercury)

    venus = Planet(0.723 * Planet.AU, 0, 14, (255, 255, 255), 4.8685 * 10**24)
    venus.yVel = -35.02 * 1000
    planets.append(venus)

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.updatePos(planets)
            planet.draw(WIN)
        
        pygame.display.update()

    pygame.quit()

main()
