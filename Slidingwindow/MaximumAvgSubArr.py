from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n=len(nums)
        r=k-1
        l=0
        curr = sum(nums[:k])
        maxsum = curr
        while(r<n-1):
            curr=curr-nums[l]
            l+=1
            r+=1
            curr=curr+nums[r]
            maxsum=max(maxsum,curr)
        return maxsum/k
    
if __name__ == "__main__":
    sol = Solution()
    arr = [4,3,7,6,1]
    k=3
    
    print(sol.findMaxAverage(arr, k))