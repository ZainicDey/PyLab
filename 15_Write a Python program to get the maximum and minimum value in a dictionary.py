a = {
    1: 1,
    2: 4,
    55: 5,
    3: 9,
    16: 33,
    5: 63,
    6: 35,
    10: 400,
    20: 100
}
sorted_a = []
for e in a.values():  
    sorted_a.append(e)

sorted_a.sort()               #ekta list a  niye sort  korbo value gula, jate [1,2,2,3,5,6,8] evabe thake

print('mininmum value is', sorted_a[0])
print('maximum value is', sorted_a[len(sorted_a) -1])
        
