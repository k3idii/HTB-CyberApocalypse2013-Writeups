# misc:: nehebkaus trap

## The problem statement
After connecting to the socket given in the challenge, we are presented a command line with ability to enter commands. 
After investigation, it seems to be python code exectution, but the input is filtered for the following badchars: `./;',_"` and space.


## The solution
Thankfully there is an `exec()` function in python, that allows to execute python code that comes as input :) 

So that:
- first input: `exec(input())`
- second input: `print(open("flag.txt").read())`

Done. 

