# file = open("./day3/sample.txt")
file = open("./day3/input.txt")

total = 0 
lines = []
for line in file:
    lines.append(line.rstrip())
    if len(lines) == 3:
        common_letters = list(set(lines[0]) & set(lines[1]) & set(lines[2]))
        for letter in common_letters:
            asc_value = ord(letter)
            if(asc_value >= 97):
                total += (asc_value - 96)
            else:
                total += (asc_value - 38)
        lines = []
print(total)