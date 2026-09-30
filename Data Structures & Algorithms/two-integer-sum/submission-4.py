class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # corner case
        if len(nums) == 1 and nums[0] == target:
            return [0]

        indexed = sorted(enumerate(nums), key=lambda x: x[1])

        left = 0
        right = len(nums) - 1

        while left < right:
            total = indexed[left][1] + indexed[right][1]
            if total == target:
                if indexed[left][0] < indexed[right][0]:
                    return [indexed[left][0],indexed[right][0]]
                else:
                    return [indexed[right][0],indexed[left][0]]
            elif total < target:
                left +=1
            else:
                right -= 1
        



        