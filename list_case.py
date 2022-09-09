# 声明一个列表
new_list = list()
print(new_list)
# 向列表添加元素1
new_list.append(1)
print(new_list)
# 列表追加另外一个列表[2, 3, 4]
new_list.extend([2, 3, 4])
print(new_list)
# 删除列表中的索引为3的元素
new_list.remove(3)
print(new_list)
# 列表拼接
new_list = new_list + [5, 6, 7]
print(new_list)
# 列表切片，步长为2
slice_list = new_list[::2]
print(slice_list)
# 列表反转
reverse_list = new_list[::-1]
print(reverse_list)
# 清空列表
reverse_list.clear()
print(reverse_list)
# 复制列表
copy_list = new_list.copy()
copy_list2 = new_list[:]
print(copy_list)
print(copy_list2)

# 查看元素出现次数
list_count = copy_list.count(1)
print(list_count)

# 查看列表元素所以位置
index_local = copy_list.index(2)
print(index_local)

# 指定位置插入元素
copy_list.insert(0, 8)
print(copy_list)

# 列表排序
copy_list.sort()
print(copy_list)