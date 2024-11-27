def sum(elements):
    total = 0
    for elem in elements:
        total+=elem
    return total
def average(elements):
    total = sum(elements)
    return round(total/len(elements), 3)

a = [3,2,5,2,56,15,7]

print(sum(a))
print(average(a))