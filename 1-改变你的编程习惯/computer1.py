# 计算器
# 支持加、减、乘、除运算

# 定义加法函数
def add(a, b):
    return a + b

# 定义减法函数
def subtract(a, b):
    return a - b

# 定义乘法函数
def multiply(a, b):
    return a * b

# 定义除法函数并处理除零错误
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero!"

# 显示欢迎信息
print("Welcome to the calculator!")

while True:
    # 获取用户输入
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # 根据不同的运算符调用不同的函数计算结果
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator!")
        continue

    # 显示结果
    print("Result: ", result)

    # 询问用户是否继续
    choice = input("Continue? (y/n): ")
    if choice != 'y':
        break

print("Goodbye!")
