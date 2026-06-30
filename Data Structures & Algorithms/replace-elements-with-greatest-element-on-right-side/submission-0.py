class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        max_int=-1
        for i in range(n-1,-1,-1):
            ans[i]=max_int
            max_int=max(max_int,arr[i])

        return ans