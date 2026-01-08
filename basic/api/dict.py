"""dict
- 特点
  - 使用键值对存储数据
  - 有序(从 Python 3.7 开始, 字典是有序的)
  - key 不可重复(如果重复, 后一个值会覆盖前一个值), 且必须是不可变类型(例如：字符串、数字、元组)
  - 可修改
- in 操作符
  - 用于检查元素是否存在于字典的键中。
- 实例方法
  - get(key): 返回指定键对应的值, 如果键不存在, 返回 None 或指定的默认值。
  - pop(key): 删除指定键的键值对, 并返回对应的值。
    - 使用 del 语句: del d1['a']
  - keys(): 返回字典中所有键的视图对象。
  - values(): 返回字典中所有值的视图对象。
  - items(): 返回字典中所有键值对的视图对象。
"""

""" ------------------------ 基础 ------------------------ """
def f1():
  d1 = {'a': 1, 'b': 2, 'c': 3}
  print('类型', type(d1)) # <class 'dict'> 

  # 定义空字典
  d2 = {}
  print('空字典1', d2) # {}
  d3 = dict()
  print('空字典2', d3) # {}

  # 获取值
  print('获取值1', d1['a']) # 1
  print('获取值2', d1.get('a')) # 1

  # 赋值
  d1['a'] = 100
  print('赋值', d1['a']) # 100

  print('所有键', d1.keys()) # dict_keys(['a', 'b', 'c'])
  print('所有值', d1.values()) # dict_values([100, 2, 3])
  print('所有键值对', d1.items()) # dict_items([('a', 100), ('b', 2), ('c', 3)])
  
# f1()

""" ------------------------ 遍历 ------------------------ """
def f2():
  d1 = {'a': 1, 'b': 2, 'c': 3}
  
  for key in d1.keys():
    print('键', key)

  for value in d1.values():
    print('值', value)
  
  for key, value in d1.items():
    print('键值对', key, value)
  
f2()
