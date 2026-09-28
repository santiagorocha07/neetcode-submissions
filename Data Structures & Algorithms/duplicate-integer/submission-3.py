class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        set_res = set()
        for i in range(len(nums)):
            if nums[i] in set_res:
                return True
            else:
                set_res.add(nums[i])
        return False

