# Template for MicroPython Functional Equivalence Performance Evaluation
This is a very simple template to do a performance evaluation on two or more functionally equivalent MicroPython function.
The results are displayed in a table in the REPL

```
################################################################################
Function             Mean time (ms)       Median time (ms)     Mean Mem (KB)
================================================================================
Function 1           0.085211             0.088000             0.078125
Function 2           0.161575             0.162000             0.328125
################################################################################
```

## How to use
Copy the ```boot.py``` and ```comparison.py``` files to your MicroPython board and restart the REPL.

*The boot file allows you to also use .mpy files*
