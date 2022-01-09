#Reverse String per word
def reverse_string(string):
    #split string into list of words
    words = string.split()
    #reversed list of words
    rev_words = reversed(words)
    return " ".join(rev_words)

string = "Hello World and universe"

print(reverse_string(string))

#Reverse String
string2 = "Reverse this string"
print(string2[::-1])

#palindrome
string3 = "racecar"
print(string3 == string3[::-1])

#palindrome 2
string4 = "aabbbaa"

for i in range(len(string4)):
    for j in range(len(string4)+1):
        if (len(string4[i:j]) > 1) and (string4[i:j] == string4[i:j][::-1]):
            print(string4[i:j], end="\n")
