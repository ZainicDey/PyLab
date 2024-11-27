d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}                             

for e in d1:                   
    if e in d2:                 #jodi same item 2ta dictionary te thake taile new dictionary te 2tar value er jogfol rakhbo
        d3[e] = d1[e] + d2[e]
    else:
        d3[e] = d1[e]           #ar naile just insert korbo

for e in d2:                    #2nd dictionary er unique je pair gula ache ta insert korte hobe new dictionary te
    if e not in d1:             
        d3[e] = d2[e]

print(d3)