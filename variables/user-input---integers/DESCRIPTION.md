### User Input in C
Another way to initialize variables in C is to get __user input__. 
User input allows the _user_ (the person running your program) to enter and save data.
With this data, our programs will be more dynamic - they will output different things, depending on what data is entered!
Before we can get user input, we first need to declare any variables that will be used.
The variables must exist before we can store information in them. 
Then we will use the `scanf` function - which is similar to `printf` but in reverse!

```
int input;

scanf("%d", &input);
```

`scanf` still needs format specifiers (`%d` for integers), to tell your program what type of data will be entered. 
It does _not_ need a `\n`, and cannot have any other text in the quotation marks.
And finally, it needs to know which variable to store this data in. 
In `scanf`, we must put an ampersand `&` before every variable name. 
This tells the program where to store the data in memory.
After getting user input, we can continue to use the variable as normal!

```
int input;

scanf("%d", &input);
printf("You entered - %d\n", input);
```

If you write a program with the example above, you may notice that it is a bit confusing to the user. 
`scanf` essentially pauses your program, and will wait until the user types a value and presses Enter.
The user will likely not know what to do at this pause, unless we tell them.
To do this, we can give the user a __prompt__.
Prompts are optional, but very informative to the user. 
Your program will still work without them, but if the user does not know how to work your program, it is not very useful. 
We can use a `printf` to make a nice prompt - notice that there is not a `\n` in this prompt.
When the user enters their input, they will press the Enter key and move our terminal output to the next line. 

```
int input;

printf("Please type a number and press Enter: ");
scanf("%d", &input);

printf("You entered - %d\n", input);
```

Output:
```
Please type a number and press Enter: 33
You entered - 33
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Make a new C file, or edit your file from the last challenge.
2. Declare an integer variable with the name `age`, and get __user input__ to initialize it (make a prompt!).
3. Print out the value that the user entered in the following format:
4. Compile and run your program to test it.
5. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```
What is your age: 23 
Your age is: 23
```
