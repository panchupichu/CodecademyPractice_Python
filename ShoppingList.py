"""Shoppping List Practice
   List/Dictionary/Control Flow
   Python 3 debugged with Thonny
"""
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

for i in prices:
    print(i)
    print(prices[i])
    print(stock[i])
    
print( )

total = 0
for i in prices:
    sales = prices[i]*stock[i]
    print('Sales of %s: %s' % (i, sales))
    total += sales

print(total)

print( )

shopping_list = ['banana', 'orange', 'apple']


food = shopping_list
def compute_bill(food):
    totalbill = 0
    for item in food:
        if stock[item] > 0:
            totalbill += prices[item]
            stock[item] -= 1
    return totalbill

print('Total Bill: %s' % compute_bill(shopping_list))
