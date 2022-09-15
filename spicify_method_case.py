# 构造函数 对象创建后会自动调用构造函数
class FooBar:
    def __init__(self):
        """
        构造函数， 对象实例化后自动调用的函数
        """
        self.somevar = 42

    def __del__(self):
        """
        析构函数， 对象被销毁前调用
        :return:
        """


f = FooBar()
print(f.somevar)


class ChildBar(FooBar):
    """
    继承父类Foobar
    """
    def __init__(self):
        """
        重写父类函数
        """
        super().__init__()
        self.somevar = 40


c = ChildBar()
print(c.somevar)


# list dicr str派生
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)


c1 = CounterList(range(10))
print(c1)
print(c1.counter)


# 特性
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height


r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size())


# 静态、类方法, 都可以被类直接调用，而不需要实例化类对象
class MyClass:
    @staticmethod
    def smeth():
        print("this is staticmethod")

    @classmethod
    def cmeth(cls):
        print("this is classmethod")


MyClass.smeth()
MyClass.cmeth()


# 迭代器使用
class Fibos:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibos = Fibos()
for f in fibos:
    if f > 1000:
        print(f)
        break


# 使用构造函数list显示将迭代器转换为列表
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti =TestIterator()
print(list(ti))

# 生成器
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


# 获取生成器的所有值
for num in flatten(nested):
    print(num)


# 生成器推导式
g = ((item + 2) ** 2 for item in range(2, 27))
print(next(g))


# 递归生成器
def recursive_generate(nested):
    try:
        for sublist in nested:
            for element in recursive_generate(sublist):
                yield element
    except TypeError:
        yield nested


print(list(recursive_generate([[[1], 2], 3, 4, [5, [6, 7]], 8])))

# 八皇后
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


import random
prettyprint(random.choice(list(queens(8))))