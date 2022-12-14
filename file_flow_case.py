# 打开文件
f = open("./test.txt", 'w', encoding='utf-8')
# 写文件
f.write("this my first text\n")
f.close()
f = open("./test.txt", 'r', encoding='utf-8')
# 读文件
print(f.read())
# 关闭文件
f.close()

# 文件的上下文管理器,使用上下文管理器，不再需要手动关闭文件
with open("./test.txt") as f:
    # 读取一行文件内容， 如果逐行读取文件内容请使用readlines
    print(f.readline())

# seek跳转文件行数读取文件内容