#Number Arrays
#Create a list of numbers from 0 to 100
numbers = [2, 4, 6, 8, 10, 2, 5]
target_number = 10
target_num_found = False

"""
for first_number in numbers:
    for second_number in numbers:
        print(first_number, second_number)
        if (first_number + second_number == target_number):
                print(f"{first_number} + {second_number} = {target_number}")
"""
"""
def check_sum(numbers, target_number):
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == target_number:
                message = f"{first_number} + {second_number} = {target_number}"
                return message
    return False
"""
#print(check_sum(numbers, target_number))

for i in range(len(numbers)):
    for j in range(len(numbers)):
       if (numbers.index(numbers[i]) != numbers.index(numbers[j])) and (numbers[i] + numbers[j] == target_number):
           print(f"{numbers[i]} + {numbers[j]}") 

for i in range(len(numbers)):
    print(i)

for number in numbers:
    print(number, numbers.index(number))

if numbers.count(2) > 0:
    print(numbers.count(2))

if 2 in numbers:
    print("Found 2")