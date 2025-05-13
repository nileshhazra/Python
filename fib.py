import time


def fib(num, memo={}):
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num in memo:  # Check if the result is already in the memo dictionary
        return memo[num]

    # Compute the Fibonacci number and store it in the memo dictionary
    memo[num] = fib(num - 1, memo) + fib(num - 2, memo)
    return memo[num]


start_time = time.time()

result = fib(40)

end_time = time.time()
print(result)

elapsed_time_ms = (end_time - start_time) * 1000

print(f"Time taken: {elapsed_time_ms:.2f} ms")
