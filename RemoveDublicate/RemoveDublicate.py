class Solution:
    def removeDuplicates(self, nums):
        count = 1

        for item in range(1, len(nums)):

            if nums[item] != nums[count - 1]:
                nums[count] = nums[item]
                count += 1

        return count
solution = Solution()
nums = [1,2,2,3,4,4,5]
result = solution.removeDuplicates(nums)
print(result)