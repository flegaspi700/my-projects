//Equality operators
Console.WriteLine("a" == "a");
Console.WriteLine("a" == "A");
Console.WriteLine(1 == 2);

string myValue = "a";
Console.WriteLine(myValue == "a");
//output is true

Console.WriteLine("a" == "a ");
//output is false

string value1 = " a";
string value2 = "A ";
Console.WriteLine(value1.Trim().ToLower() == value2.Trim().ToLower());
//output is true

string pangram = "The quick brown fox jumps over the lazy dog.";
Console.WriteLine(pangram.Contains("fox"));
Console.WriteLine(pangram.Contains("cow"));
//output is true
//output is false

// These two lines of code do the same thing:
Console.WriteLine(pangram.Contains("fox") == false);
//output is false
Console.WriteLine(!pangram.Contains("fox"));
//output is true


//The conditional operator ?:, commonly known as the ternary conditional operator, evaluates a Boolean expression, 
//and returns the result of evaluating one of two expressions, depending on whether the Boolean expression evaluates 
//to true or false.

//Here's the basic form:
//<evaluate this condition> ? <if condition is true, return this value> : <if condition is false, return this value>

int saleAmount = 1001;

int discount = saleAmount > 1000 ? 100 : 50;

Console.WriteLine($"Discount: {discount}");
//output is Discount: 100

int saleAmount = 1001;
// int discount = saleAmount > 1000 ? 100 : 50;

Console.WriteLine($"Discount: {(saleAmount > 1000 ? 100 : 50)}");

Rnadom rnd = new Random();
int randomNumber = rnd.Next(0, 2);
console.WriteLine((randomNumber==0) ? "Heads" : "Tails");
//output is Heads or Tails


string permission = "Admin|Manager";
int level = 53;

if (permission.Contains("Admin"))
{
    if (level > 55)
    {
        Console.WriteLine("Welcome, Super Admin user.");
    }
    else
    {
        Console.WriteLine("Welcome, Admin user.");
    }
}
else if (permission.Contains("Manager"))
{
    if (level >= 20)
    {
        Console.WriteLine("Contact an Admin for access.");
    }
    else
    {
        Console.WriteLine("You do not have sufficient privileges.");
    }
}
else
{
    Console.WriteLine("You do not have sufficient privileges.");
}