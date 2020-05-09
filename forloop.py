# Iterable - list,dictonary, tuple,set, string
# iterate - one by one check each item in the collection,
list = [1,2,3,4,5]

for i in list:
    print(i)


user = {
    'name':'Dattatray',
    'age':5006,
    'can_swim':False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for k, v in user.items():
    print(k, v)

