"""Find the two numbers in the list provided that sum to the target number."""

nums = [1,2,3,4,5,6]
target = 6

def find_pair(nums, target):

    for num in nums:
        num2 = target - num

        if num2 in nums:
            return [num, num2]

print(find_pair(nums, target))


"""Same thing, but return ALL pairs of solutions."""

nums = [1,2,3,4,5,6]
target = 6

def find_pair(nums, target):

    pairs = []
    for num in nums:

        num2 = target - num

        # Once halfway is reached, return
        if nums.index(num) > len(nums) / 2 - 1:
            return pairs

        if num2 in nums:
            pairs.append([num, num2])


print(find_pair(nums, target))