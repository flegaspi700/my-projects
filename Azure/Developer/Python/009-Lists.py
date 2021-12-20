#lists
#Lists in python store values in a sequence.
#Lists are mutable, meaning they can be changed.
#Lists are created with square brackets.
#Lists can contain any type of value.
#Lists can be created with a list of values:
#numbers = [2, 4, 6, 8, 10, 2, 5]

numbers = [2, 4, 6, 8, 10, 2, 5]

#type
print(type(numbers))

#length of list
print(len(numbers))

#Check if element is in list. Returns True or False.
if 2 in numbers:
    print("Found 2")

#Check if element is not in list. Returns True or False.
if 2 not in numbers:
    print("Did not find 2")

#Print index value of element.
print(numbers[0])
#or
print(numbers[-1])

#Returns the index of the value.
print(numbers.index(2))

#Slicing lists #start:stop 
#Returns 1st to 3rd elements.
print(numbers[:3]) 
#Returns 4th to 6th elements.
print(numbers[3:])

###Test knowledge of list methods.
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
        # Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#List methods
#append - Adds an element to the end of the list.
numbers.append(12)
print(numbers)

#extend - Adds all elements of a list to the end of the current list.
numbers.extend([13, 14, 15])
print(numbers)

#insert - Adds an element at the specified position.
#insert 7 at index 3
numbers.insert(3, 7)
print(numbers)

#remove - Removes the first element from the list that is equal to the specified value.
numbers.remove(2)
print(numbers)

#pop - Removes the element at the specified position.
numbers.pop(3)
print(numbers)

#Change the value of an element.
numbers[0] = 20
print(numbers)

###Test knowledge of list methods.
def skip_elements(elements):
    # initialize an empty list
    new_list = []
    i = 0
    # loop through the elements
    for i in range(len(elements)):
        if i % 2 == 0:
            # add the element to the new list
            new_list.append(elements[i])
        i += 1
    
    # return the new list
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#tuples
#Tuples are immutable lists. They cannot be changed.
#Tuples are created with parentheses.
#Tuples can contain any type of value.
#Tuples can be created with a list of values:
#numbers = (2, 4, 6, 8, 10, 2, 5)
#Tuples the order of the elements matters.

def convert_seconds(seconds):
    # convert seconds to hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return (hours, minutes, seconds)

result = convert_seconds(5000)
print(result) # Should be (1, 1, 1)
print(type(result)) # Should be tuple

#unpacking tuples
#unpacking tuples is a common task in Python.
hours, minutes, seconds = result
print(hours, minutes, seconds)
#or
hours, minutes, seconds = convert_seconds(6000)
print(hours, minutes, seconds)

#Test knowledge of tuple methods.
def file_size(file_info):
	name, type, size= file_info
	return(f"{size / 1024 :.2f}" + " KB") 

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

#iterate through a list
animals = ["cat", "dog", "rabbit"]
chars = 0
for animal in animals:
    chars += len(animal)

print(f"There are {chars} characters in the list, Average length of animal is {chars/len(animals)}")

#enumerate - returns an enumerate object.
#enumerate object can be used to loop through the list and get the index of the element.
for index, animal in enumerate(animals):
    print(f"{index} - {animal}")

def skip_elements2(elements):
    # initialize an empty list
    new_list = []
    i = 0
    # loop through the elements
    for i, element in enumerate(elements):
        if i % 2 == 0:
            # add the element to the new list
            new_list.append(element)
        i += 1
    return new_list

print(skip_elements2(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements2(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements2([])) # Should be []

#list comprehension
#list comprehension is a quick way to create a list.
#list comprehension is a list of the results of an expression.
#list comprehension can be used to create a list of numbers.
#list comprehension can be used to create a list of strings.
#list comprehension can be used to create a list of tuples.

multiples = [ x * 3 for x in range(1, 11)]
print(multiples)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print([len(language) for language in languages])

print([language.lower() for language in languages])

z = [ x for x in range(1, 100) if x % 2 == 0]
print(z)

#Test knowledge of list comprehension.
def odd_numbers(n):
	return [x for x in range(0, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

"""
Lists and Tuples Operations Cheat Sheet
Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable, there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.

Common sequence operations
len(sequence) Returns the length of the sequence
for element in sequence Iterates over each element in the sequence
if element in sequence Checks whether the element is part of the sequence
sequence[i] Accesses the element at index i of the sequence, starting at zero
sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time

Check out the official documentation for sequence operations.

List-specific operations and methods
list[i] = x Replaces the element at index i with x
list.append(x) Inserts x at the end of the list
list.insert(i, x) Inserts x at index i
list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) Removes the first occurrence of x in the list
list.sort() Sorts the items in the list
list.reverse() Reverses the order of items of the list
list.clear() Removes all the items of the list
list.copy() Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list

 ost of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.

List comprehension
[expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.

[expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  
"""

