# dct =  {1:'one',2:'two',3:'three'}
# # out = dct.get(4,'nahi hai')
# out = dct.get(1)
# print(out)


def display_info(**dct):
    return f'''
Name       :{dct.get('name')}
Section    :{dct.get('section')}
Roll number:{dct.get('rollno')}
College    :{dct.get('college')}
'''


data = display_info(name='Ravi',rollno=25)
print(data)


    