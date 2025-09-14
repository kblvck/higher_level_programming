#!/usr/bin/env python
import sys

def main():
    argv = sys.argv
    argc = len(argv) - 1  # exclude script name

    # First line
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")

    # Print arguments if any
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    main()
