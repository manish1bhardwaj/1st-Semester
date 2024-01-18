def union(ls1,ls2):
    for i in ls1:
        for j in ls2:
            if i==j:
                ls.append(i)
    return ls1+ls
               
def intersection(ls1,ls2):
    for i in ls1:
        for j in ls2:
            if i==j and i not in ls:
                ls.append(i)
    return ls
               
def symmetric_difference(ls1,ls2):
    for i in ls:
        ls1.remove(i)
        ls2.remove(i)
    return ls1+ls2
    return ls2+ls2

ls1 = [1,2,3,5]
ls2 = [2,5,90]
ls = []
print(union (ls1,ls2))
print(intersection(ls1,ls2))
print(symmetric_difference(ls1,ls2))

