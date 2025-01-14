### Compiling in C
Now that you have written a C program, you need to be able to run it and see the results! Remember that C code is written by humans, but the computer cannot understand it. We need to **compile** our C programs to translate it from human-readable C code into a computer-readable **executable**. An executable is a program that the computer is able to run (or execute). 
 
We can use the program `gcc` (the "GNU C compiler") to compile our C programs. For example, `gcc hello.c` would take a file named hello.c and compile it! We don't want to erase our C files, so gcc leaves your C file as is, and makes a second executable file from your original source code. This executable file is named `a.out` by default. If you run `ls` to view the files in your current directory, this `a.out` file will be listed. In many terminal setups, executable files will appear in green text, which indicates you can run them!
 
If your C file contains any **syntax errors**, gcc will not finish running, and will display either **errors** or **warnings**. **Syntax errors** are when your code is not formatted correctly - for example, missing a semicolon at the end of a line, mismatched parentheses, etc. A compiler **error** means that gcc could not finish compiling your program, and you will not have an executable file. A compiler **warning** means that something isn't quite right, but gcc was able to compile and create an executable. However, your executable may not behave as expected. gcc typically shows you the line number where the syntax error/warning occurred, and will often give you a hint on how to fix it. Note that gcc does not always find the true cause of the error, and the actual source may be a few lines above the one indicated. 
 
The compiler will not notice **logic errors**, which are when you wrote the code in the proper format, but your code will not solve the problem as intended. These programs will still compile and produce an executable, but they will not work as expected and may even crash. Logic errors are much harder to troubleshoot, as the compiler will not show you where the error occurs.
 
### Running programs
Compiling simply takes your C code and translates it into executable code. This code still isn't very useful to us until we run it. 
 
The command to run/execute a program is `./<your_executable>`. The first `.` means the executable is in your current directory, the `/` tells the computer to run the file. If you use gcc to compile your program, to run the executable will be `./a.out`. Then you will see the output of your program!

### Challenge Instructions
Follow these steps to complete the challenge!

1. Make sure you still have your "Hello World!" C file in your home directory.
2. Compile your C file using the command `gcc <your_file>.c` (replacing `<your_file>` with the name of your C file). This will automatically create an `a.out` executable file in your current directory.
3. To test your program, run `./a.out` to see the output from your program. 
4. To get the flag, run `verify` to validate your solution.  
