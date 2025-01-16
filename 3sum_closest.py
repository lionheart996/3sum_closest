from typing import List
import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()  # Sort the list to use two-pointer technique
        closest_sum = float('inf')  # Initialize to infinity
        closest_diff = float('inf')  # Track the closest difference

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                # Update the closest sum if the current difference is smaller than the closest difference found so far
                if current_diff < closest_diff:
                    closest_diff = current_diff
                    closest_sum = current_sum

                # Move the pointers based on the comparison
                if current_sum < target:
                    left += 1  # Need a larger sum
                elif current_sum > target:
                    right -= 1  # Need a smaller sum
                else:
                    return target  # Exact match found, no need to proceed further

        return closest_sum  # Return the closest sum found


nums = [-1,2,1,-4]
target = 1

nums1 = [0,0,0]
target1 = 1

print(Solution().threeSumClosest(nums, target))
print(Solution().threeSumClosest(nums1, target1))