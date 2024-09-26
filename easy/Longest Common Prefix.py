strs = ["flower", "flow","fliw"]
common =""
for i in range(len(strs[0])):
    flag = False
    for j in range(1,len(strs)):
        if(i>=len(strs[j])):
            flag = True
            break
        if strs[0][i]==strs[j][i]:
            continue
        else:
            flag = True
            break
    if flag:
        break
    common+=strs[0][i]

print(common)