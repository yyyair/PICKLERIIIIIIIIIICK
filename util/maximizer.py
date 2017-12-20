import math
h = lambda ATK, DEF, OBJ: ATK * DEF * math.atan(OBJ)

class KnapsackObject:
    def __init__(self, value, weight, type):
        self.value = value
        self.weight = weight
        self.type = type

    def efficiency(self):
        return h(self.weight[0], self.weight[1], self.weight[2])/float(sum(self.weight))

    def __str__(self):
        return "{" + str(self.value) + "," + str(self.weight) + "," +  str(self.efficiency())+"}"


"""
Finds a subset S of objs such that the sum value of S is maximal
:param objs: Objects
:param limits: Knapsack cieling weight values
"""
def knapsack(objs, limits):
    objs = sort(objs)
    sack = []
    sackObjs = []
    currentWeight = [0] * len(limits)
    for obj in objs:
        newWeight = [currentWeight[i] + obj.weight[i] for i in range(min(len(obj.weight), len(currentWeight)))]
        if obj.type in sack:
            pass
        elif all(newWeight[i] < limits[i] for i in range(len(limits))):
            sackObjs.insert(0, obj)
            sack.append(obj.type)
    return sackObjs
    pass

"""
Recursively selects a role for each item
:param items: All items available for selection
:param current: Currently selected pirates
"""
def choose_roles(items, current):
    if items == []:
        return current

    items = sort(items)
    added = items[0]
    current.append(added)
    n_items = []
    for item in items:
        if item.type == added.type:
            pass
        else:
            item.weight = [item.weight[i] + added.weight[i] for i in range(len(item.weight))]
            n_items.append(item)
    return choose_roles(n_items, current)



def sort(nums):
    return quicksort(nums)
    pass

def quicksort(nums):
    nums = sorted(nums, key=lambda obj: obj.efficiency(), reverse=True)
    return nums
    pass

items = [ KnapsackObject(i**2 if i != 3 else 0, [i+2, math.exp(i), i if i==3 else 0], i%4) for i in range(1,20)]
print [str(item) for item in items]
#print knapsack(items, [32,4])
strat = choose_roles(items, [])
print [ str(item) for item in strat]