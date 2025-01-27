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
TODO: Finish this!

### Challenge Instructions
Follow these steps to complete this challenge!
