# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:-
# X-DSPAM-Confidence: 0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

#fname = input("Enter file name: ")
#fh = open(fname)
#count_sum = 0
#count_number = 0
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence: "):
#        continue
#    colon_position = line.find(':')
#    value = line[colon_position+1:]
#    new_value = float(value)
#    count_sum = count_sum + new_value
#    count_number = count_number + 1
#print("Average spam confidence: ", count_sum/count_number)


fname = input("Enter file name: ")
fh = open(fname)
count_total = 0
count_line = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    stripped_line = line.strip("X-DSPAM-Confidence: ")
    count_total = count_total + float(stripped_line) 
    count_line = count_line + 1
print("Average spam confidence:", count_total/count_line)
