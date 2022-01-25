# Quiz: Dictionaries

1. How are Python dictionaries different from Python lists?
- Python dictionaries are a collection and lists are not a collection
- Python lists maintain order and dictionaries do not maintain order
- Python lists store multiple values and dictionaries store a single value
- Python lists can store strings and dictionaries can only store words

2. How are Python dictionaries different from Python lists?
- Python dictionaries are a collection and lists are not a collection
- Python lists are indexed using integers and dictionaries can use strings as indexes
- Python lists can store strings and dictionaries can only store words
- Python lists store multiple values and dictionaries store a single value

3. What is a term commonly used to describe the Python dictionary feature in other programming languages?
- Lambdas
- Associative arrays
- Sequences
- Closures

4. What would the following Python code print out?
```
stuff = dict()
print(stuff['candy'])
```
- candy
- The program would fail with a traceback
- -1
- 0

5. What would the following Python code print out?
```
 stuff = dict()
 print(stuff.get('candy',-1))
```
- 0
- -1
- The program would fail with a traceback
- 'candy'

6. (T/F) When you add items to a dictionary they remain in the order in which you added them.
- True
- False

7. What is a common use of Python dictionaries in a program?
- Splitting a line of input into words using a space as a delimiter
- Building a histogram counting the occurrences of various strings in a file
- Sorting a list of names into alphabetical order
- Computing an average of a set of numbers

8. Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?
```
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
```
- counts[key] = key + 1
- counts[key] = (counts[key] * 1) + 1
- counts[key] = counts.get(key,-1) + 1
- counts[key] = (key in counts) + 1
- counts[key] = counts.get(key,0) + 1

9. In the following Python, what does the for loop iterate through?
```
x = dict()
...
for y in x :
     ...
```
- It loops through the integers in the range from zero through the length of the dictionary
- It loops through the keys in the dictionary
- It loops through the values in the dictionary
- It loops through all of the dictionaries in the program

10. Which method in a dictionary object gives you a list of the values in the dictionary?
- items()
- all()
- values()
- each()
- keys()

11. What is the purpose of the second parameter of the get() method for Python dictionaries?
- An alternate key to use if the first key cannot be found
- To provide a default value if the key is not found
- The key to retrieve
- The value to retrieve