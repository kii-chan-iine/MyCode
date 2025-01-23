class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for x in range(n):
            a = target - nums[x]
            if nums[x] in d:
                return d[nums[x]], x
            else:
                d[a] = x


nums = [1, 7, 11, 3, 9, 6, 15]
target = 9
te = Solution()
results = te.twoSum(nums, target)
print(results)


#%%  更好的方法

class Solution1:
    def ts(self,nums,target):
        d={}
        for i,num in enumerate(nums,start=0):
            if num in d:
                return d[num],i
            else:
                d[target-num]=i
nums = [1, 7, 11, 3, 9, 6, 15]
target = 9
te1 = Solution1()
results = te1.ts(nums, target)
print(results)