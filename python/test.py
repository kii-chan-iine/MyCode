class Solution:
    def canJump(self, nums) -> bool:
        max_i=0
        for i,jump in enumerate(nums):
            if max_i>=i and i+jump>max_i:
                max_i=i+jump#更新
        return max_i>=i#如果小于，则到不了。
                
    

nums=[3,2,3,0,4,5]
# numRows=3
xx=Solution()
res=xx.canJump(nums)
print(res)