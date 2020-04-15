
from pygame.locals import *
from random import randint
import pygame
import time
/*
the fist player and the class for the movement of the snake
*/
class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(snake,x,y):
        snake.x = x * snake.step
        snake.y = y * snake.step

    def draw(snake, surface, image):
        surface.blit(image,(snake.x, snake.y))


class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(snake, length):
       snake.length = length
       for i in range(0,2000):
           snake.x.append(-100)
           snake.y.append(-100)

       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44

    def update(snake):

        snake.updateCount = snake.updateCount + 1
        if snake.updateCount > snake.updateCountMax:

            # update previous positions
            for i in range(snake.length-1,0,-1):
                snake.x[i] = snake.x[i-1]
                snake.y[i] = snake.y[i-1]

            # update position of head of snake
            if snake.direction == 0:
                snake.x[0] = snake.x[0] + snake.step
            if snake.direction == 1:
                snake.x[0] = snake.x[0] - snake.step
            if snake.direction == 2:
                snake.y[0] = snake.y[0] - snake.step
            if snake.direction == 3:
                snake.y[0] = snake.y[0] + snake.step

            snake.updateCount = 0


    def moveRight(self):
        snake.direction = 0

    def moveLeft(self):
        snake.direction = 1

    def moveUp(self):
        snake.direction = 2

    def moveDown(self):
        snake.direction = 3

    def draw(snake, surface, image):
        for i in range(0,snake.length):
            surface.blit(image,(snake.x[i],snake.y[i]))

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0

    def __init__(snake):
        snake._running = True
        snake._display_surf = None
        snake._image_surf = None
        snake._apple_surf = None
        snake.game = Game()
        snake.player = Player(3)
        snake.apple = Apple(5,5)

    def on_init(snake):
        pygame.init()
        snake._display_surf = pygame.display.set_mode((snake.windowWidth,snake.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        snake._running = True
        snake._image_surf = pygame.image.load("block.jpg").convert()
        snake._apple_surf = pygame.image.load("block.jpg").convert()

    def on_event(snake, event):
        if event.type == QUIT:
            snake._running = False

    def on_loop(self):
        snake.player.update()

        # does snake eat apple?
        for i in range(0,self.player.length):
            if snake.game.isCollision(snake.apple.x,snake.apple.y,snake.player.x[i], snake.player.y[i],44):
                snake.apple.x = randint(2,9) * 44
                snake.apple.y = randint(2,9) * 44
                snake.player.length = snake.player.length + 1


        # does snake collide with itself?
        for i in range(2,snake.player.length):
            if snake.game.isCollision(snake.player.x[0],snake.player.y[0],snake.player.x[i], snake.player.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(snake.player.x[0]) + "," + str(snake.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(snake.player.x[i]) + "," + str(snake.player.y[i]) + ")")
                exit(0)

        pass

    def on_render(self):
        snake._display_surf.fill((0,0,0))
        snake.player.draw(snake._display_surf, snake._image_surf)
        snake.apple.draw(snake._display_surf, snake._apple_surf)
        pygame.display.flip()

    def on_cleanup(snake):
        pygame.quit()

    def on_execute(snake):
        if snake.on_init() == False:
            snake._running = False

        while( snake._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                snake.player.moveRight()

            if (keys[K_LEFT]):
                snake.player.moveLeft()

            if (keys[K_UP]):
                snake.player.moveUp()

            if (keys[K_DOWN]):
                snake.player.moveDown()

            if (keys[K_ESCAPE]):
                snake._running = False

            snake.on_loop()
            snake.on_render()

            time.sleep (50.0 / 1000.0);
        snake.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
