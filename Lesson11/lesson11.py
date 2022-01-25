# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file_name = input("Enter File: ")
if len(file_name) < 1 : file_name = "mbox-short.txt"
handle = open(file_name)

dic = dict()
for line in handle:
    line = line.rstrip()
#    print(line)

    words = line.split()
#    print(words)
    if line == "" or words[0] != "From" : continue
#    print(words)

    time = words[5]
#    print(time)

    splitted_time = time.split(":")
#    print(splitted_time)

    hour = splitted_time[0]
#    print(hour)

    dic[hour] = dic.get(hour,0) + 1
#    print("found", hour, dic[hour], "time")

#print(dic)

temp = sorted(dic.items())
for key, value in temp:
    print(key, value)