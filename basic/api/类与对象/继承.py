"""类
- 继承
    - 定义: 子类可以继承父类的属性和方法, 从而实现代码的复用
    - 分类
        - 单继承: 子类只能继承一个父类
        - 多继承: 子类可以继承多个父类
            - 如果多个父类中存在相同的属性或方法, 则按照继承顺序查找(从左到右)
            - __mro__: 方法解析顺序(Method Resolution Order)属性, 可以查看类的继承顺序
            - mro(): 方法解析顺序(Method Resolution Order)方法, 可以查看类的继承顺序
    - 调用父类方法
      - 父类.方法名(self, 参数) - 常用于多继承, 调用父类的方法
      - super().方法名(参数) - 常用于单继承(如果是多继承, 则调用第一个父类的方法)
"""

""" ------------------------ 单继承 ------------------------ """
def f1():
    class Parent:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Parent", self.name)

    class Child1(Parent):
        def __init__(self, name):
            super().__init__(name)

    child1_1 = Child1("张三")
    print(child1_1.name)  # 张三
# f1()

""" ------------------------ 多继承 ------------------------ """
def f2():
    class Parent:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Parent", self.name)

    class School:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 School", self.name)
    class Child2(Parent, School):
        def __init__(self, name):
            super().__init__(name)

    child2_1 = Child2("李四")
    child2_1.say_hello()  # 你好, 我是 Parent 李四
    print(Child2.__mro__)  # (<class '__main__.Child2'>, <class '__main__.Parent'>, <class '__main__.School'>, <class 'object'>)
    print(Child2.mro())  # [<class '__main__.Child2'>, <class '__main__.Parent'>, <class '__main__.School'>, <class 'object'>]
# f2()

""" ------------------------ 单继承-重写父类方法 ------------------------ """
def f3():
    class Parent:
        def __init__(self, name):
            self.name = name

        def say_hello(self, msg):
            print("你好, 我是 Parent", self.name, msg)

    class Child1(Parent):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self, msg):
            # 方式1
            super().say_hello(msg)
            # 方式2
            Parent.say_hello(self, msg)

            print("你好, 我是 Child1", self.name, msg)

    child1_1 = Child1("张三")
    child1_1.say_hello("你好")  # 你好, 我是 Parent 张三 你好
# f3()

""" ------------------------ 多继承-重写父类方法 ------------------------ """
def f4():
    class Parent:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Parent", self.name)

    class School:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 School", self.name)

    class Child2(Parent, School):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self):
            # 方式1
            super().say_hello()  # 你好, 我是 Parent 李四
            # 方式2
            Parent.say_hello(self)  # 你好, 我是 Parent 李四
            School.say_hello(self)  # 你好, 我是 School 李四

            print("你好, 我是 Child2", self.name)  # 你好, 我是 Child2 李四

    child2_1 = Child2("李四")
    child2_1.say_hello() 
f4()
