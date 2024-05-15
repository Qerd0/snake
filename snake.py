import pygame
from random import randint
pygame.font.init()
pygame.mixer.init()


class Snake:
    def __init__(self):
        self.color = pygame.Color("Black")
        self.direction = "RIGHT"
        self.thesnake = [(230, 200), (260, 200), (290, 200), (320, 200), (350, 200)]

    def render(self, screen, collision):
        for i in self.thesnake:
            pygame.draw.rect(screen, self.color, pygame.Rect(i[0], i[1], 30, 30))
            self.rect = pygame.Rect(i[0], i[1], 30, 30)
        if collision == "False":
            if self.direction == "UP":
                self.thesnake.append(
                    (self.thesnake[len(self.thesnake) - 1][0], self.thesnake[len(self.thesnake) - 1][1] - 33))

            if self.direction == "DOWN":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0], self.thesnake[len(self.thesnake) - 1][1] + 33))

            if self.direction == "RIGHT":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0] + 33, self.thesnake[len(self.thesnake) - 1][1]))

            if self.direction == "LEFT":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0] - 33, self.thesnake[len(self.thesnake) - 1][1]))
            self.thesnake.remove(self.thesnake[0])
        else:
            if self.direction == "UP":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0], self.thesnake[len(self.thesnake) - 1][1] - 33))

            if self.direction == "DOWN":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0], self.thesnake[len(self.thesnake) - 1][1] + 33))

            if self.direction == "RIGHT":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0] + 33, self.thesnake[len(self.thesnake) - 1][1]))

            if self.direction == "LEFT":
                self.thesnake.append((self.thesnake[len(self.thesnake) - 1][0] - 33, self.thesnake[len(self.thesnake) - 1][1]))

    def moveUp(self):
        self.direction = "UP"

    def moveDown(self):
        self.direction = "DOWN"

    def moveRight(self):
        self.direction = "RIGHT"

    def moveLeft(self):
        self.direction = "LEFT"


class food:
    def __init__(self):
        self.ball = pygame.Color("Red")
        self.back = pygame.Color("White")
        self.X_cordinate = randint(200, 899)
        self.Y_cordinate = randint(201, 600)

    def render(self, screen):
        pygame.draw.rect(screen, self.back, pygame.Rect(self.X_cordinate - 5, self.Y_cordinate - 5, 10, 10))
        pygame.draw.circle(screen, self.ball, (self.X_cordinate, self.Y_cordinate), 7)

    def movement(self):
        x1 = self.X_cordinate
        y1 = self.Y_cordinate
        x2 = randint(0, 730)
        y2 = randint(225, 700)
        if x1 != x2 or y1 != y2:
            self.X_cordinate = x2
            self.Y_cordinate = y2


class Score:
    def __init__(self):
        self.color = pygame.Color("Black")

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(0, 100, 1200, 4))


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.playing = "True"
        self.counter = 0
        self.text = pygame.font.SysFont('Helvetica', 30)
        self.loosetext = pygame.font.SysFont('Helvetica', 100)
        self.text1 = self.text.render('SNAKE', False, (0, 0, 0))
        self.scoretext = self.text.render('YOUR SCORE:' + ' ' + str(self.counter), False, (0, 0, 0))
        self.text4 = self.loosetext.render('YOU LOST!', False, (255, 0, 0))
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("TODO")
        self.clock = pygame.time.Clock()
        self.running = True
        self.collision = "False"
        self.snake = Snake()
        self.apple = food()
        self.menu = Score()
        self.rect2 = pygame.Rect(self.apple.X_cordinate - 14, self.apple.Y_cordinate - 6, 30, 30)
        self.line1 = pygame.Rect(0, 100, 1200, 4)


    def update(self):
        self.events()

    def events(self):
        self.collision = "False"
        self.result = "None"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.snake.direction != "DOWN":
                self.snake.moveUp()
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.snake.direction != "UP":
                self.snake.moveDown()
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.snake.direction != "RIGHT":
                self.snake.moveLeft()
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.snake.direction != "LEFT":
                self.snake.moveRight()
        if self.snake.thesnake[len(self.snake.thesnake) - 1][0] - 15 >= 1200:
            self.playing = "False"
        if self.snake.thesnake[len(self.snake.thesnake) - 1][0] + 15 <= 0:
            self.playing = "False"
        if self.snake.thesnake[len(self.snake.thesnake) - 1][1] + 15 <= 0:
            self.playing = "False"
        if self.snake.thesnake[len(self.snake.thesnake) - 1][1] - 15 >= 700:
            self.playing = "False"
        if self.borderCollision() == True:
            self.playing = "False"
        if self.collides() == True:
            self.collision = "True"
            self.apple.movement()
            self.rect2 = pygame.Rect(self.apple.X_cordinate - 14, self.apple.Y_cordinate - 14, 30, 30)
        for i in range(0, len(self.snake.thesnake) - 1):
            if pygame.Rect(self.snake.thesnake[len(self.snake.thesnake) - 1][0], self.snake.thesnake
            [len(self.snake.thesnake) - 1][1], 30, 30).colliderect(
                pygame.Rect(self.snake.thesnake[i][0], self.snake.thesnake[i][1], 30, 30)):
                self.playing = "False"

    def collides(self):
        self.rect1 = pygame.Rect(self.snake.thesnake[len(self.snake.thesnake) - 1][0],self.snake.thesnake[len(self.snake.thesnake) - 1][1], 30, 30)
        if self.rect1.colliderect(self.rect2):
            self.counter += 1
            self.scoretext = self.text.render('YOUR SCORE:' + ' ' + str(self.counter), False, (0, 0, 0))
            return True

    def borderCollision(self):
        a = pygame.Rect(self.snake.thesnake[len(self.snake.thesnake) - 1][0] - 20,self.snake.thesnake[len(self.snake.thesnake) - 1][1] , 30, 30)
        if a.colliderect(self.line1):
            return True

    def render(self):
        if self.playing == "True":
          self.screen.fill((0, 100, 0))
          self.apple.render(self.screen)
          self.screen.blit(self.text1, (920, 30))
          self.screen.blit(self.scoretext, (920, 100))
          self.menu.render(self.screen)
          self.snake.render(self.screen, self.collision)
          pygame.display.flip()
          self.clock.tick(20)
        else:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text4, (350, 250))
            self.screen.blit(self.scoretext, (300, 400))
            pygame.display.flip()
            self.clock.tick(20)

    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()



