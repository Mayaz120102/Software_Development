#set : unique items collection  {}

nums = [12, 56, 98,78, 56, 12, 89 ]
# print(nums)

nums_set = set(nums)
# print(nums_set)

nums_set.add(55)
# print(nums_set)

# union
a = {1,3,4,5,6,7}
b = {1,2,3,4,7}
print(a&b)
print(a|b)