# Key = age, Value = weight
data = {
    25: 175,
    30: 180,
    20: 160,
    35: 170
}

#ki onujayi sort hobe shetar ekta compare function
def sum_key(item):
    return item[0] + item[1]        #protita dict. item jehetu ekekta tuple, amra 0 index ta key and 1 index ta value hishebe pai

#new dictionary te rakhbo sorted obosthai
sorted_data = dict(sorted(data.items(), key=sum_key)) #ekhane key diye amader icchamoto sort korate parbo..function a jevabe chai

print(sorted_data)