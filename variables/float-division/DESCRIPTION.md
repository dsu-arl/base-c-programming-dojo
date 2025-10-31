<<<<<<< HEAD
### Floating Point Math
Math operations for float variables are much the same as integer variables.
Addition `+`, subtraction `-`, and multiplication `*` are all the same (just with decimal places). 
The main differences come with the modulus `%` and division `/` operations.

The modulus `%` does __not__ work with float operations. Because we have decimal places, there is no remainder leftover to store. 

While integers round down with division `/`, floats will keep as much precision as possible - up to 6 decimal places.
The division result will round up if the seventh digit of precision is greater than 6. (Ex. `10 / 6 = 1.666667`)

Simple division example:
```
float x = 8.45;
float y = 2.3;
float div = x / y;

printf("Result: %f\n", div);
```

Output:
```
Result: 3.673913
```

### Simple Type Casting
We typically do not want to mix our data types - for example, we __cannot__ store a float value in a character variable.
But some data can be converted from one type to another fairly simply. 
Because integers and floats are both numerical, we can carefully use them together. 
When we do this, we will use a process called __type casting__ - converting a variable from one data type to another.
Without type casting, if we divide two integers and try to store the result in a float, the division will be __integer division__, which will **not** keep the decimal places and will round down. 

Example:
```
int x = 5, y = 4;
float res = x / y;

printf("Result: %f\n", res);
```

We would expect this result to be 1.25, but because integer division occurred, this is the output:
```
Result: 1
```

If we want to keep those decimal places, we need to tell the program to divide those integers like they are floats.
Type casting allows us to use one data type and treat it like another.
So, to divide two integers and store the precise result in a float, we need to **cast** those integers into floats. 
To cast one type to another, we just need to put parenthesis in front of the variable we want to change, and give it the new data type - `(float)x`, `(char)val`, `(int)num`.
This casting only occurs on the line that it is used, and does not change the data type of `x` and `y` permanently. 
When casting from one type to another, make sure you are storing the result as the correct type.

(Note that if you cast a `float` to an `int`, it will just drop the decimal places and round down.)

With most math operations, you technically only need to cast one of the variables to a float, but you can also cast both if you prefer. 

Example:
```
int x = 5, y = 4;
float res = (float)x / (float)y;

printf("Result: %f\n", res);
```

Output:
```
Result: 1.250000
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file.
2. Get user input for two **integer variables** using the same prompts as the example output below.
3. Divide the first number by the second number, and store the result in a **float**.
4. Print out the **operation** and the result, with all 6 decimal places of precision. (Hint: You will need two `%d`s and one `%f` in your print statement, along with all three variables in the correct order.)
5. Compile and run your program to test it.
6. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```
Enter your first integer: 8
Enter your second integer: 3
8 / 3 = 2.666667
```
=======
### Floating Point Math
Math operations for float variables are much the same as integer variables.
Addition `+`, subtraction `-`, and multiplication `*` are all the same (just with decimal places). 
The main differences come with the modulus `%` and division `/` operations.

The modulus `%` does __not__ work with float operations. Because we have decimal places, there is no remainder leftover to store. 

While integers round down with division `/`, floats will keep as much precision as possible - up to 6 decimal places.
The division result will round up if the seventh digit of precision is greater than 6. (Ex. `10 / 6 = 1.666667`)

Simple division example:
```
float x = 8.45;
float y = 2.3;
float div = x / y;

printf("Result: %f\n", div);
```

Output:
```
Result: 3.673913
```

### Simple Type Casting
We typically do not want to mix our data types - for example, we __cannot__ store a float value in a character variable.
But some data can be converted from one type to another fairly simply. 
Because integers and floats are both numerical, we can carefully use them together. 
When we do this, we will use a process called __type casting__ - converting a variable from one data type to another.
Without type casting, if we divide two integers and try to store the result in a float, the division will be __integer division__, which will **not** keep the decimal places and will round down. 

Example:
```
int x = 5, y = 4;
float res = x / y;

printf("Result: %f\n", res);
```

We would expect this result to be 1.25, but because integer division occurred, this is the output:
```
Result: 1
```

If we want to keep those decimal places, we need to tell the program to divide those integers like they are floats.
Type casting allows us to use one data type and treat it like another.
So, to divide two integers and store the precise result in a float, we need to **cast** those integers into floats. 
To cast one type to another, we just need to put parenthesis in front of the variable we want to change, and give it the new data type - `(float)x`, `(char)val`, `(int)num`.
This casting only occurs on the line that it is used, and does not change the data type of `x` and `y` permanently. 
When casting from one type to another, make sure you are storing the result as the correct type.

(Note that if you cast a `float` to an `int`, it will just drop the decimal places and round down.)

With most math operations, you technically only need to cast one of the variables to a float, but you can also cast both if you prefer. 

Example:
```
int x = 5, y = 4;
float res = (float)x / (float)y;

printf("Result: %f\n", res);
```

Output:
```
Result: 1.250000
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file.
2. Get user input for two **integer variables** using the same prompts as the example output below.
3. Divide the first number by the second number, and store the result in a **float**.
4. Print out the **operation** and the result, with all 6 decimal places of precision. (Hint: You will need two `%d`s and one `%f` in your print statement, along with all three variables in the correct order.)
5. Compile and run your program to test it.
6. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```
Enter your first integer: 8
Enter your second integer: 3
8 / 3 = 2.666667
```
>>>>>>> main
