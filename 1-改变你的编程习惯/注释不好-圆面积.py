import math

# 定义函数
def circle_area(radius):
    area = math.pi * radius ** 2 # 计算乘法
    return area # 返回结果

if __name__ == '__main__':
    r = float(input("请输入圆的半径: ")) # 用户输入
    a = circle_area(r) # 调用函数
    print(f"半径为 {r} 的圆的面积是 {a:.2f}") # 输出结果
