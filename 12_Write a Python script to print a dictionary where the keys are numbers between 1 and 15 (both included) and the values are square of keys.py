a = {
    1: 1,
    2: 4,
    55: 5,
    3: 9,
    16: 33,
    5: 63,
    6: 35,
    10: 100,
    20: 400
}
#20 er square 400 but show korbe na, 6 er square 35 na, show korbe na

for e in a.items():
    if e[0]>0 and e[1] < 16:
        if e[0] * e[0] == e[1]:
            print(e)