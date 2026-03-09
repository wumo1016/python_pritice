"""闭包
- 简介
  - 闭包是指在一个函数内部定义的函数，并且该内部函数可以访问外部函数的变量。
  - nonlocal 关键字可以在内部函数中修改外部函数的变量
"""

""" ------------------------ 基础 ------------------------ """
def f1():
    def outer(num1):
        def inner(num2):
            return num1 + num2
        return inner
    o1 = outer(10)
    print(o1(20))  # 30
# f1()

""" ------------------------ nonlocal ------------------------ """
def f2():
    def outer(num1):
        def inner(num2):
            nonlocal num1
            num1 += num2
            return num1
        return inner
    o1 = outer(10)
    print(o1(20))  # 30
    print(o1(30))  # 60
f2()
