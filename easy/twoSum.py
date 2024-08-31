class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define a dictionary for saving each number in the list and its index
        dict ={}
        for i in range(len(nums)):
            diff = target - nums[i]
            # if we saw the diffrence 
            if(diff in dict):
                # return index of diffrence and i
                return [dict[diff],i]
            # save the index
            dict[nums[i]] = i