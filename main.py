nums = [3, 8, 1, 9, 4, 7, 2, 6, 5, 0]
n = len(nums)

for i in range(n // 2):
    temp = nums[i]
    nums[i] = nums[n - 1 - i]
    nums[n - 1 - i] = temp

print(nums)