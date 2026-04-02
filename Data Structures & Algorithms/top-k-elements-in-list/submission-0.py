class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        arr_count = Counter(nums)
        arr = [[count,i] for count,i in arr_count.items()]
        arr.sort(key = lambda x:x[1],reverse = True)
        print(arr)
        for i in range(k):
            ans.append(arr[i][0])
        return ans