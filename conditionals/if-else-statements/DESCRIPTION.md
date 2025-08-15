### If/Else Statements in C
In C, `if/else` statements allow you to execute different blocks of code based on a condition. The `if` block runs if the condition is true (non-zero), while the `else` block runs if the condition is false (zero), providing an alternative action when the `if` condition is not met.

### Syntax of If/Else Statements
An `if/else` statement uses the following structure:
```C
if (condition) {
    // Code to execute if condition is true
} else {
    // Code to execute if condition is false
}
```
- The `condition` is an expression that evaluates to true (non-zero) or false (zero).
- The `if` block runs if the condition is true; otherwise, the `else` block runs.
- Common comparison operators include:
    - `==` (equal to)
    - `!=` (not equal to)
    - `<` (less than)
    - `>` (greater than)
    - `<=` (less than or equal to)
    - `>=` (greater than or equal to)

Example:
```C
int age = 17;
if (age >= 18) {
    printf("You can vote!\n");
} else {
    printf("You are too young to vote.\n");
}
```

Output:
```commandline
You are too young to vote.
```

### Notes
* The condition must be enclosed in parentheses `()`.
* Curly braces `{}` are optional for single-statement blocks, but using them is recommended for clarity.
* The `else` block ensures your program handles both outcomes of the condition.

### Challenge Instructions
Follow these steps to complete this challenge!
- Create a new C file in your home directory (choose any name).
- Declare an integer variable called `num`.
- Get user input for `num` using the prompt shown in the example output below.
- Use an `if/else` statement to check if the number is even.
    - If the number is even, print the message indicating it is even.
    - If the number is odd, print the message indicating it is odd.
- Compile and run your program to test it.
- To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```commandline
Enter a number: 4
The number is even
```
```commandline
Enter a number: 7
The number is odd
```

**NOTE:** Remember that we can use modulus `%` to get the remainder of the number so all even numbers would have a remainder of `0` when divided by `2`.
