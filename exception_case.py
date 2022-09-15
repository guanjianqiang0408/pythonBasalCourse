# 异常捕获
try:
    print(1/0)
except ZeroDivisionError:
    print("the second number can't be zero")
# 多个exception
except Exception:
    print("lastes wrap exception")
except (ZeroDivisionError, Exception):
    print("mutiple exception")


# 完整异常处理
try:
    # 代码块
    pass
except:
    # 发生异常处理的代码块
    pass
else:
    # 无异常处理的代码块
    pass
finally:
    # 无论是否有异常都处理的代码块
    pass

# 警告
from warnings import warn, filterwarnings
warn("this is warning")



# 自定义异常类
class CustomerException(Exception):
    """ Common base class for all non-exit exceptions. """

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass
