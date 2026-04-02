class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        count = 1
        n = len(nums)
        if n == 0: return 0
        arr= set(nums)
        ar1 = list(arr)
        print(ar1)
        ar1.sort()
        for i in range(1,len(ar1)):
            if ar1[i] - 1 == ar1[i-1]:
                count += 1
            else:
                ans = max(ans,count)
                count = 1
        ans = max(ans,count)   
        return ans