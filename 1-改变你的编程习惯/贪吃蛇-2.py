import pygame
import random

# 初始化 Pygame 库
pygame.init()

# 定义游戏窗口尺寸和标题
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义游戏对象
class Snake:
    def __init__(self):
        self.pos = [(4, 4), (5, 4), (6, 4)]
        self.direction = "right"
    
    def move(self):
        # 根据当前移动方向更新贪吃蛇位置
        if self.direction == "up":
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]-1))
        elif self.direction == "down":
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]+1))
        elif self.direction == "left":
            self.pos.insert(0, (self.pos[0][0]-1, self.pos[0][1]))
        elif self.direction == "right":
            self.pos.insert(0, (self.pos[0][0]+1, self.pos[0][1]))
            
        # 删除蛇尾，以保持长度不变
        self.pos.pop()
    
    def draw(self):
        # 绘制贪吃蛇身体
        for x, y in self.pos:
            pygame.draw.rect(screen, (0, 255, 0), (x*10, y*10, 10, 10), 0)
    
    def eat(self, food):
        # 检测贪吃蛇是否吃到了食物
        if self.pos[0] == food.pos:
            self.pos.append(food.pos)
            food.randomize()

class Food:
    def __init__(self):
        self.pos = (0, 0)
        self.randomize()
    
    def draw(self):
        # 绘制食物
        pygame.draw.rect(screen, (255, 0, 0), (self.pos[0]*10, self.pos[1]*10, 10, 10), 0)
    
    def randomize(self):
        # 在随机位置生成食物
        self.pos = (random.randint(0, width//10-1), random.randint(0, height//10-1))

# 初始化游戏对象
snake = Snake()
food = Food()

# 开始游戏主循环
game_over = False
clock = pygame.time.Clock()
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # 根据键盘输入更新蛇移动方向
            if event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
    
    # 更新游戏对象
    snake.move()
    snake.eat(food)
    
    # 检测贪吃蛇是否撞墙
    if not 0 <= snake.pos[0][0] < width//10 or not 0 <= snake.pos[0][1] < height//10:
        game_over = True
    
    # 检测贪吃蛇是否吃到自己
    for i, pos in enumerate(snake.pos):
        if i != 0 and pos == snake.pos[0]:
            game_over = True
            
    # 绘制游戏
    screen.fill((255, 255, 255))
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # 控制游戏速度
    clock.tick(10)

# 显示 Game Over 提示
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, (0, 0, 0))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (width/2, height/2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

# 等待一段时间后退出 Pygame 库
pygame.time.wait(2000)
pygame.quit()
