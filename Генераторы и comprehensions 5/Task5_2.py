# №2
n = 20
nums_gen = (nums for nums in range(1, n + 1) if nums % 2 == 1)
print(*nums_gen)
print(type(nums_gen))
