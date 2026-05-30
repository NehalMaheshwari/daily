#LeetCode #238 — Product of Array Except Self
def productExceptSelf(nums):
    n = len(nums)

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


nums = [1, 2, 3, 4]

print(productExceptSelf(nums))
