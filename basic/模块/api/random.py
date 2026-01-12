"""random
- 方法
  - randint(下限, 上限): 返回一个随机整数，范围包括下限和上限。
  - choice(序列): 从序列中随机选择一个元素。
  - choices(序列, k=数量): 从序列中随机选择多个元素，返回一个列表。
  
  - seed(种子): 设置随机数种子，用于生成可重复的随机数序列。
  - shuffle(序列): 随机打乱序列中的元素。
  - uniform(下限, 上限): 返回一个随机浮点数，范围包括下限和上限。
  - normalvariate(均值, 标准差): 返回一个符合正态分布的随机浮点数。
  - expovariate(率): 返回一个符合指数分布的随机浮点数。
  - gammavariate(形状参数, 尺度参数): 返回一个符合伽马分布的随机浮点数。
  - betavariate(alpha, beta): 返回一个符合贝塔分布的随机浮点数。
  - paretovariate(形状参数): 返回一个符合帕累托分布的随机浮点数。
  - weibullvariate(形状参数, 尺度参数): 返回一个符合韦伯分布的随机浮点数。
  - lognormvariate(均值, 标准差): 返回一个符合对数正态分布的随机浮点数。
  - vonmisesvariate(均值, 标准差): 返回一个符合 von Mises 分布的随机浮点数。
"""

import random


""" ------------------------ 定义方式 ------------------------ """
def test1():
    print(random.randint(1, 10))
    print(random.choice([1, 2, 3, 4, 5]))
    print(random.choices([1, 2, 3, 4, 5], k=2))