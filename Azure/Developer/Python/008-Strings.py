#Strings
def double_word(word):
    word = word * 2
    wordlen = len(word)
    message = word + str(wordlen)
    return message

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#String Indexing
"""
Modify the first_and_last function so that it returns True if the first letter of the string is the same as the 
last letter of the string, False if they’re different. 

Remember that you can access characters using message[0] or message[-1].
Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
"""
def first_and_last(message):
    if len(message) == 0:
        return True
    else:
        if message[0] == message[-1]:
            return True
        else:
            return False

print(first_and_last("ef"))
print(first_and_last("ereeh"))
print(first_and_last(""))

#String Slicing
def first_three(message):
    return message[1:4]

print(first_three("hi"))
print(first_three("hello"))
print(first_three("abcdefg"))

fruit = "pineapple"
print(fruit[:3])
print(fruit[3:])
print(fruit[:])

#methods
message = "Hello World"
print(message.index("o", 5))

#upper and lower case
print(message.upper())
print(message.lower())

#strip
message = "   Hello World   "
print(message.strip())

#lstrip
message = "   Hello World   "
print(message.lstrip())
#rstrip
message = "   Hello World   "
print(message.rstrip())

#count
message = "Hello World"
print(message.count("l"))

#replace
message = "Hello World"
print(message.replace("World", "Universe"))

#endswith
message = "Hello World"
print(message.endswith("World"))

#startswith
message = "Hello World"
print(message.startswith("Hello"))

#isnumeric
message = "Hello World"
print(message.isnumeric())

#join
message = "...".join(["a", "b", "c"])
print(message)

#split
message = "Hello World"
print(message.split())

#initials
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0] 
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

#isalpha
message = "Hello World"
print(message.isalpha())

#Formatting
print("{} {}".format("Hello", "World"))
print("{1} {0} {1}".format("Hello", "World"))
print("{greeting} {name}".format(greeting="Hello", name="World"))

name = "John"
age = 23
print("{} is {} years old.".format(name, age))

name = "Paul"
age = 10 * 3
print("{n} is {a} years old.".format(n=name, a=age))

#sample
def student_grade(name, grade):
    message = ("{n} received {g}" + "%" + " on the exam.").format(n=name, g=grade)

    return message

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#f-strings with numbers
#2f - 2 decimal places
price = 24.95
discount = 0.4
tax = 0.06
total = price * (1 - discount) * (1 + tax)
print("The total cost is ${:.2f}".format(total))
print(f"The total cost is ${total:.2f}")

#another sample
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

for x in range(0, 101, 10):
    print(f"{x} degrees Fahrenheit is {to_celsius(x)} degrees Celsius")
    
#>3 means we want the numbers to be aligned to the right for a total of three spaces
#>6.2f means we want the numbers to be aligned to the right for a total of six spaces and two decimal places
for x in range(0, 101, 10):
    print(f"{x:>3} degrees Fahrenheit is {to_celsius(x):>6.2f} degrees Celsius")

"""
String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
https://docs.python.org/3/library/stdtypes.html#string-methods
"""