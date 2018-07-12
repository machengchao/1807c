import pygame
pygame.init()
# 游戏代码... 
pygame.quit()
hero_rect = pygame.Rect(100, 500, 120, 126)
print("坐标原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄大小 %d %d" % (hero_rect.width, hero_rect.height))  
# size 属性会返回矩形区域的 (宽, 高) 元组
print("英雄大小 %d %d" % hero_rect.size)

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))
# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))

# 游戏循环
while True:
    pass
# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")
# 2> 绘制在屏幕
screen.blit(bg, (0, 0))
# 3> 更新显示
pygame.display.update()
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制在屏幕
screen.blit(hero, (200, 500))
# 3> 更新显示
pygame.display.update()
# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")
# 2> 绘制在屏幕
screen.blit(bg, (0, 0))
# 绘制英雄图像
# 1> 加载图像
hero = pygame.image.load("./images/me1.png")
# 2> 绘制在屏幕
screen.blit(hero, (200, 500))
# 3> 更新显示 - update 方法会把之前所有绘制的结果，一次性更新到屏幕窗口上
pygame.display.update()

clock = pygame.time.Clock()
i = 0
# 游戏循环
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)
    print(i)
    i += 1
# 4. 定义英雄的初始位置
    hero_rect = pygame.Rect(150, 500, 102, 126)
    while True:
            # 可以指定循环体内部的代码执行的频率
            clock.tick(60)
            # 更新英雄位置
            hero_rect.y -= 1
            # 如果移出屏幕，则将英雄的顶部移动到屏幕底部
            if hero_rect.y <= 0:
                    hero_rect.y = 700
            # 绘制背景图片
            screen.blit(bg, (0, 0))
            # 绘制英雄图像
            screen.blit(hero, hero_rect)
            # 更新显示
            pygame.display.update()

if hero_rect.bottom <= 0:
    hero_rect.y = 700
# 游戏循环
    while True:
          # 设置屏幕刷新帧率
          clock.tick(60)
          #  事件监听
          for event in pygame.event.get():
                # 判断用户是否点击了关闭按钮
                if event.type == pygame.QUIT:
                      print("退出游戏...")
                      pygame.quit()
                      # 直接退出系统
                      exit()

import pygame
class GameSprite(pygame.sprite.Sprite):
 """游戏精灵基类"""
    def __init__(self, image_name, speed=1):
    # 调用父类的初始化方法
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
       # 记录速度
        self.speed = speed
    def update(self, *args):
        # 默认在垂直方向移动
        self.rect.y += self.speed

