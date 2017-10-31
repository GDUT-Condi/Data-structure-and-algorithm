def Quick_Sort(nums, left, right):
    if left >= right:
        return nums
    temp = nums[left]
    i = left
    j = right
    while i < j:
        while nums[j] > temp and i < j:
            j -= 1

        while nums[i] <= temp and i < j:
            i += 1

        if i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

    nums[left] = nums[i]
    nums[i] = temp
    Quick_Sort(nums, left, i - 1)
    Quick_Sort(nums, i + 1, right)
    return nums


nums = [15, 11, 3, 51, 36, 42, 12, 17, 15, 32, 2, 3]
left = 0
right = len(nums) - 1
print(Quick_Sort(nums, left, right))
