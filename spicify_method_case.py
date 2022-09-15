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
    """
    函数conflict接受（用状态元组表示的）既有皇后的位置，并确定下一个皇后的位置是否会导致冲突
    参数nextX表示下一个皇后的水平位置（x坐标，即列），而nextY为下一个皇后的垂直位置（y坐标，即行）。这个函数对既有的每个皇后执行简单的检查：
    如果下一个皇后与当前皇后的x坐标相同或在同一条对角线上，将发生冲突，因此返回True；如果没有发生冲突，就返回False
    :param state:
    :param nextX:
    :return:
    """
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    """
    基线条件：最后一个皇后。对于这个皇后，你想如何处理呢？假设你想找出所有可能的解——给定其他皇后的位置，可将这个皇后放在什么位置（可能什么位置都不行）
    这段代码的意思是，如果只剩下最后一个皇后没有放好，就遍历所有可能的位置，并返回那些不会引发冲突的位置。参数num为皇后总数，而参数state是一个元组，包含已放好的皇后的位置
    :param num:
    :param state:
    :return:
    """
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    """
    输出更容易理解些。在任何情况下，清晰的输出都是好事，因为这让查找bug等工作更容易
    :param solution:
    :return:
    """
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


import random
prettyprint(random.choice(list(queens(8))))