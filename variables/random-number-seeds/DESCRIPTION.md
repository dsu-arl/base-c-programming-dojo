### Seeding Random Numbers with Fixed Values in C

In C, the `rand()` function generates pseudo-random numbers, but the sequence is predictable unless initialized with a seed using `srand()`. This challenge builds on generating random numbers and focuses on using `srand()` with user-provided integer seeds to control the random sequence, allowing reproducible results for testing or specific use cases.


### Using `srand()` and `rand()`
- **Include <stdlib.h>**:
    - Provides `srand()` to set the seed and `rand()` to generate pseudo-random numbers.
- **Seeding with `srand()`**:
    - Call `srand(seed)` with an integer `seed` to initialize the random number generator.
    - The same seed produces the same sequence of random numbers, making it useful for debugging or consistent outputs.
    - Example: `srand(42)` sets the seed to 42, ensuring the same sequence each time the program runs with that seed.
- **Generating Random Numbers**:
    - After seeding with `srand()`, use `rand()` to generate numbers, as in the previous challenge.
    - To get a random number from `0` to `max` (inclusive), use: `rand() % (max + 1)`.
- **Important Note**:
    - Call `srand()` only once at the start of `main()`. Multiple calls can reset the sequence, reducing randomness.

Example:
```C
#include <stdio.h>
#include <stdlib.h>

int main() {
    int seed = 42;
    srand(seed); // Set a fixed seed
    int random_num = rand() % (25 + 1); // Random number from 0 to 25
    printf("Random number: %d\n", random_num);
}
```

Output (same each run with seed 42):
```commandline
Random number: 24
```

### Notes
- Using a fixed integer seed with `srand()` ensures the same sequence of random numbers every time the program runs with that seed.
- Different seeds produce different sequences, allowing controlled variation.
- The modulo operator (`%`) limits the range, as covered in the previous random number challenge.

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new C file in your home directory (choose any name).
2. Include the necessary headers (`<stdio.h>` and `<stdlib.h>`).
3. Declare an integer variable `seed` and get user input to initialize it with the prompt shown below.
4. Use `srand()` with the `seed` variable to initialize the random number generator.
5. Generate two random integers using `rand()` and store them in the following variables:
    - `rand_num1`: From 0 to 50 (inclusive).
    - `rand_num2`: From 0 to 15 (inclusive).
6. Print both random numbers in the format shown below.
7. Compile and run your program multiple times with the same seed to verify the numbers are consistent, and try different seeds to see different sequences.
8. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output (numbers depend on the seed, consistent for the same seed):
```commandline
Enter your seed: 42
Random number (0-50): 30
Random number (0-15): 4
```