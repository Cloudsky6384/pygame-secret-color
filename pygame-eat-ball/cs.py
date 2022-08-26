# # # import pygame
# # #
# # # pygame.init()
# # #
# # # screen = pygame.display.set_mode((850, 540))
# # # screen.fill((240, 240, 240))
# # # # screen.fill("red")
# # #
# # # x, y = 10, 10
# # # player = pygame.Rect(x, y, 10, 10)
# # # pygame.draw.rect(screen, "red", player)
# # #
# # # clock = pygame.time.Clock()
# # #
# # # pygame.display.update()
# # #
# # # while True:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             pygame.quit()
# # #             exit()
# # #             pass
# # #         pass
# # #     clock.tick(60)
# #
# # import pygame
# # import time
# # from pygame.locals import *
# #
# # pygame.init()
# #
# #
# # class Player:
# #     def __init__(self, screen: pygame.Surface, size: tuple or list):
# #         if type(size) == tuple:
# #             size = list(size)
# #
# #         self.screen = screen
# #         x, y = 850 / 2, 540 / 2
# #         self.size = size
# #         self.rect = pygame.Rect(0, 0, *self.size)
# #         self.image = pygame.Surface(self.size)
# #         pygame.draw.rect(self.image, "red", self.rect)
# #         self.__pos = self.image.get_rect(center=(x, y))
# #         self.speed = 5
# #         self.player = None
# #
# #     @property
# #     def pos(self):
# #         return self.get_center_pos()
# #
# #     @pos.setter
# #     def pos(self, pos: tuple or list):
# #         if type(pos) == tuple:
# #             pos = list(pos)
# #
# #         self.__pos = pos
# #         self.__pos = self.get_left_pos()
# #
# #     def get_center_pos(self):
# #         """
# #         返回中心位置
# #         :return: 中心位置
# #         """
# #         return [self.__pos[0] + self.size[0] // 2, self.__pos[1] + self.size[1] // 2]
# #
# #     def get_left_pos(self):
# #         """
# #         返回左上角位置
# #         :return: 左上角位置
# #         """
# #         return [self.__pos[0] - self.size[0] // 2, self.__pos[1] - self.size[1] // 2]
# #
# #     def player_key(self):
# #         key_pressed = pygame.key.get_pressed()
# #         if key_pressed[K_w]:
# #             self.__pos[1] -= self.speed
# #         if key_pressed[K_s]:
# #             self.__pos[1] += self.speed
# #         if key_pressed[K_a]:
# #             self.__pos[0] -= self.speed
# #         if key_pressed[K_d]:
# #             self.__pos[0] += self.speed
# #
# #     def display(self):
# #         self.screen.blit(self.image, self.pos)
# #
# #
# # class Game:
# #     def __init__(self):
# #         # 设定窗口大小
# #         self.screen = pygame.display.set_mode((850, 540))
# #         self.screen_rect = self.screen.get_rect()
# #         # 设置窗口标题
# #         pygame.display.set_caption('Hole Wold', 'Hole Wold')
# #         # 设置窗口背景颜色
# #         self.screen.fill((240, 240, 240))
# #         pygame.display.flip()
# #         # 实例化 Clock Object 以便限制FPS
# #         self.clock = pygame.time.Clock()
# #
# #     def mainloop(self):
# #         play = Player(game.screen, (10, 10))
# #         while True:
# #             for event in pygame.event.get():
# #                 if event.type == pygame.QUIT:
# #                     pygame.quit()
# #                     exit()
# #
# #             self.screen.fill((240, 240, 240))
# #
# #             play.player_key()
# #             play.display()
# #
# #             pygame.display.update()
# #             # 限帧60
# #             self.clock.tick(60)
# #
# #
# # if __name__ == '__main__':
# #     game = Game()
# #     game.mainloop()
#
# import pygame
# import time
# from pygame.locals import *
#
# pygame.init()
#
#
# class Player:
#     def __init__(self, screen):
#         self.rect = None
#         self.screen = screen
#         self.x, self.y = 850 / 2, 540 / 2
#         self.speed = 3
#         self.player = None
#
#     def player_key(self):
#         key_pressed = pygame.key.get_pressed()
#         if key_pressed[K_w]:
#             self.y -= self.speed
#         if key_pressed[K_s]:
#             self.y += self.speed
#         if key_pressed[K_a]:
#             self.x -= self.speed
#         if key_pressed[K_d]:
#             self.x += self.speed
#
#     def display(self):
#         self.rect = pygame.Rect(self.x, self.y, 10, 10)
#         self.rect.center = self.rect.topleft
#         pygame.draw.rect(self.screen, "red", self.rect)
#         pygame.display.update()
#
#
# class Game:
#     def __init__(self):
#         # 设定窗口大小
#         self.screen = pygame.display.set_mode((850, 540))
#         # self.screen_rect = self.screen.get_rect()
#         # 设置窗口标题
#         pygame.display.set_caption('Hole Wold', 'Hole Wold')
#
#         # self.font_name = pygame.font.match_font('corbel')
#         # self.font = pygame.font.Font(self.font_name, 50)
#         self.font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
#         self.font_surface = self.font.render('1', True, (150, 150, 150))
#         # self.screen.blit(self.font_surface, (0, 0))
#
#         # 设置窗口背景颜色
#         self.screen.fill((240, 240, 240))
#         pygame.display.flip()
#         # 实例化 Clock Object 以便限制FPS
#         self.clock = pygame.time.Clock()
#         pygame.display.update()
#
#     def mainloop(self):
#         play = Player(game.screen)
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()
#
#             self.screen.fill((240, 240, 240))
#             self.screen.blit(self.font_surface, (0, 0))
#
#             play.player_key()
#             play.display()
#
#             # 限帧60
#             self.clock.tick(60)
#
#
# if __name__ == '__main__':
#     game = Game()
#     game.mainloop()
#


