def greeting(name):
    print("Hello, " + name)

def greeting2(name, department):
    print("Hello, " + name + " from " + department)

greeting("John")
greeting2("John", "IT")

# 
def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds)

print_seconds(1, 2, 3)

# Return value
def print_seconds2(hours, minutes, seconds):
    return (hours * 3600 + minutes * 60 + seconds)

value1 = print_seconds2(1, 2, 3)
value2 = print_seconds2(2, 3, 4)
total_seconds = value1 + value2
print("Total is " + str(total_seconds) + " seconds")

#Return multiple values
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return hours, minutes, seconds

hours, minutes, seconds = convert_seconds(5000)
print("convert seconds to hours, minutes, seconds")
print(hours, minutes, seconds)

#Return None
def greeting3(name, department):
    print("Hello and Hi, " + name + " from " + department)

result = greeting3("John", "IT")
print(result)

#Function that convert miles to kilometers(1 mile = 1.60934 km)
def convert_miles_to_kilometers(miles):
    km = miles * 1.60934
    return km

my_miles = 10
my_km = convert_miles_to_kilometers(my_miles)
print("My " + str(my_miles) + " miles is " + str(my_km) + " kilometers")


#This function compares two numbers and returns them in increasing order.
def compare_numbers(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1

smaller, larger = compare_numbers(10, 20)
print(smaller, larger)

#This function returns the lucky number.
def lucky_number(name):
    number = len(name) * 7
    message = "Hello, " + name + " Your lucky number is " + str(number)
    return message

print(lucky_number("Luis"))
print(lucky_number("Tiffany"))