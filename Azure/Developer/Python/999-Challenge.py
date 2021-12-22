#Number Arrays
#Problem statement: Sum of Two Numbers.
#Given an array of integers and a value, 
#determine if there are any two integers in the array whose sum is equal to the given value. 
#Return true if the sum exists and return false if it does not.
numbers = [2, 4, 6, 8, 10, 2, 5]
target_number = 11
target_num_found = False

#This is using a for loop to iterate through the list. This will work but will be inefficient.
for i in range(len(numbers)):
    for j in range(len(numbers)):
       if (numbers.index(numbers[i]) != numbers.index(numbers[j])) and (numbers[i] + numbers[j] == target_number):
           print(f"{numbers[i]} + {numbers[j]}")

def sum_of_two_numbers(numbers, target_number):
    #This is using a for loop to iterate through the list. This will work but will be inefficient.
    for i in range(len(numbers)):
        for j in range(len(numbers)):
           if (numbers.index(numbers[i]) != numbers.index(numbers[j])) and (numbers[i] + numbers[j] == target_number):
               print(f"{numbers[i]} + {numbers[j]}")
               target_num_found = True
    if target_num_found == False:
        print("No numbers found")

sum_of_two_numbers(numbers, target_number)

#for i in range(len(numbers)):
#    print(i, "print i")

#for number in numbers:
#    print(number, numbers.index(number))

#if numbers.count(2) > 0:
#    print(numbers.count(2), "Here")

#if 2 in numbers:
#    print("Found 2")