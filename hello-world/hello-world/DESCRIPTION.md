### Libraries in C
The first part of a C program typically involves including libraries. Libraries give us access to various useful functions, such as printing text to the screen or getting input from the user.
```C
#include <stdio.h>
```
The line above imports the `stdio.h` (Standard Input/Output) library, which contains functions for input and output operations, such as `printf` (used for printing to the screen) and `scanf` (used for reading user input). Without including this line, we wouldn’t be able to use these functions in our program.

### The `main` Function
In C, every program must have a `main` function. This function marks the **starting point of execution**. When the program runs, it starts executing the code from here. C programs always run from top to bottom, meaning that each line of code happens one at a time, from start to end. `main` is always the starting place, `return 0;` the stopping place.
```C
int main() {
    return 0;
}
```
- `int`: This is the return type of the `main` function, which specifies that `main` will return an integer value.
- `return 0;`: This statement indicates that the program has run successfully. Returning 0 is a common way to signal success in C.

The concept of return types and the return statement will be covered more thoroughly in the Functions module so don't worry about fully understanding them now.

**Curly braces** `{ }` are used to define the start and end of the `main` function's code block. Everything between these braces is part of the function, and it tells the compiler where the function begins and ends.

### Printing Output
We can use the `printf` function to output text to the screen. The text we want to display is passed to `printf` as a parameter (or argument). For example, if we want to print the text `"Welcome to the CSC-150 Dojo!"`, we would use the following code:
```C
printf("Welcome to the CSC-150 Dojo!");
```
- The text inside the quotes `" "` is a string literal and is exactly what will appear on the screen when the program is executed.

### Including Newlines with `\n`
In C, you can use the **escape sequence** `\n` within a string to represent a new line (i.e., move to the next line in the output).

For example, if you want to print text on multiple lines, you can use `\n` like this:
```C
printf("Welcome to the CSC-150 Dojo!\n");
printf("Let's get started!\n");
```
This would output:
```commandline
Welcome to the CSC-150 Dojo!
Let's get started!
```
- `\n` is a special character in C known as an escape sequence. It tells the program to move the output cursor to the next line, just like hitting the **Enter** or **Return** key on your keyboard.
- Without the `\n`, the printed text will stay on the same line. If you omit it, you'll get something like this:
```C
printf("Welcome to the CSC-150 Dojo!");  // Prints on the same line
printf("We are going to learn C!");  // Also prints on the same line
```
Which would output:
```commandline
Welcome to the CSC-150 Dojo!Let's get started!
```
You can use `\n` as many times as you need to control the formatting of your output and create more readable, user-friendly text on the screen.

### Importance of Semicolons
You might have noticed that some lines end with a semicolon (`;`). In C, semicolons are used to mark the end of a statement. A statement is any line of code that performs an action, such as declaring a variable, assigning a value, or calling a function.
- **Why semicolons are important**: Without semicolons, the compiler wouldn’t know where one statement ends and the next begins, leading to errors.


### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a C file and name it whatever you want (just make sure it ends with `.c`).
2. Inside your C file, include the `stdio.h` library and create `main` function. Don't forget `return 0;` at the end of `main`!
3. Use the `printf` function inside `main` to print the text `Hello World!` to the screen (make sure to include a newline at the end!).
4. To get the flag, run `verify <your_file>.c` (replacing `<your_file>` with the name of your C file) after completing the steps above to verify your solution.