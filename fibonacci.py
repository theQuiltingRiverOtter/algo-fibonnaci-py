def fibonacci(n):
    nums = [0, 1]
    if n == 0:
        return nums[0]
    for i in range(1, n):
        nums.append(nums[-1] + nums[-2])
    return nums[-1]


def r_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return r_fibonacci(n - 1) + r_fibonacci(n - 2)
