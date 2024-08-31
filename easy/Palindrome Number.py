
def isPalindrome( x: int) -> bool:
    b = 0 
    z=x
    if(x<0):
        return False
    while(z>0):
        b = b*10 + z%10
        z = z//10
    return b == x





print(isPalindrome(121))