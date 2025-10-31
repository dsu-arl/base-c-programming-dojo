### Shorthand Math Operations in C

In C, shorthand math operations provide concise ways to update variable values using operators like `++`, `--`, `+=`, `-=`, `*=`, `/=`, and `%=`. These operators combine an arithmetic operation with assignment, making your code more efficient and readable.

* `++` increment
    * Increases the variable's value by 1. For example, `x++` is equivalent to `x = x + 1`.
* `--` decrement
    * Decreases the variable's value by 1. For example, `x--` is equivalent to `x = x - 1`.

* `+=` add and assign
    * Adds a specified value to the variable and stores the result. For example, `x += 5` is equivalent to `x = x + 5`.

* `-=` subtract and assign
    * Subtracts a specified value from the variable and stores the result. For example, `x -= 3` is equivalent to `x = x - 3`.

* `*=` multiply and assign
    * Multiplies the variable by a specified value and stores the result. For example, `x *= 2` is equivalent to `x = x * 2`.

* `/=` divide and assign
    * Divides the variable by a specified value and stores the result. For example, `x /= 4` is equivalent to `x = x / 4`.

* `%=` modulus and assign
    * Computes the remainder of the variable divided by a specified value and stores the result. For example, `x %= 3` is equivalent to `x = x % 3`.

### Using Shorthand Operators

Shorthand operators can be used anywhere you would perform a math operation and assign the result to the same variable. They are particularly useful for updating variables in loops or when making incremental changes.

Example:
```C
int x = 10;
x += 5;  // x is now 15
x--;     // x is now 14
x *= 2;  // x is now 28
printf("x = %d\n", x);
```

Output:
```commandline
x = 28
```

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new C file in your home directory (choose any name).
2. Declare an integer variable called `num` and get user input to initialize it with a prompt.
3. Perform the following shorthand operations on `num` in this order:
    1. Increment `num` by 1 using `++.`
    2. Add 10 to `num` using `+=.`
    3. Multiply `num` by 2 using `*=.`
    4. Decrement `num` by 1 using `--`.
4. After each operation, print the updated value of `num` in the format shown below.
5. Compile and run your program to test it.
6. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```commandline
Enter a number: 5
After increment: 6
After adding 10: 16
After multiplying by 2: 32
After decrement: 31
```
