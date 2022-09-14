# simple infer list
a = [item for item in range(0, 3)]
b = [item for item in range(3, 6)]
print(a, b)
# double infer list
c = [i1 + i2 for i1 in a for i2 in b]
print(c)

# condition infer list
d = [item for item in c if item > 3]
print(d)

# 将字符串作为代码执行
exec("print('Hello world')")

# 执行一系列python语句
print(eval("2 + 18 * 2"))