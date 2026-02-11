#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
result_set = set()

for num in original_array:
    result_set.add(num + 2)

print(original_array)
print(list(result_set))

#[2, 8, 9, 48, 8, 22, -12, 2]
#{24, 10, 11, 50}