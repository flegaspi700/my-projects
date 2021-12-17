#Use for loops when there's a sequence of elements that you want to iterate. 
#Use while loops when you want to repeat an action until a condition changes.

#break and continue
#break
#The break statement ends the current loop.
#continue
#The continue statement ends the current iteration of the loop and continues with the next iteration.

#while loops
x = 0
while x <5:
    print("The current value of x is: ", x)
    x += 1
print("The loop has ended")

def attemps(tries):
    x = 1
    while x <= tries:
        print("Attempt #", x)
        x += 1
    print("You have run out of attempts")

attemps(10)


#for loops
for x in range(5):
    print("The current value of x is: ", x)
print("The FOR loop has ended")

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

#For Loops iterate over a sequence of values of any type, not just a range of numbers
for x in "Hello World":
    print(x)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
for friend in friends:
    print("Happy New Year: ", friend)

values = [ 23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("total: ", sum, "length: ", length)

values = [ "Hello", "World", "in", "a", "frame", 52, 59, 37, 48]
for value in values:
    print(value)


#For Loops in range
x = 1
for n in range(1, 15):
    x = x * n
print("Range value", x)

n=0
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(5))
print(factorial(4))

#For loops in range with step
for n in range(1, 10, 2):
    print(n)

#Nested Loops
for x in range(5):
    for y in range(3):
        print(x, y)

values = [ "Hello", "World", "in", "a", "frame"]
x = 0
y = 0
for x in range(5):
    for value in values:
        print(x, " ", value, end=" ")
    print()

for left in range(7):
    for right in range(left, 7):
        print("[", left, "|", right, "]", end="-")
    print()

teams = ["Dragons", "Wolves", "Tigers", "Lions", "Panthers"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team, "vs", away_team)

def greet_friends(friends):
    for friend in friends:
        print("Happy New Year: ", friend)

greet_friends(["Kevin", "Karen", "Jim", "Oscar", "Toby"])
greet_friends("Barry")

#Recursion - a function that calls itself until it reaches a base case and then returns the result to its caller
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
        #5 * 4 * 3 * 2 * 1

print(factorial(5))

#recursion with a while loop - a function that calls itself until it reaches a base case and then returns the result to its caller
def factorial2(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

print(factorial2(5))

