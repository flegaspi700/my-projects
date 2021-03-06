#Two Dimensional Array
#Problem statement: Two Dimensional Array.
#Given a two dimensional array,
#return the sum of all the values in the array.

#This is a two dimensional array.

#Questions: 
#1. does the array have the same length in each row?
#2. What is the dimension of the array? more rows or more columns?

array = [[1, 0, 3], 
         [4, 5, 6], 
         [0, 8, 9],
         [10, 11, 12],
         [13, 14, 15]]

#print the array
for row in array:
    for num in row:
        print(num, end=" ")
    print()

sum_total = 0

#print the total sum of all the values in the array
for row in array:
    for num in row:
        sum_total += num

print(f"The sum of all the values in the array is {sum_total}")

#print array using index
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=" ")
    print()

#update an array value
array[0][0] = 16
print(array[0][0])

#Check if an array has a zero value
row_with_zero = set()
col_with_zero = set()

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 0:
            print(f"found {array[i][j]} in index {i}:{j}", end="\n")
            row_with_zero.add(i)
            col_with_zero.add(j)

print("rows", row_with_zero)
print("cols", col_with_zero)

#Update the array to zero
for i in range(len(array)):
    for j in range(len(array[i])):
        if i in row_with_zero or j in col_with_zero:
            array[i][j] = 0

print("Updated array")
for row in array:
    for num in row:
        print(num, end=" ")
    print()

#Generate a array of random numbers
import random
array = [[random.randint(0, 10) for i in range(3)] for j in range(3)]
print(array)

array2 = []
for outer in range(3):
    array2.append([])
    for inner in range(3):
        array2[outer].append(random.randint(0, 10))

###############################################################################
def create_random_array(rows, cols):
    import random
    array = []
    
    for outer in range(rows):
        array.append([])
        for inner in range(cols):
            array[outer].append(random.randint(0, 9))
    
    return array

def print_array(array):
    for row in array:
        for num in row:
            print(num, end=" ")
        print()

def check_for_zero(array):
    #Check if an array has a zero value
    row_with_zero = set()
    col_with_zero = set()
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                print(f"found {array[i][j]} in index {i}:{j}", end="\n")
                row_with_zero.add(i)
                col_with_zero.add(j)
    
    return row_with_zero, col_with_zero

def update_array(array, row_zero, col_zero):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i in row_zero or j in col_zero:
                array[i][j] = 0

    return array

def main():    
    print("Main execution")
    main_array = create_random_array(5, 5)

    print("Main array")
    print_array(main_array)

    print("Checking for zero")
    row_zero, col_zero = check_for_zero(main_array)
    print("rows", row_zero)
    print("cols", col_zero)

    print("Updating array")
    updated_array = update_array(main_array, row_zero, col_zero)
    print("Updated array")
    print_array(updated_array)

main ()





