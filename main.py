import pygame
from ship import *
from asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock =  pygame.time.Clock()
color = (0, 10, 30)

Numlevels = 4
Level = 1
AsteroidCount = 3
player = Ship()
danger = Asteroid()

speed = pygame.math.Vector2(5, 0)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
self.image = pygame.transform.rotate(self.image, 270 - rotation)

def move_asteroid():
      screen_info = pygame.display.Info()
      global self
      self.rect.move_ip(speed)
      if self.rect.bottom > screen_info.current_h or self.rect.top < 0:
        speed[1] *= -1
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.move_ip(0, speed[1])

      if self.rect.right > screen_info.current_w or self.rect.left < 0:
        speed[1] *= -1
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.move_ip(0, speed[1])
        speed[0] *= -1
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect.move_ip(speed[0], 0) 

def main():
   while Level <= Numlevels:
      clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
            player.speed[0] = 10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
            player.speed[0] = 0

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            player.speed[0] = -10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            player.speed[0] = 0

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            player.speed[1] = -10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            player.speed[1] = 0
            
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            player.speed[1] = 10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_DOWN:
            player.speed[1] = 0
      move_asteriod()  
      player.update()
      screen.fill(color)
      screen.blit(danger.image, danger.rect)
      screen.blit(player.image, player.rect)
      pygame.display.flip()

if __name__=='__main__':
  main()
