#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for p in params:
        if not p.endswith("ism"):
            print(p + "ism")

# ./append_it.py
#none$
#?> ./append_it.py "parallel" "egoism" "human"
#parallelism$
#humanism$

