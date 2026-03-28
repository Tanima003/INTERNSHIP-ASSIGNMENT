list = [1,2,4,6,7,8]
index = 2
total = 0
for i in range (len(list)):
    if i != index:
        total += list[i]
print("the total is:", total)
result = str(total)
print("the total result is ", result)
