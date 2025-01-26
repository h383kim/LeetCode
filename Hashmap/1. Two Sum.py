################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/two-sum
################################################################


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in seen_dict: # Look up the dict if the diff is seen
                return [idx, seen_dict[diff]] # If seen, spotted the answer
            else: # Else, add the seen num with its index
                seen_dict[num] = idx


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numsIndexed = []
#         for idx, num in enumerate(nums):
#             numsIndexed.append((num, idx))

#         sorted_nums = sorted(numsIndexed, key=lambda x: x[0])

#         left, right = 0, len(nums) - 1
#         while left < right:
#             Sum = sorted_nums[left][0] + sorted_nums[right][0]
#             if Sum < target:
#                 left += 1
#                 continue
#             elif Sum > target:
#                 right -= 1
#                 continue
#             else:
#                 return [sorted_nums[left][1], sorted_nums[right][1]]
        