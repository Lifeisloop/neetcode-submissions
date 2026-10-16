class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for x in nums:
            if  x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        sorted_nums = sorted(freq, key = lambda x: freq[x], reverse=True)

        for x in range(k):
            ans.append(sorted_nums[x])

        return ans