def lengthOfLastWord( s: str) -> int:
    arr= s.strip().split(" ")
    return len(arr[len(arr)-1])
    



print(lengthOfLastWord("   fly me   to   the moon  "))