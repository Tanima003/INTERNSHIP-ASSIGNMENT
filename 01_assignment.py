s=input('Enter a string: ')
n=int(input("enter the number"))
vowels=[ch for ch in s if ch in 'aeiouAEIOU']
if n>len(vowels):
    print("Number of vowels in the string is less than n")
else:
    print("First n vowels", vowels[:n])
