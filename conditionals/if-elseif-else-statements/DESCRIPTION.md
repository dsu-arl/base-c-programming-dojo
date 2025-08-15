### If/Else If/Else Statements in C
In C, `if/else if/else` statements allow you to check multiple conditions and execute different blocks of code based on which condition is true. The `if` block runs if its condition is true (non-zero). If it’s false, each `else if` block is checked in order, and its block runs if its condition is true. If no conditions are true, the `else` block (if present) runs as a default action.

### Syntax of If/Else If/Else Statements
An `if/else if/else` statement uses the following structure:
```C
if (condition1) {
    // Code to execute if condition1 is true
} else if (condition2) {
    // Code to execute if condition2 is true
} else {
    // Code to execute if no conditions are true
}
```
- Each `condition` is an expression that evaluates to true (non-zero) or false (zero).
- Only the first true condition’s block executes; subsequent conditions are skipped.
- The `else` block is optional and runs only if all conditions are false.
- Common comparison operators include:
    - `==` (equal to)
    - `!=` (not equal to)
    - `<` (less than)
    - `>` (greater than)
    - `<=` (less than or equal to)
    - `>=` (greater than or equal to)

Example:
```C
int score = 85;
if (score >= 90) {
    printf("Grade: A\n");
} else if (score >= 80) {
    printf("Grade: B\n");
} else if (score >= 70) {
    printf("Grade: C\n");
} else {
    printf("Grade: F\n");
}
```

Output:
```commandline
Grade: B
```

### Notes
- Conditions must be in parentheses `()`.
- Curly braces `{}` are optional for single-statement blocks, but using them is recommended for clarity.
- Use `else if` to check additional conditions only if prior ones fail.
- The `else` block ensures a default action if no conditions are met.

### Challenge Instructions
Follow these steps to complete this challenge!
- Create a new C file in your home directory (choose any name).
- Declare an integer variable called `num`.
- Get user input for `num` using the prompt shown in the example output below.
- Use an `if/else if/else` statement to check if the number is even, odd, or zero.
    - If the number is zero, print the message indicating it is zero.
    - If the number is even, print the message indicating it is even.
    - If the number is odd, print the message indicating it is odd.
- Compile and run your program to test it.
- To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```commandline
Enter a number: 0
The number is zero
```
```commandline
Enter a number: 4
The number is even
```
```commandline
Enter a number: 7
The number is odd
```

**NOTE:** `0 % 2` equals `0`, but we want to display a specific message for zero so make sure the ordering of the conditionals is correct.