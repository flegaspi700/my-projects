string sku = "01-MN-L";

string[] product = sku.Split('-');

string type = "";
string color = "";
string size = "";

switch (product[0])
{
    case "01":
        type = "Sweat shirt";
        break;
    case "02":
        type = "T-Shirt";
        break;
    case "03":
        type = "Sweat pants";
        break;
    default:
        type = "Other";
        break;
}
// Output: Sweat shirt

switch (product[1])
{
    case "MN":
        color = "Maroon";
        break;
    case "BL":
        color = "Black";
        break;
    case "GR":
        color = "Green";
        break;
    case "RD":
        color = "Red";
        break;
    default:
        color = "White";
        break;
}
// Output: Maroon

switch (product[2])
{
    case "S":
        size = "Small";
        break;
    case "M":
        size = "Medium";
        break;
    case "L":
        size = "Large";
        break;
    default:        
        size = "One Size Fits All";
        break;  
}
// Output: Large

Console.WriteLine($"Product: {size} {color} {type}");
//output: Product: Large Maroon Sweat shirt
