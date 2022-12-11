import os
# file = open(os.path.join(".","day1","sample.txt"))
file = open(os.path.join(".","day4","input.txt"))

counter_sub = 0

for line in file:
    splitLine = line.rstrip().split(",")

    # build elf one rooms
    elf_one = splitLine[0].split("-")
    # build elf two rooms
    elf_two = splitLine[1].split("-")

    # check if range is sub of another range
    if (
        (int(elf_one[0]) >= int(elf_two[0])
        and  int(elf_one[1]) <= int(elf_two[1]))
        or (int(elf_two[0]) >= int(elf_one[0])
        and  int(elf_two[1]) <= int(elf_one[1]))
    ):
        counter_sub += 1

print("counter sub: " + str(counter_sub))