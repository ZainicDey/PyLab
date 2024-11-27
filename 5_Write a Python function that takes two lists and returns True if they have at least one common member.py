def mil_paise(a,b):
    for e in b:      
        if e in a:
            return True
    return False      
a = [1,2,3,4,1,7]
b = [2,9,8,2,5,6]

if mil_paise(a,b):
    print("Mil paise")
else:
    print("Mil painai")