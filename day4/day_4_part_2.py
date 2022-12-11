# file = open(".\day4\sample.txt")
file = open(".\day4\input.txt")

counter_overlap = 0

for line in file:
    splitLine = line.rstrip().split(",")

    # build elf one rooms
    elf_one = splitLine[0].split("-")
    # build elf two rooms
    elf_two = splitLine[1].split("-")

    # check if range overlaps
    if (
        (int(elf_one[0]) <= int(elf_two[1])
        and  int(elf_two[0]) <= int(elf_one[1]))
        or (int(elf_two[0]) <= int(elf_one[1])
        and  int(elf_one[0]) <= int(elf_two[1]))
    ):
        counter_overlap += 1

print("counter overlap: " + str(counter_overlap))