import pygame
import random
import time
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()


# 创建玩家类
class Player:
    def __init__(self, screen):
        # 初始化颜色
        self.color = "white"
        # 初始化背景颜色
        self.color_back = (255, 159, 243)
        # 传入窗口
        self.screen = screen
        self.player = None
        # 规定玩家大小
        self.size = (17, 17)
        # 规定初始坐标
        self.x, self.y = 1200 / 2, 700 / 2
        # 生成位置信息
        self.player_rect = pygame.Rect(self.x, self.y, *self.size)
        # 规定移动速度
        self.speed = 2

    # 设定玩家移动按键绑定
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

    # 显示在screen窗口
    def display(self):
        self.player_rect = pygame.Rect(self.x, self.y, *self.size)
        self.player_rect.center = self.player_rect.topleft
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(self.screen, self.color, self.player_rect)


# 创建子弹类
class Bullet:
    def __init__(self, screen, color):
        self.a = None
        self.screen = screen
        self.color = color
        # 设定子弹出现坐标
        self.x, self.y = random.randint(0, 1200), random.randint(0, 700)
        # 子弹位置信息
        self.bull_rect = pygame.Rect(self.x, self.y, 5, 5)
        # 子弹颜色
        self.color_bull = random.choice(self.color)

    # 显示在screen窗口
    def display(self):
        pygame.draw.circle(self.screen, self.color_bull, [self.x, self.y], 5, 0)


# 创建子弹集类
class BulletSet:
    def __init__(self, screen, color):
        self.bullet_r = None
        # 创建子弹集
        self.bullets = []
        # 创建子弹位置信息集
        self.bullets_rect = []
        self.screen = screen
        self.color = color
        self.bullets_number = 0
        # 生成40个子弹
        while self.bullets_number < 40:
            bullet = Bullet(self.screen, self.color)
            # 当前生成子弹图像录入子弹集
            self.bullets.append(bullet)
            # 当前生成子弹位置信息录入子弹位置信息集
            self.bullets_rect.append(bullet.bull_rect)
            self.bullets_number += 1

    # 显示在screen窗口
    def display(self):
        for bullet in self.bullets:
            self.bullet_r = bullet
            bullet.display()


class Game:
    def __init__(self):
        self.screen_over = self.s_s = self.s = self.m = self.SYSJ = self.t1 = self.player_rect = \
            self.bull_rect = self.font_fraction = self.bullets = self.bullet = self.bullets_rect = None
        # 设定颜色集
        self.color = [(255, 159, 243), (95, 39, 205), (84, 160, 255), (0, 210, 211), (29, 209, 161), (72, 219, 251),
                      (255, 107, 107), (255, 107, 107), (254, 202, 87), (255, 159, 243)]
        # 设定背景颜色
        self.color_back = (255, 159, 243)

        self.fraction = 0

        # 设定字体文件
        self.font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        self.font_o = pygame.font.Font('./font/MiSans-Light.ttf', 70)
        self.font_over = self.font_o.render('over!', True, (140, 140, 140))

        # 设定倒计时时间
        self.game_time = 30
        self.start_time = time.time()

        # 设定窗口和窗口大小
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen_rect = self.screen.get_rect()

        # 设定窗口标题
        pygame.display.set_caption('by Cloudsky', 'by Cloudsky')

        # 设定背景颜色
        self.screen.fill(self.color_back)
        pygame.display.flip()

        # 设定时间帧
        self.clock = pygame.time.Clock()

    # 游戏倒计时模块
    def time(self):
        self.t1 = time.time() - self.start_time
        self.SYSJ = self.game_time - self.t1
        self.m, self.s = divmod(self.SYSJ, 60)
        self.s_s = int(self.s)

    # 游戏文字显示模块
    def game_font(self, SYSJ, s_s):
        self.SYSJ = SYSJ
        self.s_s = s_s
        self.font_fraction = self.font.render('%d' % self.fraction, True, (140, 140, 140))
        self.screen.blit(self.font_fraction, (10, 1))
        if self.SYSJ > 0:
            font_time = self.font.render('%d' % self.s_s, True, (140, 140, 140))
            self.screen.blit(font_time, (1130, 1))
        else:
            self.screen_over = self.screen.blit(self.font_over, (1200 / 2 - 70, 700 / 2 - 70))

    # 游戏碰撞
    def collide(self, player_rect, bull_rect, bullets, bullets_rect):
        self.player_rect = player_rect
        self.bull_rect = bull_rect
        self.bullets = bullets
        self.bullets_rect = bullets_rect
        i = 0
        for bullrect in self.bull_rect:
            if self.player_rect.colliderect(bullrect):
                self.bullets.pop(i)
                self.bullets_rect.remove(bullrect)
                self.fraction += 1
            i += 1

    # 游戏背景颜色切换按键绑定
    def game_key(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            if pygame.display.get_active():
                self.color_back = random.choice(self.color)

    # 显示窗口
    def display(self):
        player = Player(game.screen)
        bulletset = BulletSet(game.screen, game.color)
        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.game_key(event)
            self.screen.fill(self.color_back)

            game.collide(player.player_rect, bulletset.bullets_rect, bulletset.bullets, bulletset.bullets_rect)

            bulletset.display()

            player.player_key()
            player.display()

            self.time()
            self.game_font(game.SYSJ, game.s_s)

            pygame.display.update()

            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.display()
