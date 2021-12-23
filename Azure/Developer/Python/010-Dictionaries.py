#Dictionaries
#Dictionaries are a collection of key-value pairs.
#Dictionaries are similar to lists, except that indexing is done via keys instead of integers.
#Dictionaries are enclosed in curly braces {}, and have keys and values separated by a colon :.
#Dictionaries are unordered, which means that the order of the key-value pairs is not guaranteed.
#Dictionaries are mutable, which means that they can be changed after they have been created.

file_count = {'Python': 1.2, 'Java': 1.4, 'C++': 1.5, 'Ruby': 1.8}
print(file_count)
print(file_count['Python'])
print(file_count.keys())
print(file_count.values())
print(file_count.items())

#add a new key-value pair
file_count["JavaScript"] = 1.6
print(file_count)


#delete a key-value pair
del file_count["Ruby"]
print(file_count)

#update a key-value pair
file_count["Python"] = 1.7
print(file_count)

#check if a key exists
print("Java" in file_count)
print("JavaScript" in file_count)

#check if a value exists
print(1.7 in file_count.values())
print(1.8 in file_count.values())

#check if a key-value pair exists
print(file_count.get("Python"))
print(file_count.get("Python", "Not Found"))

#dictionary .update() method

#iterate through a dictionary
for key, value in file_count.items():
    print(f"{key} is {value}")

#iterate through a dictionary's keys
for key in file_count.keys():
    print(key)

#iterate through a dictionary's values
for value in file_count.values():
    print(value)

#Exercise
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

#check data types
print(type(toc))
print(type(toc.keys()))
print(type(toc.values()))
print(type(toc.items()))

#iterate through a dictionary
for files in file_count:
    print(files)

#Exercise
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys, values in cool_beasts.items():
    print("{} have {}".format(keys, values))

#Exercise
def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1
    return letter_count

count = count_letters("AaBbCc dEeFf 1234") 
print(count)

#Exercise - output should be : "red shirt", "blue shirt", and so on
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
	for item in value:
		print("{} {}".format(item, key))

#dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
#dict.clear() - Removes all the items of the dictionary
#dict.copy() - Returns a shallow copy of the dictionary
#dict.fromkeys(seq[, value]) - Returns a dictionary with keys from seq and value equal to value.

#List vs Dictionary
#List is a collection of items in a particular order.
#Dictionary is a collection of key-value pairs.
#List is mutable, dictionary is immutable.
#List is ordered, dictionary is unordered.
#List is indexed, dictionary is not indexed.
#List is a sequence, dictionary is a mapping.
#Dictionary is a hash table, list is a linked list.
#Dictionary is better for large data sets, list is better for small data sets.
#Dictionary is better for fast lookup, list is better for insertion and deletion.
#Dictionary It doesn't matter if you have 10 users or 10,000 users, accessing the entry for a given user will take the same time.

#Use Dictionary if you are going to search for a specific element.

#Set vs Dictionary
#Is like a list, but it doesn't have duplicates.
#Is like a dictionary, but it doesn't have keys.