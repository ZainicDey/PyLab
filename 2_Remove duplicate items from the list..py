a = [1,2,3,4,3,5,6,1] #1 and 3 2bar ache
new_a = [] #unique value gula new list a rakhbo

for i in range(0, len(a)):
    if a[i] not in new_a: #a[i] ei value ta jodi thake taile add korbo na new list a
        continue
    else:                 #na thakle add korbo
        new_a.append(a[i])

print(new_a)