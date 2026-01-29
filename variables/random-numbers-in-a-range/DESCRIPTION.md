### Generating Random Numbers in a Custom Range

In the previous challenges, we learned how to generate random numbers from `0` to a maximum value using `rand() % (max + 1)`, and how to seed the random number generator with `time(NULL)` for different sequences each run. But what if you need a random number that starts at a value other than `0`? For example, what if you want a random number between `10` and `20`?

This challenge introduces how to generate random numbers within a custom range, where both the minimum and maximum values can be any integer.

### The Range Formula

To generate a random number from `min` to `max` (inclusive), use the following formula:

```text
random_num = rand() % (max - min + 1) + min;
```

**How it works:**
- `(max - min + 1)` calculates the total number of possible values in the range.
- `rand() % (max - min + 1)` gives a random number from `0` to `(max - min)`.
- Adding `min` shifts the range up so the result is from `min` to `max`.

**Example breakdown:**
- To get a random number from `10` to `20`:
  - Range size: `20 - 10 + 1 = 11` (the values 10, 11, 12, ..., 20)
  - `rand() % 11` gives a number from `0` to `10`
  - Adding `10` shifts it to `10` to `20`

Example:
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL)); // Seed with current time
    int random_num = rand() % (20 - 10 + 1) + 10; // Random number from 10 to 20
    printf("Random number (10-20): %d\n", random_num);
}
```

Output (different each run):
```commandline
Random number (10-20): 14
```

### Notes

- Always seed the random number generator with `srand(time(NULL))` at the start of `main()` for different sequences each run.
- The formula `rand() % (max - min + 1) + min` works for any range where `min <= max`.
- Make sure to include `<time.h>` for `time()`, `<stdlib.h>` for `rand()` and `srand()`, and `<stdio.h>` for `printf()`.
- This technique is useful for games (dice rolls, card draws), simulations, and any situation where you need random values within specific bounds.

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new C file in your home directory (choose any name).
2. Include the necessary headers (`<stdio.h>`, `<stdlib.h>`, and `<time.h>`).
3. Use `srand()` with `time(NULL)` to seed the random number generator.
4. Generate three random integers using `rand()` and the range formula, stored in the following variables:
    - `rand_num1`: From 1 to 10 (inclusive).
    - `rand_num2`: From 50 to 100 (inclusive).
    - `rand_num3`: From -5 to 5 (inclusive).
5. Print all three random numbers in the format shown below.
6. Compile and run your program multiple times to verify you get different numbers each time, all within the correct ranges.
7. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output (your numbers will be different each run):
```commandline
Random number (1-10): 7
Random number (50-100): 83
Random number (-5 to 5): -2
```