from plane_sprites import *
# 让敌机组调用 update 和 draw 方法
enemy_group.update()
enemy_group.draw(screen)
# 更新屏幕显示
pygame.display.update()
import pygame
from plane_sprites import *
class PlaneGame(object):
"""飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
    def start_game(self):
        print("开始游戏...")
if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()
def __init__(self):
      print("游戏初始化")
      # 1. 创建游戏的窗口
      self.screen = pygame.display.set_mode((480, 700))
      # 2. 创建游戏的时钟
      self.clock = pygame.time.Clock()
      # 3. 调用私有方法，精灵和精灵组的创建
      self.__create_sprites()
  def __create_sprites(self):
      pass

import pygame
  # 游戏屏幕大小
  SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
self.screen = pygame.display.set_mode(SCREEN_RECT.size)
def start_game(self):
  """开始游戏"""
      print("开始游戏...")
      while True:
          # 1. 设置刷新帧率
          self.clock.tick(60)
          # 2. 事件监听
          self.__event_handler()
          # 3. 碰撞检测
          self.__check_collide()
          # 4. 更新精灵组
          self.__update_sprites()
          # 5. 更新屏幕显示
          pygame.display.update()
  def __event_handler(self):
  """事件监听"""
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              PlaneGame.__game_over()
  def __check_collide(self):
  """碰撞检测"""
      pass
  def __update_sprites(self):
    """更新精灵组"""
      pass

  @staticmethod
  def __game_over(): 
  """游戏结束"""

       print("游戏结束")
       pygame.quit()
       exit()

def __create_sprites(self):
   """创建精灵组"""
      # 背景组
      self.back_group = pygame.sprite.Group()
      # 敌机组
      self.enemy_group = pygame.sprite.Group()
      # 英雄组
      self.hero_group = pygame.sprite.Group()
def __update_sprites(self):
 """更新精灵组"""
      for group in [self.back_group, self.enemy_group, self.hero_group]:
          group.update()
          group.draw(self.screen)

class Background(GameSprite):
   """游戏背景精灵"""
      def update(self):
      # 1. 调用父类的方法实现
          super().update()
          # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
          if self.rect.y >= SCREEN_RECT.height:
              self.rect.y = -self.rect.height

def __create_sprites(self):
# 创建背景精灵和精灵组
    bg1 = Background("./images/background.png")
    bg2 = Background("./images/background.png")
    bg2.rect.y = -bg2.rect.height
    self.back_group = pygame.sprite.Group(bg1, bg2)

def __update_sprites(self):
    self.back_group.update()
    self.back_group.draw(self.screen)
def __init__(self, is_alt=False):
    image_name = "./images/background.png"
    super().__init__(image_name)
    # 判断是否交替图片，如果是，将图片设置到屏幕顶部
    if is_alt:
        self.rect.y = -self.rect.height

# 创建背景精灵和精灵组
bg1 = Background()
bg2 = Background(True)
self.back_group = pygame.sprite.Group(bg1, bg2)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 4. 设置定时器事件 - 每秒创建一架敌机
pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
def __event_handler(self):
   for event in pygame.event.get():
       # 判断是否退出游戏
       if event.type == pygame.QUIT:
           PlaneGame.__game_over()
           elif event.type == CREATE_ENEMY_EVENT:
           print("敌机出场...")

class Enemy(GameSprite):
"""敌机精灵"""
    def __init__(self):
        # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy1.png")
        # 2. 设置敌机的随机初始速度
        # 3. 设置敌机的随机初始位置
    def update(self):
        # 1. 调用父类方法，让敌机在垂直方向运动
        super().update()
        # 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕...")

# 敌机组
self.enemy_group = pygame.sprite.Group()
self.enemy_group.update()
self.enemy_group.draw(self.screen)
elif event.type == CREATE_ENEMY_EVENT:
self.enemy_group.add(Enemy())
import random
def __init__(self):
      # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
      super().__init__("./images/enemy1.png")
      # 2. 设置敌机的随机初始速度 1 ~ 3
      self.speed = random.randint(1, 3)
      # 3. 设置敌机的随机初始位置
      self.rect.bottom = 0
      max_x = SCREEN_RECT.width - self.rect.width
      self.rect.x = random.randint(0, max_x)

def update(self):
    super().update()
    # 判断敌机是否移出屏幕
    if self.rect.y >= SCREEN_RECT.height:
        # 将精灵从所有组中删除
        self.kill()
class Hero(GameSprite):
"""英雄精灵"""
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

# 英雄组
self.hero = Hero()
self.hero_group = pygame.sprite.Group(self.hero)
self.hero_group.update()
self.hero_group.draw(self.screen)
# 返回所有按键的元组，如果某个键被按下，对应的值会是1
 keys_pressed = pygame.key.get_pressed()
 # 判断是否按下了方向键
 if keys_pressed[pygame.K_RIGHT]:
     print("向右移动...")
def update(self):
# 飞机水平移动
self.rect.x += self.speed
# 获取用户按键
keys_pressed = pygame.key.get_pressed()
if keys_pressed[pygame.K_RIGHT]:
    self.hero.speed = 2
elif keys_pressed[pygame.K_LEFT]:
    self.hero.speed = -2
else:
    self.hero.speed = 0

def update(self):
     # 飞机水平移动
     self.rect.x += self.speed
     # 判断屏幕边界
     if self.rect.left < 0:
         self.rect.left = 0
     if self.rect.right > SCREEN_RECT.right:
         self.rect.right = SCREEN_RECT.right

def fire(self):
print("发射子弹...")
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# 每隔 0.5 秒发射一次子弹
pygame.time.set_timer(HERO_FIRE_EVENT, 500)
elif event.type == HERO_FIRE_EVENT:
    self.hero.fire()
class Bullet(GameSprite):
   """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)
    def update(self):
        super().update()
        # 判断是否超出屏幕，如果是，从精灵组删除
        if self.rect.bottom < 0:
            self.kill()

# 创建子弹的精灵组
self.bullets = pygame.sprite.Group()
def fire(self):
    # 1. 创建子弹精灵
    bullet = Bullet()
    # 2. 设置精灵的位置
    bullet.rect.bottom = self.rect.y - 20
    bullet.rect.centerx = self.rect.centerx
    # 3. 将精灵添加到精灵组
    self.bullets.add(bullet)
def __check_collide(self):
      # 1. 子弹摧毁敌机
      pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
      # 2. 敌机撞毁英雄
      enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
      # 判断列表时候有内容
      if len(enemies) > 0:
          # 让英雄牺牲
         self.hero.kill()
         # 结束游戏
         PlaneGame.__game_over()
