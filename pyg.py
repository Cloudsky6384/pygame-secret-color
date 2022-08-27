import pygame
import random
import time
from pygame.locals import *

pygame.init()


class Player:
    def __init__(self, screen, size):
        self.color = "white"
        self.color_back = (255, 159, 243)
        self.screen = screen
        # self.rect = None
        self.player = None
        self.size = size
        self.x, self.y = 1200 / 2, 700 / 2
        self.rect = pygame.Rect(self.x, self.y, *self.size)
        self.speed = 3

    def player_key(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w]:
            self.y -= self.speed
        if key_pressed[K_s]:
            self.y += self.speed
        if key_pressed[K_a]:
            self.x -= self.speed
        if key_pressed[K_d]:
            self.x += self.speed

    def display(self):
        self.rect = pygame.Rect(self.x, self.y, *self.size)
        self.rect.center = self.rect.topleft
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(self.screen, self.color, self.rect)


class Wall:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y
        self.wall_right = None
        self.wall_left = None
        self.wall_down = None
        self.wall_up = None

    def display(self):
        self.wall_left = pygame.Rect(self.x - 9, self.y, 3, 20)
        self.wall_right = pygame.Rect(self.x + 9, self.y, 3, 20)
        self.wall_up = pygame.Rect(self.x, self.y - 9, 20, 3)
        self.wall_down = pygame.Rect(self.x, self.y + 9, 20, 3)
        self.wall_left.center = self.wall_left.topleft
        self.wall_right.center = self.wall_right.topleft
        self.wall_up.center = self.wall_up.topleft
        self.wall_down.center = self.wall_down.topleft
        pygame.draw.rect(self.screen, "black", self.wall_left)
        pygame.draw.rect(self.screen, "black", self.wall_right)
        pygame.draw.rect(self.screen, "black", self.wall_up)
        pygame.draw.rect(self.screen, "black", self.wall_down)


class Ballet:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.zd = 0
        self.x, self.y = random.randint(0, 1200), random.randint(0, 700)
        self.bull_rect = pygame.Rect(self.x, self.y, 5, 5)

    # def bull_sc(self):
    #     while self.zd < 40:
    #         self.bull_rect = pygame.Rect(self.x, self.y, 5, 5)
    #         self.bulls.append(self.bull_rect)
    #         self.zd += 1

    def display(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], 5, 0)


class Bull:
    def __init__(self):
        self.bulls = []
        self.bulls_sl = 0
        game = Game()
        while self.bulls_sl < 4:
            self.color = [(236, 204, 104), (255, 127, 80), (255, 107, 129), (164, 176, 190)]
            self.color_bull = random.choice(self.color)
            bullet = Ballet(game.screen, self.color_bull)
            self.bulls.append(bullet)
            self.bulls_sl += 1

    def display(self):
        for bullet in self.bulls:
            bullet.display()


class Collide:
    def __init__(self, bull_rect, player_rect: pygame.Rect, screen):
        self.font_fraction = None
        self.game = None
        self.gamefont = None
        self.screen = screen
        # self.fraction = fraction
        self.fraction = 0
        self.bull_rect = bull_rect
        self.player_rect = player_rect
        self.font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        # self.font_fraction = self.font.render('%d' % self.fraction, True, (140, 140, 140))
        # self.screen.blit(self.font_fraction, (10, 1))

    def collide(self):
        if self.player_rect.colliderect(self.bull_rect):
            self.fraction += 1
        self.font_fraction = self.font.render('%d' % self.fraction, True, (140, 140, 140))
        self.screen.blit(self.font_fraction, (10, 1))


class GameTime:
    def __init__(self, screen):
        self.font_fraction = None
        self.screen_over = None
        self.s_s = None
        self.s = None
        self.m = None
        self.SYSJ = None
        self.t1 = None
        self.screen = screen
        self.font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        self.game_time = 60
        self.start_time = time.time()
        # self.font_fraction = self.font.render('%d' % self.fraction, True, (140, 140, 140))
        # self.font_time = self.font.render('%d' % self.game_time, True, (140, 140, 140))
        self.font_o = pygame.font.Font('./font/MiSans-Light.ttf', 70)
        self.font_over = self.font_o.render('over!', True, (140, 140, 140))

    def game_time_f(self):
        self.t1 = time.time() - self.start_time
        self.SYSJ = self.game_time - self.t1
        self.m, self.s = divmod(self.SYSJ, 60)
        self.s_s = int("%d" % self.s)
        if self.SYSJ > 0:
            font_time = self.font.render('%d' % self.s_s, True, (140, 140, 140))
            self.screen.blit(font_time, (1130, 1))
        else:
            self.screen_over = self.screen.blit(self.font_over, (1200 / 2 + 70, 700 / 2 + 70))


class Game:
    def __init__(self):
        self.color = [(236, 204, 104), (255, 127, 80), (255, 107, 129), (164, 176, 190)]
        self.color_back = (255, 159, 243)
        self.color_bull = random.choice(self.color)
        self.fraction = 0
        # 设定窗口大小
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen_rect = self.screen.get_rect()
        # 设置窗口标题
        pygame.display.set_caption('Hello World', 'Hello World')

        # self.font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        # self.font_fraction = self.font.render('%d' % self.fraction, True, (140, 140, 140))
        # self.font_time = self.font.render('%d' % self.game_time, True, (140, 140, 140))

        # 设置窗口背景颜色
        self.screen.fill(self.color_back)
        pygame.display.flip()
        # 实例化 Clock Object 以便限制FPS
        self.clock = pygame.time.Clock()

    def change_screen_color(self):
        self.color_back = random.choice(self.color)

    def mainloop(self):
        play = Player(game.screen, (11, 11))
        bullet = Ballet(game.screen, game.color_bull)
        gamefont = GameTime(game.screen)
        # collide = Collide(bullet.bull_rect, play.rect, game.screen)
        bull = Bull()
        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                        (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if pygame.display.get_active():
                        self.change_screen_color()

            self.screen.fill(self.color_back)
            # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # self.screen.fill(self.color)
            play.player_key()

            gamefont.game_time_f()

            wall = Wall(game.screen, play.x, play.y)
            wall.display()

            collide = Collide(bullet.bull_rect, play.rect, game.screen)
            bull.display()
            bullet.display()
            play.display()
            collide.collide()

            # 限帧60
            self.clock.tick(60)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
