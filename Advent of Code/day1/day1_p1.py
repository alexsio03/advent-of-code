file = open("day1_input.txt", "r")
lines = file.readlines()

total = 0
for line in lines:
    first = 0 
    last = 0
    check = True
    for i in range(len(line)):
        if line[i].isdigit():
            if check:
                first = line[i]
                check = False
            last = line[i]
    num = first + last
    total += int(num)
print(total)
file.close()