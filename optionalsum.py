def optional_sum(*cf,ob='Add'):
    if ob == 'Add':
        s=0
        for i in cf:
            s+=i
        return s
    elif ob=='Mul':
        s=1
        for i in cf:
            s*=i
        return s
out = optional_sum(3,4,4,ob="Mul")
print(out)
    