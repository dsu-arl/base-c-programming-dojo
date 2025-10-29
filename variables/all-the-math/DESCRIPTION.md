<<<<<<< HEAD
### More Math
You already know how to do addition, so this challenge will expand on the other operators. 

- `+` addition
- `-` subtraction
    - Normal subtraction (used just like addition)
- `*` multiplication
    - Normal multiplication
- `/` division
    - With integers, all division results will __round down__, or drop any decimal places. For example, `15 / 4 = 3.75`, but with integers, we ignore those decimal places and round down to `3`. 
- `%` remainder (modulus)
    - The modulus is the remainder result of division. For example, `10 / 3` results in `3` with a remainder of `1`. The modulus only keeps the remainder - `1`. 

### Computing results
When you are performing math operations in C, you have a few options on how to use your variables. 
You can make a separate variable to hold every value you compute, you can reuse variables, or you can even do the math directly in a print statement and not need a variable at all!
See the code snippets below for examples.

Separate variables:
```
int x = 5, y = 7;
int sum = x + y;
int div = x - y;
printf("%d + %d = %d\n", x, y, sum);
printf("%d - %d = %d\n", x, y, sub);
```

Reuse variables:
```
int x = 5, y = 7;
int res = x + y;
printf("%d + %d = %d\n", x, y, res);
res = x - y;
printf("%d - %d = %d\n", x, y, res);
```

Math in print statements:
```
int x = 5, y = 7;
printf("%d + %d = %d\n", x, y, x+y);
printf("%d - %d = %d\n", x, y, x-y);
```

All above snippets will restult in the same output:
```
5 + 7 = 12
5 - 7 = -2
```

Remember, when printing multiple variables, each `%d` needs a matching variable to print out, and the order matters!
When doing math in a print statement, the result of the math will be printed in place of the `%d`.

NOTE: Since `%` is used for printing variables, we have to escape it using another `%` so it prints out properly. For example:
```C
printf("100%%\n");
```
will output `100%`.

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file.
2. Declare two integer variables, and get user input to initialize both.
3. Using whatever method you prefer, find the result of the following operations: `+`, `-`, `*`, `/`, and `%`. 
4. Print out all five results in the following format:
5. Compile and run your program to test it.
6. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.
```
Enter your first number: 4
Enter your second number: 9
4 + 9 = 13
4 - 9 = -5
4 * 9 = 36
4 / 9 = 0
4 % 9 = 4
```
=======
### More Math
You already know how to do addition, so this challenge will expand on the other operators. 

- `+` addition
- `-` subtraction
    - Normal subtraction (used just like addition)
- `*` multiplication
    - Normal multiplication
- `/` division
    - With integers, all division results will __round down__, or drop any decimal places. For example, `15 / 4 = 3.75`, but with integers, we ignore those decimal places and round down to `3`. 
- `%` remainder (modulus)
    - The modulus is the remainder result of division. For example, `10 / 3` results in `3` with a remainder of `1`. The modulus only keeps the remainder - `1`. 

### Computing results
When you are performing math operations in C, you have a few options on how to use your variables. 
You can make a separate variable to hold every value you compute, you can reuse variables, or you can even do the math directly in a print statement and not need a variable at all!
See the code snippets below for examples.

Separate variables:
```
int x = 5, y = 7;
int sum = x + y;
int div = x - y;
printf("%d + %d = %d\n", x, y, sum);
printf("%d - %d = %d\n", x, y, sub);
```

Reuse variables:
```
int x = 5, y = 7;
int res = x + y;
printf("%d + %d = %d\n", x, y, res);
res = x - y;
printf("%d - %d = %d\n", x, y, res);
```

Math in print statements:
```
int x = 5, y = 7;
printf("%d + %d = %d\n", x, y, x+y);
printf("%d - %d = %d\n", x, y, x-y);
```

All above snippets will restult in the same output:
```
5 + 7 = 12
5 - 7 = -2
```

Remember, when printing multiple variables, each `%d` needs a matching variable to print out, and the order matters!
When doing math in a print statement, the result of the math will be printed in place of the `%d`.

NOTE: Since `%` is used for printing variables, we have to escape it using another `%` so it prints out properly. For example:
```C
printf("100%%\n");
```
will output `100%`.

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file.
2. Declare two integer variables, and get user input to initialize both.
3. Using whatever method you prefer, find the result of the following operations: `+`, `-`, `*`, `/`, and `%`. 
4. Print out all five results in the following format:
```
Enter your first number: 4
Enter your second number: 9
4 + 9 = 13
4 - 9 = -5
4 * 9 = 36
4 / 9 = 0
4 % 9 = 4
```
>>>>>>> main
