def fibo(n):
    """
    斐波那契额数列
    :param n:
    :return:
    """
    fibs = [0, 1]
    for i in range(n):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


fibo_list = fibo(5)
print(fibo_list)
print(fibo.__doc__)


def factorial(n):
    """
    递归使用， 阶乘函数
    :param n:
    :return:
    """
    ## 普通实现
    # result = n
    # for i in range(1, n):
    #     result *= i
    # return result

    ## 递归实现
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def search(sequence, number, lower, upper):
    """
    递归使用， 二分查找
    :param sequence:
    :param number:
    :param lower:
    :param upper:
    :return:
    """
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


# lambda 函数使用
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
result = reduce(lambda x, y: x + y, numbers)
print(result)


# 抽象是隐藏非必要的细节，通过定义处理细节的函数，让程序更抽象
