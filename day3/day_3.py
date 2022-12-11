import os
# file = open(os.path.join(".","day1","sample.txt"))
file = open(os.path.join(".","day3","input.txt"))

total = 0 
for line in file:
    first, last = line[:len(line)//2], line[len(line)//2:]
    common_letters = list(set(first) & set(last))
    for letter in common_letters:
        asc_value = ord(letter)
        if(asc_value >= 97):
            total += (asc_value - 96)
        else:
            total += (asc_value - 38)

print(total)