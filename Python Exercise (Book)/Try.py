allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        print('k:'+ k +' ', 'v:' + str(v))
        print(v.get(item, 0))
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print(totalBrought(allGuests, 'apples'))