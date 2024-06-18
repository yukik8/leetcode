class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return 'No solution'


nums = input('nums = ')
inputnums = [int(item) for item in nums.split(',')] #LeetCode上でエラー発生
target = int(input('target = '))
answer = Solution().twoSum(inputnums, target)
print(answer)