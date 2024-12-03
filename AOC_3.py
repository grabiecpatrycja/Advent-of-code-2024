import re

#part_1
mull_1 = 0
with open("input_3.txt") as file:
    data = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.finditer(pattern,data)

    for match in matches:
        elements = re.split(r"[\(\),]",match.group())
        mull_1 += int(elements[1]) * int(elements[2])

print(mull_1)


#part_2
mull_2 = 0
with open("input_3.txt") as file:
    data = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern,data)

    flag = True
    for match in matches:
        if match.group() == "do()":
            flag = True
        elif match.group() == "don't()":
            flag = False
        elif match.group not in ["do()", "don't()"] and flag == True:
            elements = re.split(r"[\(\),]",match.group())
            mull_2 += int(elements[1]) * int(elements[2])

print(mull_2)