
"""After creating in windows environ vairables use below  to gain access"""

# import os

# path = os.getenv("Path")

# print(path)



"""Command to create and Environmental Variables on LINUX"""

# export MY_DB_URL="Localhost:5432"
# printenv
# echo $MY_DB_URL


def find_max(nums):
    max_num = float("-inf")
    
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

nums = (3,2,1)
print(find_max(nums))