### Generating Random Numbers in C
In C, generating random numbers is useful for simulations, games, or testing. The C standard library (`<stdlib.h>`) provides the `rand()` function to generate pseudo-random numbers. This challenge focuses on using `rand()` to produce random integers up to a specified maximum value.

### Using `rand()`
- `rand()`: Generates a pseudo-random integer between `0` and `RAND_MAX` (a large constant defined in `<stdlib.h>`). You need to include the `<stdlib.h>` library to use it.
- **Range Limiting**: To generate a random number from `0` to a maximum value `max` (inclusive), use the formula:
    ```text
    random_num = rand() % (max + 1);
    ```
    This produces a random integer from `0` to `max`. Just doing `rand() % max` would give you a number between `0` and `max - 1` since `max % max` equals `0`.
- **Note**: Without seeding, `rand()` produces the same sequence of numbers each time the program runs. For this challenge, we’ll use the default sequence and cover seeding in a future challenge.

Example:
```C
#include <stdio.h>
#include <stdlib.h>

int main() {
    int random_num = rand() % (10 + 1); // Random number from 0 to 10
    printf("Random number: %d\n", random_num);
}
```

Output (same sequence each run, e.g.):
```commandline
Random number: 6
```

### Notes
- The modulo operator (`%`) is used to limit the range of the random number.
- Since we're not seeding the random number generator in this challenge, the sequence of numbers will be predictable and repeat each time the program runs.

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new C file in your home directory (choose any name).
2. Include the necessary headers (<stdio.h> for printf() and <stdlib.h> for rand()).
3. Generate two random integers using rand() stored in the following variables:
    * `rand_num1`: From 0 to 100 (inclusive).
    * `rand_num2`: From 0 to 75 (inclusive).
4. Print both random numbers in the format shown below.
5. Compile and run your program to test it.
6. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output (your numbers will be different than example but consistent each run due to no seeding):
```commandline
Random number (0-100): 6
Random number (0-75): 12
```