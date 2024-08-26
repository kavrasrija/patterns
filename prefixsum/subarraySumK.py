from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixsum = 0
        d = {0: 1}
        
        for num in nums:
            prefixsum += num
            
            if (prefixsum - k) in d:
                result += d[prefixsum - k]
            
            if prefixsum not in d:
                d[prefixsum] = 1
            else:
                d[prefixsum] += 1
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 1]
    k = 5
    print(sol.subarraySum(nums, k))  # Should print 2

        