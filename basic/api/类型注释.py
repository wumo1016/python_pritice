"""类型注释
- 简介
  - 类型注释是指在变量、函数参数、函数返回值等地方添加的类型提示。
"""

""" ------------------------ 基础 ------------------------ """


def f1():
    # 字符串
    s1: str = "hello world"
    print(s1)
    # 整数
    i1: int = 123
    print(i1)
    # 浮点数
    f1: float = 12.34
    print(f1)
    # 布尔值
    b1: bool = True
    print(b1)
    # 列表
    list1: list[int | str] = [1, 2, 3, 4, 5]
    print(list1)
    # 元组
    tuple1: tuple[int, ...] = (1, 2, 3, 4, 5)
    print(tuple1)
    # 字典
    dict1: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    print(dict1)
    # 集合
    set1: set = {1, 2, 3, 4, 5}
    print(set1)
    # 空值
    none1: None = None
    print(none1)

    # 函数
    def f2(a: int, b: int) -> int:
        return a + b

    print(f2(1, 2))  # 3


f1()
