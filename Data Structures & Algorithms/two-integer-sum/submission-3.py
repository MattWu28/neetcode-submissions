class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while True: #not infininte loop b/c pair is guaranteed
            if nums[i] + nums[j] == target:
                return [i,j]
            elif j != len(nums) - 1:
                j += 1
            else:
                i += 1
                j = i+1 