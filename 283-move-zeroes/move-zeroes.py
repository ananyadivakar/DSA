class Solution(object):
    def moveZeroes(self, nums):
        insertPos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertPos], nums[i] = nums[i], nums[insertPos]
                insertPos += 1