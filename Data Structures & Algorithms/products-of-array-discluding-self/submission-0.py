class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_mul = [0]*n
        post_mul = [0] * n
        pre_mul[0] = 1
        post_mul[-1] = 1
        for i in range(1,len(nums)):
            pre_mul[i] = pre_mul[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            post_mul[j] = post_mul[j+1] * nums[j+1]
        for k in range(n):
            ans[k] = pre_mul[k] * post_mul[k]
        return ans
