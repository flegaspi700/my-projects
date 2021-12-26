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

#Generate a random two dimensional array
import random

ran_array = []





