### Data Types in C
All variables must be given a data type when they are declared. 
So far, we have only used integer variables, which can store whole numbers. 
We can also store characters and decimal numbers in our variables. 
All variables have similar structures, and are declared/initialized/printed in much the same ways.
Below are the key differences in data types.

### Character Variables in C
Character variables can hold only a single character (a, b, c, 1, 2, 3, #, !, etc.).
A character requires just 1 byte of memory and is the smallest type of variable.

To declare a character, we use the `char` keyword:
```
char letter;
```

To initialize a character, we must use single quotation marks to show that we want to assign the character value:
```
letter = 'a';
```

Without the single quotes, the computer would assume you are trying to use another variable to initialize your character, for example:
```
char x;
char letter = x; // accesses the variable named x, not the character 'x'
```

To print a character, we use the `%c` format specifier:
```
char grade = 'A';
printf("Your grade: %c\n", grade);
```

Output:
```
Your grade: A
```

### Floating-Point Variables in C
Floating-point variables, or floats, in C are used to store numbers with decimal places. 
Floats, like integers, need 4 bytes of memory. 
They store 6 decimal places of precision with each value.

To declare a float, we use the `float` keyword:
```
float price;
```

To initialize a float, we can use values with decimal places:
```
price = 3.99;
```

To print a float, we use the `%f` format specifier:
```
printf("Items cost: %f\n", price);
```

With floats, the `%f` will print out all 6 decimal places by default, and will fill them with 0's unless otherwise initialized:
```
Items cost: 3.990000
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Create a new C file in your home directory (whatever name you want).
2. Declare 3 variables - one of each data type.
3. Initialize your variables with your first initial, your GPA, and your age. (Make sure you match data types correctly!)
3. Print out all three variables on separate lines, in the following format (and in this order):
4. Compile and run your program to test it.
5. To get the flag, run verify <yourfile>.c to verify your solution.

Example output:
```
My age is: 25
My first initial is: A
My GPA is: 3.870000
```
