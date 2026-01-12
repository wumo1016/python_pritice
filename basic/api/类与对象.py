"""类
- 特点
  - 命名规范: 类名采用大驼峰命名法(每个单词的首字母大写, 不使用下划线)
- 实例属性
  - __dict__: 实例属性的字典(以字典的形式存储所有实例属性)
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

""" ------------------------ 初始化方法 ------------------------ """
def f2():
    # 定义类
    class MyClass:
        # self 代表实例对象本身
        def __init__(self, name):
            self.name = name

    # 实例化类
    my_obj = MyClass("张三")
    print(my_obj.name)
f2()
