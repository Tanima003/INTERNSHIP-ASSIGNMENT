list = [2,4,7,9,12,1,20,34,15,19,21,31]
list.sort()
print("sort list is:", list)
max_odd = None
for num in list:
    if num %2 != 0:
        if max_odd is None or num > max_odd:
            max_odd = num
if max_odd is not None:
        print("maximum odd number is:", max_odd)
else:
        print("no odd number found")