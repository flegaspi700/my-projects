//Addition operator
int firstNumber = 12;
int secondNumber = 7;
Console.WriteLine(firstNumber + secondNumber);
//Subtraction operator
Console.WriteLine(firstNumber - secondNumber);
//Multiplication operator
Console.WriteLine(firstNumber * secondNumber);
//Division operator
Console.WriteLine(firstNumber / secondNumber);
//Modulus operator
Console.WriteLine(firstNumber % secondNumber);
//Increment operator
int incrementNumber = 1;
Console.WriteLine(incrementNumber++);
//Decrement operator
int decrementNumber = 1;
Console.WriteLine(decrementNumber--);
//Assignment operator
int assignNumber = 1;
Console.WriteLine(assignNumber = 2);
//Equality operator
Console.WriteLine(firstNumber == secondNumber);
//Inequality operator
Console.WriteLine(firstNumber != secondNumber);
//Greater than operator
Console.WriteLine(firstNumber > secondNumber);
//Less than operator
Console.WriteLine(firstNumber < secondNumber);
//Greater than or equal to operator
Console.WriteLine(firstNumber >= secondNumber);
//Less than or equal to operator
Console.WriteLine(firstNumber <= secondNumber);
//Logical AND operator
Console.WriteLine(firstNumber > secondNumber && firstNumber < secondNumber);
//Logical OR operator
Console.WriteLine(firstNumber > secondNumber || firstNumber < secondNumber);
//Logical NOT operator
Console.WriteLine(!(firstNumber > secondNumber));
//Bitwise AND operator
Console.WriteLine(firstNumber & secondNumber);
//Bitwise OR operator
Console.WriteLine(firstNumber | secondNumber);
//Bitwise XOR operator
Console.WriteLine(firstNumber ^ secondNumber);
//Bitwise NOT operator
Console.WriteLine(~firstNumber);
//Bitwise left shift operator
Console.WriteLine(firstNumber << secondNumber);
//Bitwise right shift operator
Console.WriteLine(firstNumber >> secondNumber);

//Mix data types to force implicit type conversions
string firstName = "Bob";
int widgetsSold = 7;
Console.WriteLine(firstName + " sold " + widgetsSold + " widgets.");
//output: Bob sold 7 widgets.

//Attempt a more advanced case of adding numbers and concatenating strings
string firstName = "Bob";
int widgetsSold = 7;
Console.WriteLine(firstName + " sold " + widgetsSold + 7 + " widgets.");
//output: Bob sold 77 widgets.
//Add parentheses to make our intention clear to the compiler
Console.WriteLine(firstName + " sold " + (widgetsSold + 7) + " widgets.");
//output: Bob sold 14 widgets.

//To cast int to decimal, you add the cast operator before the value. 
//You use the name of the data type surrounded by parenthesis in front of the value to cast it. 
//In this case, we would add (decimal) before the variables first and second.
int first = 7;
int second = 5;
decimal quotient = (decimal)first / (decimal)second;
Console.WriteLine(quotient);
//output: 2.8

//Write code to determine the remainder after int division.
Console.WriteLine("Modulus of 200 / 5 : " + (200 % 5));
Console.WriteLine("Modulus of 7 / 5: " + (7 % 5));
//output: Modulus of 200 / 5 : 0
//output: Modulus of 7 / 5: 2

//Increment and decrement operators
int value = 1;

value = value + 1;
Console.WriteLine("First increment: " + value);

value += 1;
Console.WriteLine("Second increment: " + value);

value++;
Console.WriteLine("Third increment: " + value);

value = value - 1;
Console.WriteLine("First decrement: " + value);

value -= 1;
Console.WriteLine("Second decrement: " + value);

value--;
Console.WriteLine("Third decrement: " + value);
//output: First increment: 2
//output: Second increment: 3
//output: Third increment: 4
//output: First decrement: 3
//output: Second decrement: 2
//output: Third decrement: 1


int value = 1;
value++;
Console.WriteLine("First: " + value);
Console.WriteLine("Second: " + value++);
Console.WriteLine("Third: " + value);
Console.WriteLine("Fourth: " + (++value));
//output: First: 2
//output: Second: 2
//output: Third: 3
//output: Fourth: 4

//Fahrenheit to Celsius
int fahrenheit = 94;
decimal celsius = (fahrenheit - 32m) * (5m / 9m);
Console.WriteLine(fahrenheit + " degrees Fahrenheit is " + celsius + " degrees Celsius.");
//output: 94 degrees Fahrenheit is 34.4 degrees Celsius.

int fahrenheit = 94;
decimal celsius = (fahrenheit - 32m) * (5m / 9m);
Console.WriteLine("The temperature is " + celsius + " Celsius.");
//output: The temperature is 31.4 Celsius.

Console.WriteLine(5 / 10);
//output: 0

