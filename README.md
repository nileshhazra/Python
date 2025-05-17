# ☕ Python notebook

![Python](https://img.shields.io/badge/Python-%231E9FB4.svg?style=flat&logo=python&logoColor=white)

## Python Basics: Data Types, Data Structures, and Frequently Used Methods

### 1. Data Types

- **int**: Integer numbers  
  `x = 10`
- **float**: Floating-point numbers  
  `pi = 3.14`
- **complex**: Complex numbers  
  `z = 2 + 3j`
- **bool**: Boolean values  
  `is_active = True`
- **str**: Strings (text)  
  `name = "Alice"`
- **NoneType**: Represents no value  
  `value = None`

---

### 2. Data Structures

### List

Ordered, mutable collection  
`fruits = ["apple", "banana", "cherry"]`

**Common Methods:**

- `append(x)`
- `remove(x)`
- `pop([i])`
- `sort()`
- `reverse()`

#### Tuple

Ordered, immutable collection  
`coordinates = (10, 20)`

**Common Methods:**

- `count(x)`
- `index(x)`

#### Set

Unordered collection of unique items  
`unique_numbers = {1, 2, 3}`

**Common Methods:**

- `add(x)`
- `remove(x)`
- `union(other_set)`
- `intersection(other_set)`

#### Dictionary

Unordered collection of key-value pairs  
`person = {"name": "Alice", "age": 25}`

**Common Methods:**

- `keys()`
- `values()`
- `items()`
- `get(key, default)`
- `update(other_dict)`

#### Frozenset

Immutable set  
`frozen = frozenset([1, 2, 3])`

---

### 3. Frequently Used String Methods

- `lower()`: `"Hello".lower()` → `'hello'`
- `upper()`: `"Hello".upper()` → `'HELLO'`
- `strip()`: `"  hi  ".strip()` → `'hi'`
- `replace(old, new)`: `"hello world".replace("world", "Python")` → `'hello Python'`
- `split(sep)`: `"a,b,c".split(",")` → `['a', 'b', 'c']`
- `join(list)`: `",".join(['a', 'b', 'c'])` → `'a,b,c'`

---

### 4. Frequently Used List Methods

- `append(x)`
- `extend(iterable)`
- `insert(i, x)`
- `remove(x)`
- `pop([i])`
- `sort()`
- `reverse()`

---

### 5. Frequently Used Dictionary Methods

- `get(key, default)`
- `keys()`
- `values()`
- `items()`
- `update(other_dict)`
- `pop(key)`

---

### 6. Frequently Used Set Methods

- `add(x)`
- `remove(x)`
- `union(other_set)`
- `intersection(other_set)`
- `difference(other_set)`

---

### 7. Type Conversion

- `int(x)`, `float(x)`, `str(x)`, `list(x)`, `set(x)`, `dict(x)`

---

### 8. Useful Built-in Functions

- `len(x)`
- `type(x)`
- `range(start, stop, step)`
- `enumerate(iterable)`
- `zip(a, b)`

---

### 9. Example

```python
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Alice

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

text = "Hello, World!"
print(text.lower())  # 'hello, world!'
```

## Binary Search

```python
def search_insert(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        mid_val = nums[mid]
        if target == mid_val:
            return mid
        elif target > mid_val:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


res = search_insert([1, 2, 3, 4, 5], 10)
print(res)
```

The standard way to calculate `mid` in binary search is:

```python
mid = (left + right) // 2
```

This is efficient and works well in Python because Python integers can grow arbitrarily large, so integer overflow is not an issue.

**In some other languages** (like C, C++, or Java), using `(left + right) // 2` can cause integer overflow if `left` and `right` are very large. To avoid this, a safer way is:

```python
mid = left + (right - left) // 2
```

**In Python**, both methods are equally efficient and safe.  
There is no more efficient way than this for calculating `mid` in binary search. The main efficiency comes from the binary search algorithm itself, not from how `mid` is calculated.
