from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.k=[]
        sum=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            self.k.append(sum)
            
        

    def sumRange(self, left: int, right: int) -> int:
        if left>0 and right>0:
            return self.k[right]-self.k[left-1]
        else:
            return self.k[left or right]
nums = [1, 2, 3, 4, 5]
obj = NumArray(nums)
print(obj.sumRange(1, 3))
print(obj.sumRange(0, 3))
print(obj.sumRange(2, 4))
print(obj.sumRange(0, 4))