def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    output = len(nums) * [1]
    prod = 1
    for i, n in enumerate(nums):
        output[i] *= prod
        prod *= n
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= prod
        prod *= nums[i]

    return output