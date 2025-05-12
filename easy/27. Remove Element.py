def removeElement( nums, val: int) -> int:
    k=0
    j_arr=[]
    for i in range(len(nums)):
        if(i in j_arr):
            continue
        if(nums[i]!=val):
            k+=1
        if(nums[i]==val ):
            j=len(nums)-1
            while nums[j]==val and j>i:
                j_arr.append(j)
                j-=1
            if(nums[j]!=val):
                k+=1
                nums[i]=nums[j]
                nums[j]=val

    return k

removeElement([3,2,2,3],3)
                



 

    




