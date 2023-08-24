
nums = input().split()
set_nums = set()

for i in range(len(nums)):
     if nums[i].lstrip('0') not in set_nums:
          print('NO')
     else:
          print('YES')
     set_nums.add(nums[i].lstrip('0'))