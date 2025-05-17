# binary search
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
