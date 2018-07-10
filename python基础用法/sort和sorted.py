# 1.使用sort排序

my_list = [3,2,5,6,7,8,1]

my_list.sort()

print(my_list)
# 使用sort()方法对list排序会修改list本身,不会返回新list,
# 通常此方法不如sorted()方便，但是如果你不需要保留原来的list，此方法将更有效sort()。

# 2.使用sorted()排序,不会改变原来的

you_list = [3,2,5,6,7,8,1]
result = sorted(you_list)
print(you_list)
print(result)

#字典排序，默认key值进行排序
my_dict = {"a":"1", "c":"3", "b":"2"}
result_dict = sorted(my_dict)
print(result_dict)