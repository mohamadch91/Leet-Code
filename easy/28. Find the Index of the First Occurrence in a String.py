def strStr( haystack: str, needle: str) -> int:
    len_needle=len(needle)
    index=0
    flag=False
    while index<len(haystack):
        new_str= haystack[index:index+len_needle]
        if(new_str==needle):
            flag=True
            break
        index+=1
            
    if not flag:
        return -1
    return index



print(strStr("leetcode","leeto"))