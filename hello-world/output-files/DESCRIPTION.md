### Compiling with Output Files
You may remember that `gcc` names the executable file "a.out" by default. Because the executable name is always the same, each time you compile a new program, or re-compile the same program, your old `a.out` will be overwritten by the new `a.out`. Typically this is fine, since you can always recompile your source code and make a new file. If you have your C file, you can make a new `a.out` at any time! If you delete your C file, you cannot get it back, even if you havet the `a.out` file! Sometimes, you may want to keep multiple executables from your programs. One easy way is to just rename your `a.out` file to something else. Another way is to use `gcc` to name the output file when you compile it!
 
To give `gcc` a different **output file** name, we can use the `-o` flag. For example, to name the executable "my_output", we can use the command `gcc hello.c -o my_output`. 

Note: If you make changes to your C file, you will need to re-compile it for your executable to have the most recent changes.

### Running Output Files

To run an output file with a different name, we still just use the `./<executable_name>` command. For the example above, to run the "my_output" file, we can use `./my_output`.  

### Challenge Instructions
Follow these steps to complete the challenge!
 
1. Make sure you still have your "Hello World!" C file in your home directory.
2. Compile your C file and name the output file "hello" using the command `gcc <your_file>.c -o hello` (replacing <your_file> with the name of your C file).
3. To test your program, run `./hello` to see the output from your program.
4. To get the flag, run `verify` to validate your solution. 
