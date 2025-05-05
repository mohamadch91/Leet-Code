


def isValid( s: str) -> bool:
    dict ={
        "{": False,
        "[": False,
        "(": False
    }
    dict1 ={
        "}": "{",
        "]" : "[",
        ")": "(",

    }
    array=[]

    for i in s:
        
        if i in dict:
            dict[i]= True
            array.append(i)
        else:
            if(len(array)==0):
                return False
            word=dict1[i]
            last = array.pop()
            if  word==last :
                dict[word]=False
            else:
                return False
    if(len(array)!=0):
        return False
    if (dict["("] or dict["{"] or dict["["] ):
        return False
    return True


print(isValid("(([]){})"))