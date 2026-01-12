"""包
- 介绍
  - 本质就是一个文件夹，文件夹中可以包含多个模块
  - 文件夹中必须包含一个 __init__.py 文件
- 导入方式
  - import 包名.模块名
    - 例如: import utils.my_fun
    - 调用: utils.my_fun.sum(1, 2)  # 3
  - from 包名 import 模块名
    - 例如: from utils import my_fun
    - 调用: my_fun.sum(1, 2)  # 3
  - from 包名.模块名 import 函数名[, 函数名2, 变量名, ...]
    - 例如: from utils.my_fun import sum
    - 调用: sum(1, 2)  # 3
  - from 包名 import *
    - 例如: from utils import *
    - 调用: my_fun.sum(1, 2)  # 3
    - 注意: 需要在 __init__.py 文件中定义 __all__ 变量
  - from 包名.模块名 import *
    - 例如: from utils.my_fun import *
    - 调用: sum(1, 2)  # 3
"""

""" ------------------------ 导入1 ------------------------ """
# import utils.my_fun

# print(utils.my_fun.sum(1, 2))  # 3

""" ------------------------ 导入2 ------------------------ """
# from utils import * 

# print(my_fun.sum(1, 2))  # 3
