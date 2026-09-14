class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Base case
        if len(nums) <= 1:
            return nums

        # Divide
        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        # Recursively sort
        left = self.sortArray(left)
        right = self.sortArray(right)

        # Merge
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                res.append(left[i])
                i += 1

            else:
                res.append(right[j])
                j += 1

        # Remaining elements
        res.extend(left[i:])
        res.extend(right[j:])

        return res