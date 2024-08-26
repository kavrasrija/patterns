from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            com=target-nums[i]
            if com in d:
                return [d[com],i]
            if nums[i] not in d:
                d[nums[i]]=i
        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [4,3,7,6,1]
    k=7
    print(sol.twoSum(nums,k))