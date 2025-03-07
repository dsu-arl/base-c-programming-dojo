### Math in C
Now that we know how to __declare__, __initialize__, and get __user input__ for our variables, it's time to do some math!
Computers are _very good_ at doing math and processing data.
We can use the values stored in our variables to perform math operations and save/display the results!

### Math operators
The good news is that math in programming is just like normal math :) we use the same operators: 
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `%` remainder (modulus)

(You may not be familiar with the `%` or remainder/modulus operator - we'll cover that in a different challenge.)
With these operators, we can do math on our variables!

For example:
```
int x = 3 + 5;
int y = 10;
int z = 20;
int sum;
sum = y + z;

printf("x = %d\n", x);
printf("sum = %d\n", sum);
```

Output:
```
x = 8
sum = 30
```

In programming, we always take the result of the operation on the right side of the equals sign and store it in the variable on the left side. We don't want to do `x + y = z;` - instead do `z = x + y;`.

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file.
2. Declare three integer variables - `num1`, `num2`, and `sum`.
3. Get user input for `num1` and `num2`.
4. Find the `sum` by adding `num1` and `num2` together.
5. Print out the result!
6. To get the flag, run verify <yourfile>.c to verify your solution.

Example:
```
Enter your first number: 5
Enter your second number: 7
Sum = 12
```
