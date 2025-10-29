<<<<<<< HEAD
### Integer Variables in C
In C, integer variables are used to store whole numbers (both positive and negative) without decimal points. 
An integer typically takes up 4 bytes of memory, and can hold numbers that are smaller than positive or negative 2.1 billion. 
This limitation is due to +2.1 billion and -2.1 billion being the largest values that can fit in 4 bytes of memory.

### Declaring Integers
All variables must be given both a data dype and a name when they are declared.
The keyword `int` is used to declare an integer variable.
In the example below, `int` is the data type and `year` is the variable name. 
```
int year;
```

In the rest of our program, we can just use the variable name (`year`) to refer to this variable. 
Variable names should be descriptive - in this example, the `year` variable will be used to store the current year.

You can declare as many variables as you want.
```
int x;
int y;
int z;
```

You can also declare all of your variables on one line - each variable will be the same data type and their names must be comma separated.
```
int x, y, z;
```

### Initializing Integers
To initialize our `year` variable, we simply assign it a value. The value on the right is stored in the variable on the left.
(Remember that the variable must be declared before it can be initialized or used in your program.) 
```
year = 2025;
```

You can use this format to update your variables at any time.
Variables will always hold the value most recently assigned to them, they will continue to store that value until the program ends or the variable is updated.
```
year = 2026;
year = 2027;
```

You can also declare and initialize all on one line, and then use your variable as normal.
```
int year = 2025;
```

### Printing Integers
When printing variables, we will continue using the `printf` function. 
To print out the value stored in a variable, we will need to use __format specifiers__, which are special characters that tell `printf` how to display output. 
The format specifier for integers is `%d`.
When printing variables, we also need to tell `printf` which variable to print. 
```
printf("The current year is %d\n", year);
```

In the example above, `printf` will print all of the text in the quotation marks, and it will replace the `%d` with the value stored in the `year` variable. 

We can print multiple variables in a single `printf`. The number of variables must match the number of `%d`s you have, and the order will also match. The first `%d` will print the value stored in the first variable, the second `%d` will print the second variable, and so on.
```
printf("%d, %d\n", x, y);
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Create a new C file in your home directory (whatever name you want).
2. Declare an integer variable with the name `age`, and initialize it to your current age.
3. Print out your integer variable in the following format (don't forget the `\n`):
4. Compile and run your program to test it.
5. To get the flag, run `/challenge/verify <your_file>.c` to verify your solution.

Example output:
```
My age is: 25
```

=======
### Integer Variables in C
In C, integer variables are used to store whole numbers (both positive and negative) without decimal points. 
An integer typically takes up 4 bytes of memory, and can hold numbers that are smaller than positive or negative 2.1 billion. 
This limitation is due to +2.1 billion and -2.1 billion being the largest values that can fit in 4 bytes of memory.

### Declaring Integers
All variables must be given both a data dype and a name when they are declared.
The keyword `int` is used to declare an integer variable.
In the example below, `int` is the data type and `year` is the variable name. 
```
int year;
```

In the rest of our program, we can just use the variable name (`year`) to refer to this variable. 
Variable names should be descriptive - in this example, the `year` variable will be used to store the current year.

You can declare as many variables as you want.
```
int x;
int y;
int z;
```

You can also declare all of your variables on one line - each variable will be the same data type and their names must be comma separated.
```
int x, y, z;
```

### Initializing Integers
To initialize our `year` variable, we simply assign it a value. The value on the right is stored in the variable on the left.
(Remember that the variable must be declared before it can be initialized or used in your program.) 
```
year = 2025;
```

You can use this format to update your variables at any time.
Variables will always hold the value most recently assigned to them, they will continue to store that value until the program ends or the variable is updated.
```
year = 2026;
year = 2027;
```

You can also declare and initialize all on one line, and then use your variable as normal.
```
int year = 2025;
```

### Printing Integers
When printing variables, we will continue using the `printf` function. 
To print out the value stored in a variable, we will need to use __format specifiers__, which are special characters that tell `printf` how to display output. 
The format specifier for integers is `%d`.
When printing variables, we also need to tell `printf` which variable to print. 
```
printf("The current year is %d\n", year);
```

In the example above, `printf` will print all of the text in the quotation marks, and it will replace the `%d` with the value stored in the `year` variable. 

We can print multiple variables in a single `printf`. The number of variables must match the number of `%d`s you have, and the order will also match. The first `%d` will print the value stored in the first variable, the second `%d` will print the second variable, and so on.
```
printf("%d, %d\n", x, y);
```

### Challenge Instructions
Follow these steps to complete this challenge!

1. Create a new C file in your home directory (whatever name you want).
2. Declare an integer variable with the name `age`, and initialize it to your current age.
3. Print out your integer variable in the following format (don't forget the `\n`):
4. Compile and run your program to test it.
5. To get the flag, run `/challenge/verify <your_file>.c` to verify your solution.

Example output:
```
My age is: 25
```

>>>>>>> main
