#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print(f"parameters: {len(params)}")
    for p in params:
        print(f"{p}: {len(p)}")

# ./count_it.py 
#none$
#?> ./count_it.py "Game" "of" "Thrones" 
#parameters: 3$
#Game: 4$
#of: 2$
#Thrones: 7$