# Find Target Indices After Sorting Array

def target_indices(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result