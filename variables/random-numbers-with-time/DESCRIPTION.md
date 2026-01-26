### Seeding Random Numbers with Time in C

In the previous challenges, we used `rand()` to generate pseudo-random numbers and `srand()` with a fixed seed for reproducible sequences. But what if you want truly different random numbers each time your program runs? The solution is to use the current time as a seed!

The `<time.h>` library provides the `time()` function, which returns the current time as the number of seconds since January 1, 1970 (known as the Unix epoch). Since this value changes every second, it makes an excellent seed for generating unique random sequences.

### Using `time()` with `srand()`
- **Include `<time.h>`**:
    - Provides the `time()` function to get the current time.
- **Getting the Current Time**:
    - `time(NULL)` returns the current time as a `time_t` value (number of seconds since the Unix epoch).
    - Passing `NULL` means we don't need to store the time in a separate variable.
- **Seeding with Time**:
    - Use `srand(time(NULL))` to seed the random number generator with the current time.
    - Each time you run the program (at least one second apart), you'll get a different sequence of random numbers.
- **Generating Random Numbers**:
    - After seeding, use `rand()` as before to generate random numbers.
    - To get a random number from `0` to `max` (inclusive), use: `rand() % (max + 1)`.

Example:
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL)); // Seed with current time
    int random_num = rand() % (100 + 1); // Random number from 0 to 100
    printf("Random number: %d\n", random_num);
}
```

Output (different each time you run):
```commandline
Random number: 47
```

### Notes
- Using `time(NULL)` as a seed ensures different random sequences each time the program runs.
- Call `srand(time(NULL))` only once at the beginning of `main()`. Calling it multiple times can reduce randomness.
- If you run the program twice within the same second, you may get the same sequence since the seed would be identical.
- The `time_t` type returned by `time()` is automatically cast to an `unsigned int` when passed to `srand()`.

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new C file in your home directory (choose any name).
2. Include the necessary headers (`<stdio.h>`, `<stdlib.h>`, and `<time.h>`).
3. Use `srand()` with `time(NULL)` to seed the random number generator with the current time.
4. Generate two random integers using `rand()` and store them in the following variables:
    - `rand_num1`: From 0 to 25 (inclusive).
    - `rand_num2`: From 0 to 1000 (inclusive).
5. Print both random numbers in the format shown below.
6. Compile and run your program multiple times to verify you get different numbers each time.
7. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output (your numbers will be different each run):
```commandline
Random number (0-25): 17
Random number (0-1000): 583
```
