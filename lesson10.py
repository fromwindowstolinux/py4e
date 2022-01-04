# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

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
#    print(words[1])
    word = words[1]
#    print(word)
    dic[word] = dic.get(word,0) + 1
#    print("found", word, dic[word], "time")
#print(dic)

highest_frequency = -1
sender = None
for key,value in dic.items():
#    print (key,value)
    if value > highest_frequency:
        highest_frequency = value
        sender = key

print(sender, highest_frequency)