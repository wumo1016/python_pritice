"""变量
- 简介
  - 变量是指在程序运行过程中可以改变其值的量。
"""


""" ------------------------ 基础 ------------------------ """
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


# f2()

""" ------------------------ 查看变量类型 type isinstance ------------------------ """
def f3():
    s0 = 123
    print(type(s0))  # <class 'int'>
    print(isinstance(s0, int))  # True

    s1 = 1.25
    print(type(s1))  # <class 'float'>
    print(isinstance(s1, float))  # True

    s2 = "hello world"
    print(type(s2))  # <class 'str'>
    print(isinstance(s2, str))  # True

    s3 = True
    print(type(s3))  # <class 'bool'>
    print(isinstance(s3, bool))  # True

    s4 = None
    print(type(s4))  # <class 'NoneType'>

f3()