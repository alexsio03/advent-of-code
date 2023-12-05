file = open("day1_input.txt", "r")
lines = file.readlines()    

numvals = {"one": "1", "two": "2", "three": "3",
           "four": "4", "five": "5", "six": "6",
           "seven": "7", "eight": "8", "nine": "9"}

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
        for key in numvals:
            if key in line[i:i+len(key)]:
                if check:
                    first = numvals[key]
                    check = False
                last = numvals[key]
    print(first, last)
    num = first + last
    total += int(num)
print(total)
file.close()