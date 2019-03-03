import random
import statistics

num_list = []
for i in range(0, 20):
    num = random.randint (0,100)
    num_list.append(num)

print(num_list)
mean = statistics.mean(num_list)
median = statistics.median(num_list)
pstdev = statistics.pstdev(num_list)
stdev = statistics.pstdev(num_list)
print("平均値：")
print(mean)
print("中央値：")
print(median)
print("母標準偏差：")
print(pstdev)
print("標本標準偏差：")
print(stdev)
