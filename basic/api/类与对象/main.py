"""类
- 特点
  - 命名规范: 类名采用大驼峰命名法(每个单词的首字母大写, 不使用下划线)
- 私有属性和方法
  - 定义: 在属性名或方法名前添加双下划线(例如: __name、__age、__say_hello() 等)
  - 调用: 只能在类的内部调用(例如: self.__name、self.__say_hello() 等)
  - 特点: 不会被子类继承(例如: 父类有 __name 属性, 子类无法直接访问 __name 属性)
- 类属性(静态属性)
  - 定义: 在类中定义的变量, 所有实例对象共享
  - 调用: 类名.属性名
  - 修改: 类名.属性名 = 值(通过 实例.属性名 无法修改)
- 类方法
  - 定义: 在类中定义的函数, 不需要实例化类就可以调用
    - @classmethod 装饰器
    - 第一个参数必须是 cls(相当于类本身)
  - 调用: 类名.方法名()
- 静态方法
  - 定义: 在类中定义的函数, 不需要实例化类就可以调用
    - @staticmethod 装饰器
    - 无参数要求
  - 调用: 类名.方法名()
- 实例属性
  - 定义: 在类中定义的变量, 每个实例对象都有自己的属性值
    - 可以在类中定义, 也可以在实例化类时动态添加(通过 实例.属性名 = 值 来添加)
  - 调用: 实例对象.属性名(优先查找实例属性, 没有则查找类属性)
  - 例如
    - __dict__: 实例属性的字典(以字典的形式存储所有实例属性)
- 实例方法
  - 定义: 在类中定义的函数, 第一个参数必须是 self(代表实例对象本身)
  - 调用: 实例对象.方法名()
- 魔法方法
  - 简介
    - 魔法方法是指在类中定义的特殊方法, 它们以双下划线开头和结尾(例如: __init__、__str__、__eq__ 等)
    - 它们的作用是在特定的情况下自动调用, 无需手动调用
  - 例如
    - __init__: 初始化方法(在实例化类时自动调用)
    - __str__: 字符串表示方法(在使用 print() 函数时自动调用)
    - __eq__: 等于方法(在使用 == 运算符时自动调用)
    - __lt__: 小于方法(less than)(在使用 < 运算符时自动调用)
    - __le__: 小于等于方法(less than or equal)(在使用 <= 运算符时自动调用)
    - __gt__: 大于方法(greater than)(在使用 > 运算符时自动调用)
    - __ge__: 大于等于方法(greater than or equal)(在使用 >= 运算符时自动调用)
    - __del__: 删除方法(在删除实例对象时自动调用)
"""

""" ------------------------ 基础 ------------------------ """


def f1():
    # 定义类
    class MyClass:
        pass

    # 实例化类
    my_obj = MyClass()
    print(my_obj)  # <__main__.MyClass object at 0x101234567>
    # 动态添加属性
    my_obj.name = "张三"
    print(my_obj.name)  # 张三
    print(my_obj.__dict__)  # {'name': '张三'}


# f1()

""" ------------------------ 初始化方法, 实例属性 ------------------------ """


def f2():
    # 定义类
    class MyClass:
        # self 代表实例对象本身
        def __init__(self, name):
            self.name = name

    # 实例化类
    my_obj = MyClass("张三")
    print(my_obj.name)


# f2()

""" ------------------------ 实例化方法 ------------------------ """


def f3():
    # 定义类
    class MyClass:
        # self 代表实例对象本身
        def __init__(self, name):
            self.name = name

        # 实例方法
        def say_hello(self):
            print("你好,", self.name)

    my_obj = MyClass("张三")
    my_obj.say_hello()  # 你好, 张三


# f3()

""" ------------------------ 魔法方法 ------------------------ """


def f4():
    # 定义类
    class MyClass:
        # self 代表实例对象本身
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
            return f"{self.name}的价格是{self.price}"

        def __eq__(self, other):
            return self.price == other.price

        def __lt__(self, other):
            return self.price < other.price

        def __le__(self, other):
            return self.price <= other.price

        def __gt__(self, other):
            return self.price > other.price

        def __ge__(self, other):
            return self.price >= other.price

        def __del__(self):
            print(f"{self.name}被删除了")

    my_obj1 = MyClass("张三", 100)
    my_obj2 = MyClass("李四", 200)

    print(my_obj1)  # 张三的价格是100
    print(my_obj2)  # 李四的价格是200

    print(my_obj1 == my_obj2)  # False
    print(my_obj1 != my_obj2)  # True

    print(my_obj1 < my_obj2)  # True
    print(my_obj1 <= my_obj2)  # True
    print(my_obj1 > my_obj2)  # False
    print(my_obj1 >= my_obj2)  # False


# f4()

""" ------------------------ 类属性(静态属性) ------------------------ """


def f5():
    # 定义类
    class MyClass:
        # 类属性
        count = 0

        # self 代表实例对象本身
        def __init__(self, name):
            self.name = name

    my_obj = MyClass("张三")
    print(my_obj.count)  # 0
    my_obj.count += 1
    print(MyClass.count)  # 0
    MyClass.count += 1
    print(MyClass.count)  # 1
    print(my_obj.count)  # 1


# f5()

""" ------------------------ 类方法&静态方法 ------------------------ """


def f6():
    # 定义类
    class MyClass:
        # self 代表实例对象本身
        def __init__(self, name):
            self.name = name

        #  cls === MyClass
        @classmethod
        def say_hello(cls):
            print("你好, 类方法")

        @staticmethod
        def say_hello3():
            print("你好, 静态方法")

        # 实例方法
        def say_hello2(self):
            print("你好,", self.name)

    my_obj = MyClass("张三")

    MyClass.say_hello()  # 你好, 类方法
    my_obj.say_hello2()  # 你好, 张三
    MyClass.say_hello3()  # 你好, 静态方法


f6()
