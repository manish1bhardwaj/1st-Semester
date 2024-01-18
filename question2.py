def strict_difference(ls):
    ans =[]
    for i in range (0, len(ls)-1):
        diff = abs(ls[i]-ls[i+1])
        ans.append(diff)
    return sorted(ans) == ans

arr = [1,2,5,-1]
re = strict_difference(arr)
print(re)
