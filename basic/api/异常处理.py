"""异常处理
- 语法
  - try:
    - 可能会出错的代码
  - except [异常类型1 as e1, 异常类型2 as e2, ...]:
      - 不写异常类型, 表示捕获所有异常
      - 出错时执行的代码
  - finally:
      - 无论是否出错, 都会执行的代码
      - 可选
- 错误类型  
  - Exception: 所有异常的基类
  - TypeError: 类型错误(例如: 1 + "a")
  - NameError: 变量未定义错误(例如: a + b)
  - IndexError: 索引错误(例如: [1, 2, 3][4])
  - KeyError: 键错误(例如: {"a": 1, "b": 2}["c"])
  - AttributeError: 属性错误(例如: "a".upper())
  - ValueError: 数值转换错误(例如: int("a"))
  - ZeroDivisionError: 除0错误(例如: 8 / 0)
"""

""" ------------------------ 基础使用 ------------------------ """
def f1():
    try:
        # 可能会出错的代码
        num = int(input("请输入一个整数: "))
        result = 8 / num
        print(result)
    except ValueError as e1:
        # 出错时执行的代码
        print("请输入一个整数:", e1)
    except ZeroDivisionError:
        # 出错时执行的代码
        print("除0错误:")
    finally:
        # 无论是否出错, 都会执行的代码
        print("程序结束")

# f1()

""" ------------------------ 捕获所有 ------------------------ """
def f2():
    try:
        # 可能会出错的代码
        num = int(input("请输入一个整数: "))
        result = 8 / num
        print(result)
    # 不带参数
    # except:
    #     print("请输入一个整数:")

    # 带参数
    except Exception as e:
        print("请输入一个整数:", e)

    finally:
        # 无论是否出错, 都会执行的代码
        print("程序结束")

f2()