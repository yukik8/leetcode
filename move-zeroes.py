class Solution:
    def moveZeroes(self, nums) -> None:
        ans = []
        zerocount = 0
        j = 0
        for i in nums:
            if i == 0:
                zerocount += 1
            else:
                ans.append(i)
        for j in range(zerocount):
            ans.append(0)
        print(ans)

Solution().moveZeroes(nums=[0, 1, 0, 3, 12])