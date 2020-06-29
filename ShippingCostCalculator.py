""" Shipping Cost Calculator
    Exercise: List/Dictionary/Control Flow
    Python 3 debugged with Thonny
"""
# Create a dictionary for price list
prices = {
    'ground' : [20.00, 1.50, 3.00, 4.00, 4.75],
    'drone' : [0.00, 4.50, 9.00, 12.00, 14.25],
    'premium' : 125.00
    }

# Calculate cost for Ground Shipping
def cost_ground(weight):
    flat = prices['ground'][0]
    if weight <= 2:
        cost = weight*(prices['ground'][1]) + flat
    elif weight <= 6:
        cost = weight*(prices['ground'][2]) + flat
    elif weight <= 10:
        cost = weight*(prices['ground'][3]) + flat
    else:
        cost = weight*(prices['ground'][4]) + flat
    return cost
#test function
print(cost_ground(8.4))

# Calculate cost for Drone Shipping
def cost_drone(weight):
    flat = prices['drone'][0]
    if weight <= 2:
        cost = weight*(prices['drone'][1]) + flat
    elif weight <= 6:
        cost = weight*(prices['drone'][2]) + flat
    elif weight <= 10:
        cost = weight*(prices['drone'][3]) + flat
    else:
        cost = weight*(prices['drone'][4]) + flat
    return cost
# Test function
print(cost_drone(1.5))

# Calculate cost for Premium Shipping
def cost_premium(weight):
    cost = prices['premium']
    return cost
# Test function
print(cost_premium(100.00))

# Determine which shipping methond is the cheapest
def find_cheapest(weight):
    A = cost_ground(weight)
    B = cost_drone(weight)
    C = cost_premium(weight)
    if A < B and A < C :
        print("Cheapest for %d lb: Ground. Cost: $ %d" % (weight, A))
    elif B < A and B < C :
        print("Cheapest for %d lb: Drone. Cost: $ %d" % (weight, B))    
    else:
        print("Cheapest for %d lb: Premium. Cost: $ %d" % (weight, C))
    return("Thank you for shipping with us!")

#test function
print(find_cheapest(4.8))
print(find_cheapest(41.5))
