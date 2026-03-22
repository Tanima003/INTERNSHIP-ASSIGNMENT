list = [1, 2, 4, 7]
missing_sum = 0
for i in range(min(list), max(list)+1):
    if i not in list:
        missing_sum += i
print("missing sum is", missing_sum)