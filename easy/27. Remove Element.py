def removeElement( nums, val: int) -> int:
    k=0
    len_nums= len(nums)
    for i in range(len(nums)):
        if(nums[i]==val):
            k+=1
            j=len(nums)
            while nums[j]==val:
                j-=1
            nums[i]=nums[j]
    print(nums)
    return k

removeElement([3,2,2,3],3)
                



 

    




