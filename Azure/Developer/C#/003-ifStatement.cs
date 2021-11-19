Random dice = new Random();
int diceRoll1 = dice.Next(1, 7);
int diceRoll2 = dice.Next(1, 7);
int diceRoll3 = dice.Next(1, 7);

int total = diceRoll1 + diceRoll2 + diceRoll3;

Console.WriteLine($"You rolled a {diceRoll1} + {diceRoll2} + {diceRoll3} = {total}");
if ((total >= 2) && (total <= 12))
{
    Console.WriteLine("You win!");
}
else
{
    Console.WriteLine("You lose!");
}

if (total == 7 || total == 11)
{
    Console.WriteLine("You win!");
}
else if (total == 2 || total == 3 || total == 12)
{
    Console.WriteLine("You lose!");
}
else
{
    Console.WriteLine("You get to roll again!");
}
//
Random dice = new Random();

int roll1 = dice.Next(1, 7);
int roll2 = dice.Next(1, 7);
int roll3 = dice.Next(1, 7);

int total = roll1 + roll2 + roll3;

Console.WriteLine($"Dice roll: {roll1} + {roll2} + {roll3} = {total}");

if ((roll1 == roll2) || (roll2 == roll3) || (roll1 == roll3))
{
    if ((roll1 == roll2) && (roll2 == roll3))
    {
        Console.WriteLine("You rolled triples!  +6 bonus to total!");
        total += 6;
    }
    else
    {
        Console.WriteLine("You rolled doubles!  +2 bonus to total!");
        total += 2;
    }
}

if (total >= 16)
{
    Console.WriteLine("You win a new car!");
}
else if (total >= 10)
{
    Console.WriteLine("You win a new laptop!");
}
else if (total == 7)
{
    Console.WriteLine("You win a trip for two!");
}
else
{
    Console.WriteLine("You win a kitten!");
}

//
string message = "the quick brown fox jumps over the lazy dog";
bool result = message.Contains("fox");
Console.WriteLine(result);
//output is true

if (message.Contains("fox"))
{
    Console.WriteLine("The fox is in the sentence!");
}
else
{
    Console.WriteLine("The fox is not in the sentence!");
}
//output: The fox is in the sentence!

//challenge
int expireDays = 11;

if ((expireDays <= 10) && (expireDays > 5))
{
    Console.WriteLine("Your subscription will expire soon. Renew now!");
}
else if ((expireDays <= 5) && (expireDays > 1))
{ 
    Console.WriteLine($"Your subscription expires in {expireDays} days.");
    Console.WriteLine("Renew now and save 10%!");
}
else if (expireDays == 1)
{ 
    Console.WriteLine($"Your subscription expires in within a day.");
    Console.WriteLine("Renew now and save 20%!");
}
else if (expireDays == 0)
{
    Console.WriteLine("Your Subscription has expired");
}
else 
{
    Console.WriteLine("You're ok");
}
