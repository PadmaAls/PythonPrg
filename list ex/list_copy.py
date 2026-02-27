nums = [1, 2, 3, 4]
# print(nums)

nums[0] = 10
nums.append(50)
print(nums)

x = nums

x[1] = 20

# print(x)
# print(nums)

y = nums.copy()
y[2] = 30

print(x)
print(y)
print(nums)

z = nums
z[2] = 100



print(z)
print(nums)