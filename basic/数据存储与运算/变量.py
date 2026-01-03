"""
- 简介
  - 变量是指在程序运行过程中可以改变其值的量。
"""


def f1():
    s1 = 123
    print(s1)
    s1 = "hello world"
    print(s1)


# f1()


# 一次性定义多个变量
def f2():
    s1, s2 = 123, "hello world"
    print(s1)
    print(s2)


f2()
