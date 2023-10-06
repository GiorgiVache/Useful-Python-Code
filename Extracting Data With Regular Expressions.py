import re

hand = open("regex_sum_1767530.txt")
listnums = []
for line in hand:
    new_line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    if len(nums) > 0:
        for num in nums:
            listnums.append(int(num))

sum = 0
for num in listnums:
    sum = sum + num

print(sum)
