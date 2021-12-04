Random random = new Random();
int attack = random.Next(1, 10);
int hero = 10;
int monster = 10; 

do
{
    attack = random.Next(1, 10);
    //The hero will attack first
    monster = monster - attack;
    Console.WriteLine($"Monster was damaged and lost {attack} health and now has {monster} health.");

    if (monster <=0) continue;

    attack = random.Next(1, 10);
    hero = hero - attack;
    Console.WriteLine($"Hero was damaged and lost {attack} health and now has {hero} health.");
;
} while ((hero > 0) && (monster > 0));

if (hero > monster)
    Console.WriteLine("Hero Wins!");
else
    Console.WriteLine("Monster Wins!");

/*
while (current >= 3)
{
    Console.WriteLine(current);
    current = random.Next(1, 11);
}
Console.WriteLine($"Last number: {current}");
*/
