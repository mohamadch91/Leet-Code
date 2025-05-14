def searchInsert( nums, target: int):
    pivot = int(len(nums)/2)
    if(target == nums[pivot]):
        return pivot
    if(len(nums)==1):
        if(target>nums[0]):
            return 1
        else:
            return 0
    if(len(nums)==2):
        if(target>nums[1]):
            return pivot+1
        if (target < nums[0]):
            return 0
        if(target>nums[0] and target<nums[1]):
            return pivot
    if(target<nums[pivot]):
        return searchInsert(nums[:pivot],target)
    if(target>nums[pivot]):
        return pivot+searchInsert(nums[pivot:],target)

    





print(searchInsert(nums = [1], target = 0))