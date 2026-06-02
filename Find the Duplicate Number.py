#LeetCode #287 — Find the Duplicate Number
def findDuplicate(nums):

    slow = nums[0]
    fast = nums[0]

    # Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Find entrance of cycle
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]

print(findDuplicate(nums))
