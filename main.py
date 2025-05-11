print('hello world!')
import sys

arr = []
for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}, Size in bytes: {sys.getsizeof(arr)}")

import array

arr = array.array('i', [1, 2, 3, 4])  # 'i' = signed int
print(arr)
arr.append(5)
arr.insert(2, 10)
print(arr)
# This enforces all elements to be integers, offering better performance and less memory than lists.
# Use array.array when you need strict typing and space optimization.

import sys
print(sys.getsizeof([1, 2, 3]))  # Size in bytes
