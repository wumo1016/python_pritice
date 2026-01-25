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
    - 重写父类方法
        - 定义: 在子类中重新定义父类的方法, 从而实现对父类方法的重写
        - 特点
            - 方法名必须与父类的方法名相同
            - 参数列表必须与父类的方法参数列表相同(如果有默认值, 则可以不同)
            - 可以在子类中添加新的参数
- 多态
    - 含义
        - 同一个事物在不同场景下表现出不同的形态
        - python 中的多态是指, 同一个函数, 传入不同的对象, 可以表现出不同的行为
    - 三个条件
        - 继承关系: 子类必须继承自父类
        - 方法重写: 子类必须重写父类的方法
        - 父类引用: 父类引用指向子类对象
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

        def get_money(self, money):
            print("我从 Parent 类中获取了", money)

    class School:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 School", self.name)

    class Child2(Parent, School):
        def __init__(self, name):
            super().__init__(name)

        # 非重写
        # def get_money(self):
        #     pass

        # 重写父类方法
        def get_money(self, money):
            super().get_money(money)
            print("我从 Child2 类中获取了", money)

    child2_1 = Child2("李四")
    child2_1.say_hello()  # 你好, 我是 Parent 李四
    child2_1.get_money(
        100
    )  # 我从 Parent 类中获取了 100 元 我从 Child2 类中获取了 100 元
    print(
        Child2.__mro__
    )  # (<class '__main__.Child2'>, <class '__main__.Parent'>, <class '__main__.School'>, <class 'object'>)
    print(
        Child2.mro()
    )  # [<class '__main__.Child2'>, <class '__main__.Parent'>, <class '__main__.School'>, <class 'object'>]


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


# f4()

""" ------------------------ 单继承-私有属性和方法 ------------------------ """


def f5():
    class Parent:
        def __init__(self, name):
            self.name = name
            self.__age = 18

        def __say_hello(self):
            print("你好, 我是 Parent", self.name)

    class Child1(Parent):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self):
            super().__say_hello()

    child1_1 = Child1("张三")
    print(child1_1.name)  # 张三
    # print(child1_1.__age)  # AttributeError: 'Child1' object has no attribute '__age'
    child1_1.say_hello()  # AttributeError: 'Child1' object has no attribute '__say_hello'


# f5()

""" ------------------------ 多态 ------------------------ """


def f6():
    class Animal:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Animal")

    class Dog(Animal):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self):
            super().say_hello()
            print("你好, 我是 Dog", self.name)

    class Cat(Animal):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self):
            super().say_hello()
            print("你好, 我是 Cat", self.name)

    def say_hello_polymorphic(obj: Animal):
        obj.say_hello()

    dog1_1 = Dog("狗1")
    cat1_1 = Cat("猫1")

    say_hello_polymorphic(dog1_1)  # 你好, 我是 Animal 狗1 你好, 我是 Dog 狗1
    say_hello_polymorphic(cat1_1)  # 你好, 我是 Animal 猫1 你好, 我是 Cat 猫1


# f6()

""" ------------------------ 伪多态 ------------------------ """


def f7():
    class Animal:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Animal")

    class Dog(Animal):
        def __init__(self, name):
            super().__init__(name)

        def say_hello(self):
            super().say_hello()
            print("你好, 我是 Dog", self.name)

    class Phone:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print("你好, 我是 Phone", self.name)

    def say_hello_polymorphic(obj: Animal):
        obj.say_hello()

    dog1_1 = Dog("狗1")
    phone1_1 = Phone("手机1")

    say_hello_polymorphic(dog1_1)  # 你好, 我是 Animal 狗1 你好, 我是 Dog 狗1
    say_hello_polymorphic(phone1_1)  # 你好, 我是 Phone 手机1


f7()
