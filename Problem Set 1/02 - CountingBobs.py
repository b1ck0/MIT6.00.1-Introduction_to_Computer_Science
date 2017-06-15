# This script counts and retunrs the number of "bob"s in the variable s

s = 'azcbobobegghakl'

count = 0
itr = 0
while itr <= len(s)-3:
    if s[itr] + s[itr+1] + s[itr+2] == 'bob':
        count += 1
        itr += 1
    else:
        itr += 1
        continue
print("Number of times bob occurs is: " + str(count))