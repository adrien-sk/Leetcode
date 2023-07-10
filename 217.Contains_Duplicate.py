class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        
        for val in nums:
            if val in mySet:
                return True            
            mySet.add(val)        
        return False
