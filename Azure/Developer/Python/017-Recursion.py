#Regular Expression
import re

txt = "Oh happy day"
x = re.search("O*app*", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

#Search for a sequence that starts with "oh", followed by two (any) characters, and an "p":
x = re.findall("Ohp*", txt)
print(x)
