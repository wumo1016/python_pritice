"""装饰器
- 简介
  - 装饰器是一种在函数或类定义之前添加额外功能的机制。
- 备注
  - 内部函数(inner)必须和原函数(被装饰的函数)的参数和返回值类型保持一致
"""
S
""" ------------------------ 基础 ------------------------ """
def f1():
    """ 装饰器的写法1 """
    def comment():
        print("发表评论")

    def check_login(func):
        def inner():
            print("检查登录状态")
            func()
        return inner
 
    comment1 = check_login(comment)
    comment1()

    """ 装饰器的写法2 """
    @check_login
    def comment2():
        print("发表评论")
    comment2()
f1()
