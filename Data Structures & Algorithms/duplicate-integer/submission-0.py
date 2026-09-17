class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counter = Counter()
        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True

        return False