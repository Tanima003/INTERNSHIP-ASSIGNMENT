list=[1,7,9,10,3,20,15,19]
list.sort()
print("sort list is:", list)
gaps = [list[i+1]-list[i] for i in range(len(list)-1)]
max_gaps=max(gaps)
print("maximum gaps is:", max(gaps))
min_gaps=min(gaps)
print("minimum gaps is:", min(gaps))