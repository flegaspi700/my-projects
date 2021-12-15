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
