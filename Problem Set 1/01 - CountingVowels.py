# This script counts and returns the number of volwels in the variable s
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = 'azcbobobegghakl'

count = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1
    else:
        continue
 
print("Number of vowels: " + str(count))