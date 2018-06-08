# dbug.py

dbug runs your script, and wherever it runs into an exception/error, gives you access to the 
frames and opens the bpython shell right there, giving you access to the variables. 
After fixing your code, you can run `reload()` to test again. 

## Dependencies
bpython: https://github.com/bpython/bpython

## Usages
`python -m dbug <your script>`

`python -m dbug <your script>:<line number>`

## Functions inside the debugger
`select(frame_no)`: Selects a frame given a frame number and opens the shell inside

`reload()`: reload the original script
