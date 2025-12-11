#!/usr/bin/env python
import hidden_4

if __name__ == "__main__":
    # dir() lists all names in the module
    names = dir(hidden_4)

    # Filter out names starting with "__" and sort
    for name in sorted(n for n in names if not name.startswith("__")):
        print(name)
