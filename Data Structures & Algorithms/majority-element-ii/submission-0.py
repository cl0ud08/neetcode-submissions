class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = {}
        n = len(nums)

        for num in nums:
            res[num] = res.get(num, 0) + 1

        ans = []

        for num, count in res.items():
            if count > n // 3:
                ans.append(num)

        return ans