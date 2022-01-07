import re

handle = open("regex_sum_1235853.txt")
number = []
counter = 0
for line in handle:
    line = line.rstrip()
#    print(line)
    find = re.findall("[0-9]+", line)
#    print(find)
    if len(find) > 0 :
        number = number + find
#    print(number)
total = 0
for no in number:
    no = int(no)
    total = total + no
    counter += 1
#    print(counter)
print(total)