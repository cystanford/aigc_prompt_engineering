import pygame
import random

pygame.init()

# 初始化窗口
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色常量
white = (255, 255, 255)
black = (0, 0, 0)

# 初始化游戏状态
game_over = False

# 定义贪吃蛇类
class Snake:
    def __init__(self):
        self.pos = [(1, 1), (1, 2), (1, 3)]
        self.direction = "right"

    def draw(self):
        for p in self.pos:
            pygame.draw.rect(screen, white, (p[0]*10, p[1]*10, 10, 10), 0)

    def move(self):
        global game_over

        # 根据当前移动方向更新贪吃蛇位置
        if self.direction == "up":
            if self.pos[0][1] > 0:
                self.pos.insert(0, (self.pos[0][0], self.pos[0][1]-1))
            else:
                game_over = True
        elif self.direction == "down":
            if self.pos[0][1] < height/10-1:
                self.pos.insert(0, (self.pos[0][0], self.pos[0][1]+1))
            else:
                game_over = True
        elif self.direction == "left":
            if self.pos[0][0] > 0:
                self.pos.insert(0, (self.pos[0][0]-1, self.pos[0][1]))
            else:
                game_over = True
        elif self.direction == "right":
            if self.pos[0][0] < width/10-1:
                self.pos.insert(0, (self.pos[0][0]+1, self.pos[0][1]))
            else:
                game_over = True
            
        # 删除蛇尾，以保持长度不变
        if not game_over:
            self.pos.pop()

    def change_direction(self, direction):
        if direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "right" and self.direction != "left":
            self.direction = "right"

# 定义食物类
class Food:
    def __init__(self):
        self.pos = (0, 0)
        self.randomize()

    def draw(self):
        # 绘制食物
        pygame.draw.rect(screen, (255, 0, 0), (self.pos[0]*10, self.pos[1]*10, 10, 10), 0)

    def randomize(self):
        # 在随机位置生成食物
        while True:
            temp_pos = (random.randint(0, width//10-1), random.randint(0, height//10-1))
            if temp_pos not in snake.pos:
                break
        self.pos = temp_pos

# 初始化贪吃蛇和食物
snake = Snake()
food = Food()

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("right")

    # 绘制背景
    screen.fill(black)

    # 绘制贪吃蛇和食物
    snake.draw()
    food.draw()

    # 贪吃蛇移动
    snake.move()

    # 检测贪吃蛇是否吃到食物
    if snake.pos[0] == food.pos:
        food.randomize()
    
    # 检测贪吃蛇是否撞墙或者吃到自己
    for i, pos in enumerate(snake.pos):
        if i != 0 and pos == snake.pos[0]:
            game_over = True
            break
    
    # 刷新屏幕
    pygame.display.update()

    if game_over:
        # 显示 Game Over 文字
        font = pygame.font.SysFont(None, 24)
        text = font.render("Game Over!", True, white)
        screen.blit(text, (width/2-50, height/2-12))
        pygame.display.update()
        pygame.time.wait(2000)
        break

    pygame.time.wait(200)