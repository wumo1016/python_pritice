"""
- 简介
  - 在代码中为变量、函数、类等元素所起的名称。
- 命名规范
  - 多个单词使用下划线连接
  - 英文字母全部小写
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
