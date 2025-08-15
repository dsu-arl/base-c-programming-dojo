# What are Variables?

Variables are places to store data in programs!
You can imagine a variable as a labeled box where you can store information to use later. 
For example, if you want to remember someone's age, you can create a variable named `age` and put the number inside.
Later in your program, you can see the value stored in the `age` box, change it, and use it to accomplish whatever goals your program may have.

## Declaring Variables

In C, all variables must be __declared__ and given a __data type__ before they can be used.
__Declaring__ a variable is telling the computer that you would like to create a new variable, and the computer will allocate (or assign) memory for that variable to use.
The variable's __data type__ tells the computer what type of data will be stored - numbers, letters, etc.
C has 3 main data types: __integers__ store whole numbers, __floats__ store numbers with decimal points, and __characters__ store characters (letters, numbers, symbols, etc.).

## Initializing Variables

In C, after a variable has been declared, the computer assigns a random chunk of memory for that variable to use. 
This chunk of memory may have leftover garbage data in it already from other programs.
Therefore, it is best practice to always __initialize__ your variables (depending on how they will be used). 
__Initializing__ a variable is when you store a value in it for the first time (its initial value).
After a variable has been initialized, you know that it does not have garbage data in it, and it can be used correctly in your program.
You can initialize a variable by hardcoding it (giving it a value directly in the code) or by getting user input.

# Helpful Terminology

- __Variable__ - a place to store data
- __Declaration__ - creating a new variable/allocating memory (has garbage data in it at first)
- __Initialization__ - storing a value in a variable for the first time 
- __Data Type__ - the kind of values that will be stored
- __Integers__ - positive or negative whole numbers
- __Floats__ - positive or negative numbers with decimal points
- __Characters__ - letters, numbers, symbols
