"""装饰器
- 简介
  - 装饰器是一种在函数或类定义之前添加额外功能的机制。
- 备注
  - 内部函数(inner)必须和原函数(被装饰的函数)的参数和返回值类型保持一致
"""

""" ------------------------ 基础 ------------------------ """
def f1():
    # 装饰器的写法1
    def comment():
        print("发表评论")

    def check_login(func):
        def inner():
            print("检查登录状态")
            func()
        return inner
 
    comment1 = check_login(comment)
    comment1()

    # 装饰器的写法2
    @check_login
    def comment2():
        print("发表评论")
    comment2()
# f1()

""" ------------------------ 有参有返回值装饰器 ------------------------ """
def f2():
    def check_login(func):
        def inner(num):
            print("检查登录状态")
            return func(num)
        return inner

    @check_login
    def comment1(num):
        print(f"评论数量={num}")
        return num
        
    print(comment1(2))

# f2()

""" ------------------------ 可变参数装饰器 ------------------------ """
def f3():
    """ 装饰器的写法1 """

    def check_login(func):
        def inner(*args, **kwargs):
            print("检查登录状态")
            return func(*args, **kwargs)
        return inner

    @check_login
    def comment1(num, price):
        print(f"评论数量={num}, 价格={price}")
        
    comment1(2, 100)

# f3()

""" ------------------------ 多个装饰器装饰一个函数 ------------------------ """
def f4():

    def check_login(func):
        def inner(*args, **kwargs):
            print("检查登录状态")
            return func(*args, **kwargs)
        return inner

    def check_price(func):
        def inner(*args, **kwargs):
            print("检查价格")
            return func(*args, **kwargs)
        return inner


    # 传统写法(执行从外到内)
    def comment1(num, price):
        print(f"评论数量={num}, 价格={price}")
    
    comment1 = check_login(check_price(comment1))
    comment1(2, 100)

    # 装饰器的写法2(从上到下执行)
    @check_login
    @check_price
    def comment2(num, price):
        print(f"评论数量={num}, 价格={price}")
        
    comment2(2, 100)

f4()

