#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # Get arguments, skip the script name itself
    args = sys.argv[1:]

    # Convert each argument to int and sum them
    total = sum(int(arg) for arg in args)

    # Print the result
    print(total)