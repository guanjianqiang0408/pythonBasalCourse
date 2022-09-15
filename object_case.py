# 创建自定义的类
# self指向实例对象本身

class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f"hi, my name is {self.name}")


person = Person()
person.set_name("zhangfei")
name = person.get_name()
print(name)
person.greet()

"""
方法（关联方法）将其第一个参数关联到它所属的实力，因此无需提供self参数
可以将属性关联到一个普通函数，但是这样就没有特殊的self参数
"""


class Class:

    def method(self):
        print("I have a self")


def function():
    print("I don't have a self")


# 隐藏方法和属性
class Secretive:

    def __inaccessible(self):
        """
        该函数外部是无法使用的
        :return:
        """
        print("Bet you can't see me")

    def accessible(self):
        """
        该函数外部是可以使用的
        :return:
        """
        print("The secret message is")
        self.__inaccessible()


s = Secretive()
s.accessible()


# 超类使用
class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    """
    该类直接从超类中继承了filter方法，所以不需要重新定义
    """
    def init(self):
        self.blocked = ["SPAM"]


f = Filter()
f.init()
result = f.filter([1, 2, 3])
print(result)

s = SPAMFilter()
s.init()
result = s.filter(["SPAM", "eggs", "bacon"])
print(result)

# 接口和内省,判断类是否有指定方法
print(hasattr(f, "filter"))
print(hasattr(f, "talk"))


# 抽象基类
from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        """
        子类继承抽象父类，必须重写方法
        :return:
        """
        pass


class Knigger(Talker):
    """
    如果子类继承抽象基类，没有重写抽象方法，会如下错误：
    TypeError: Can't instantiate abstract class Knigger with abstract method talk
    """
    def talk(self):
        pass


k = Knigger()
