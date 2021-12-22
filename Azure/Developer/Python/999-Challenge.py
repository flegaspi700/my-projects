#Number Arrays
#Problem statement: Sum of Two Numbers.
#Given an array of integers and a value, 
#determine if there are any two integers in the array whose sum is equal to the given value. 
#Return true if the sum exists and return false if it does not.
numbers = [2, 4, 6, 8, 10, 2, 5]
target_number = [10, 11, 22, 12]
#This is using a for loop to iterate through the list. This will work but will be inefficient.
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if (i != j) and (numbers[i] + numbers[j] == target_number):
            print(f"{numbers[i]} + {numbers[j]} and {i} != {j}")

def sum_of_two_numbers(numbers, t_number):
    target_num_found = False
    found_numbers = []
    #This is using a for loop to iterate through the list. This will work but will be inefficient.
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j) and (numbers[i] + numbers[j] == t_number) and not ((i in found_numbers) and (j in found_numbers)):
                print(f"{t_number} = {numbers[i]:>2} + {numbers[j]:>2} in Index {i} and {j}")
                target_num_found = True
                found_numbers.append(i)
                found_numbers.append(j)
                #print(found_numbers)

    if target_num_found == False:
        print(f"{t_number} No equivalent sum was found")

for t_num in target_number:
    sum_of_two_numbers(numbers, t_num)

#for count, number in enumerate(numbers):
#    print(count, number)

#for i in range(len(numbers)):
#    print(i, "print i")

#for number in numbers:
#    print(number, numbers.index(number))

#if numbers.count(2) > 0:
#    print(numbers.count(2), "Here")

numbers = [2, 4, -2, 8, 10, 7, 5]
target_number = 0

def sum_two(numbers,target_number):
    find_num = 0
    for num in numbers:
        find_num = target_number - num
        if (find_num in numbers) and (numbers.index(find_num) != numbers.index(num)):
            return True
    return False

print(sum_two(numbers, target_number))

#if 2 in numbers:
#    print("Found 2")