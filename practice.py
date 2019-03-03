import math

result = math.pow(2, 3)
print(result)

import random
result = random.randint(0, 100)
print(result)

import statistics
nums = [1, 5, 33, 12, 46, 33, 2]
mean = statistics.mean(nums)
median = statistics.median(nums)
mode = statistics.mode(nums)
print(mean)
print(median)
print(mode)

import keyword
a = keyword.iskeyword("for")
b = keyword.iskeyword("football")
print(a)
print(b)
