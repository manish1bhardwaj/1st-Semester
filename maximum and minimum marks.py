marks = {
    "physics" : 20, 
    "maths"   : 24,
    "english" : 19,
    "aiml"    : 25,
    "python"  : None,
    "webtech" : 23

 }
# data cleaning (remove all unnecessary keys)
for key , val in (marks.items()):
    if type (val) != int:
        marks.pop(key)
        

values = marks.values()
max_marksValue = max(values)
min_marksValue = min(values)

subject_maxMarks = []
subject_minMarks = []

for key , val in marks.items():
    if max_marksValue == val:
        subject_maxMarks.append(key)

    if min_marksValue == val:
        subject_minMarks.append(key)

print("Maximum:", subject_maxMarks,)        

print("Minimum:", subject_minMarks,)  