### Storing Big Numbers in C
In C, when you need to store numbers that are larger than what standard integers or floats can handle, you can use `long` and `double` data types. These types allow you to work with larger whole numbers and more precise or larger decimal numbers, respectively.

* `long` (long integer)
    * Used to store larger whole numbers, typically requiring 8 bytes of memory
    * Can hold values up to approximately ±9 quintillion (±9,223,372,036,854,775,807)
    * Declared with the `long` keyword
    * Printed using the `%ld` format specifier

* `double` (double-precision floating-point)
    * Used to store larger or more precise numbers with decimal places, requiring 8 bytes of memory
    * Offers about 15-17 decimal places of precision and can handle much larger values than float
    * Declared with the `double` keyword
    * Printed using the `%lf` format specifier

### Declaring and Using Big Number Types
To use `long` or `double`, declare them with their respective keywords. Initialize and manipulate them similarly to `int` and `float`, but be mindful of their format specifiers when printing.

Example:
```C
long big_int = 1234567890123;
double big_float = 1234567890.123456789;

printf("Big integer: %ld\n", big_int);
printf("Big float: %lf\n", big_float);
```

```commandline
Big integer: 1234567890123
Big float: 1234567890.123457
```

NOTE: When printing a double, `%lf` shows up to 6 decimal places by default, but you can specify precision (e.g., `%.9lf` for 9 decimal places). For scanf, use `%ld` for `long` and `%lf` for `double`, with the `&` operator before the variable name.

### Challenge Instructions
Follow these steps to complete this challenge!

1. Create a new C file in your home directory (choose any name).
2. Declare one long variable and one double variable.
3. Get user input to initialize both variables, using appropriate prompts and format specifiers (`%ld` for `long`, `%lf` for `double`).
4. Perform the following operations:
    * For the `long` variable, multiply it by 1000 using `*=` and store the result in the same variable.
    * For the `double` variable, add 5000 to it using `+=` and store the result in the same variable.
5. Print both results in the format shown below, ensuring the `double` shows 6 decimal places.
6. Compile and run your program to test it.
7. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output:
```commandline
Enter a large integer: 123456789
Enter a large decimal number: 987.654321
Large integer after multiplying by 1000: 123456789000
Large decimal after adding 5000: 5987.654321
```