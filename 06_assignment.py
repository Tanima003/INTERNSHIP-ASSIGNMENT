list = ["internship", "python", "ambiguous", "student"]
count = 0
for word in list:
    for ch in word:
        if ch.islower():
            count += 1  
print("the total number of words is:", count)