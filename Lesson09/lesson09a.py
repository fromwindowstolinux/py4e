# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
list_of_words = []
fh = open(fname)
for line in fh:
    #split the line
    line = line.split()
    #check for repeated words
    for word in line:
        if word in list_of_words:
            continue
    #append unrepeated words in the list
        list_of_words.append(word)
    #sort all the words
list_of_words.sort()
print(list_of_words)