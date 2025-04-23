### If Statements in C
In C, `if` statements allow you to execute code conditionally based on whether a specified condition evaluates to true. An `if` statement checks a condition, and if the condition is true (non-zero in C), the code block inside the if is executed. If the condition is false (zero), the code block is skipped.

### Syntax of If Statements
An if statement uses the following structure:
```C
if (condition) {
    // Code to execute if condition is true
}
```

* The `condition` is an expression that evaluates to true (non-zero) or false (zero).
* The code block inside `{}` runs only if the condition is true.
* Common comparison operators include:
    * `==` (equal to)
    * `!=` (not equal to)
    * `<` (less than)
    * `>` (greater than)
    * `<=` (less than or equal to)
    * `>=` (greater than or equal to)

Example:
```C
int x = 10;
if (x > 5) {
    printf("x is greater than 5\n");
}
```

Output:
```commandline
x is greater than 5
```

### Notes
* The condition must be enclosed in parentheses `()`.
* The curly braces `{}` are optional if the `if` block contains only one statement, but using them is good practice for clarity.
* No `else` is required; the program simply continues after the if block if the condition is false.

### Challenge Instructions
Follow these steps to complete this challenge!

1. Create a new C file in your home directory (choose any name).
2. Declare an integer variable called `age`.
3. Get user input for `age` using the prompt in the example output below.
4. Print out the user's age with the same output as the example below.
5. Use an if statement to check if the user is old enough to vote (age 18 or older).
    * If the condition is true, print the message below indicating they can vote.
6. Compile and run your program to test it.
7. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```commandline
Enter your age: 24
You are 24 years old.
You are old enough to vote!
```

```commandline
Enter your age: 17
You are 17 years old.
```