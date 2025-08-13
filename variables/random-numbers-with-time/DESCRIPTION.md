### Seeding Random Numbers with Time
Using a fixed value for the seed will result in the same output every time the program is run. To get unique output (nearly) every time, we can add in the `time()` function. 
Rather than using the same seed value each time, we will learn how to use the current time as the seed! Because time changes every second, our seed will also change each second, resulting in 
different output.

### The `time()` function
- Include `<time.h>` library
- When `time(NULL)` is called, it returns the current time in seconds, since January 1, 1970 (the Unix epoch)
    - for example, if you called `time()` at 9:45am on Aug 13, 2025, it would return `1755080700` - the number of seconds from Jan 1, 1970 until that moment
    - the `NULL` means we are not sending anything to the `time()` function, which is what we want in this case
- Rather than storing the time in a variable, we will actually just call it from _within_ the `srand()` function
    - `srand( time(NULL) )` will first call `time(NULL)`, then take whatever value it returns (the time in seconds), and send _that_ value to be our seed in `srand()`
    - this will result in a different seed being used each time the program runs (unless you run your program multiple times in the same second!)
    - with the time as a seed, your output will start to look random!

### Notes
- Truly **random** numbers are very hard to generate. These are _pseudo-random_ numbers, they look random but can be predicted (given enough time and effort).
- Remember, only call `srand()` **one time**, at the top of main. Calling it again will reset the sequence.

### Challenge Instructions 
Follow these steps to complete this challenge!

1. Create a new C file in your home directory, or build on your file from the previous challenge (choose any file name).
2. Include the necessary headers (`<stdio.h>`, `<stdlib.h>`, and `<time.h>`).
3. Seed the random number generator with the current time (`srand( time(NULL) );`) - Note that you do not need a `seed` variable for this program.
4. Generate two random integers using `rand()` and store them in the following variables (same as the last challenge):
    - `rand_num1`: From 0 to 50 (inclusive).
    - `rand_num2`: From 0 to 15 (inclusive).
5. Print both random numbers in the format shown below.
6. Compile and run your program multiple times to see the different numbers that were generated! Try running `./a.out` twice as fast as you can - you might get the same numbers if you run both within the same second!
8. To get the flag, run `/challenge/verify <yourfile>.c` to verify your solution.

Example output (will be different than shown, due to seeding with time):
```
Random number (0-50): 23
Random number (0-15): 7
```
