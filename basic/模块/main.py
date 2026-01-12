"""模块
- 导入方式
  - import 模块名[, 模块名2, ...]
    - 例如: import math
    - 调用: math.函数名()
  - import 模块名 as 别名
    - 例如: import math as m
    - 调用: m.sqrt(9)  # 3.0
  - from 模块名 import 函数名[, 函数名2, 变量名, ...]
    - 例如: from math import sqrt
    - 调用: sqrt(9)  # 3.0
  - from 模块名 import 函数名 as 别名
    - 例如: from math import sqrt as s
    - 调用: s(9)  # 3.0
  - from 模块名 import *
    - 例如: from math import *
    - 调用: sqrt(9)  # 3.0
- 内置模块
  - math: 数学计算
  - random: 随机数
  - time: 时间
  - calendar: 日历
  - datetime: 日期时间
  - os: 操作系统
  - sys: 系统参数
  - csv: CSV 文件操作函数
  - re: 正则表达式函数
- 自定义模块
  - 模块的导入
  - 模块的使用
- 内置变量
  - __name__: 当前模块的名称
    - 自身运行时: __name__ == '__main__'
    - 被导入时: __name__ == '模块名'
  - __all__: 模块的公开接口(只影响 from 模块名 import *)
    - 例如: __all__ = ['sum']
    - 调用: from test1 import * 导入的只有 sum 函数
 """

""" ------------------------ 导入1 ------------------------ """
# import test1

# print(test1.sum(1, 2))  # 3

""" ------------------------ 导入2 ------------------------ """
# from test1 import mul, div

# print(mul(2, 3))  # 6
# print(div(6, 3))  # 2.0

""" ------------------------ 导入3 ------------------------ """
from test1 import *

print(sum(2, 3))  # 5
print(sub(6, 3))  # 3