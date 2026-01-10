"""函数
- 定义
  - def 函数名(参数1, 参数2, ...):
    函数体
    return 返回值
- 调用
  - 函数名(参数1, 参数2, ...)
- 函数的说明文档
  - help(函数名): 查看函数的说明文档
- global
  - global 变量名: 声明变量为全局变量

"""

""" ------------------------ 函数的说明文档 ------------------------ """


def circle_area_len(r):
    """
    根据圆的半径计算圆的周长
    :param r: 圆的半径
    :return: 圆的周长
    """
    return 2 * 3.14 * r


# circle_area_len(5)

""" ------------------------ 3.13 函数变量作用域 ------------------------ """

num = 10


def f1():

    num = 100
    print("f1-num1:", num)  # 100


# f1()
# print("global-num:", num)  # 10


def f2():
    # 表示要在函数中使用全局变量 num
    global num
    num = 100
    print("f2-num:", num)  # 100


# f2()

# print("global-num:", num)  # 100
