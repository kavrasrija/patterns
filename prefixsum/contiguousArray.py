from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans, cnt, pref = 0, 0, {0: -1}
        for i, num in enumerate(nums):
            cnt += 1 if num else -1
            if cnt in pref:
                ans = max(i - pref[cnt], ans)
            else:
                pref[cnt] = i
        return ans

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 1, 1, 0, 1, 0]
    print(sol.findMaxLength(nums))

        
        