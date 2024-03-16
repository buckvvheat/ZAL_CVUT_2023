class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
 
def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
 
def maxExpirationDay(fridge):
    max_exp = -1
    for food in fridge:
        max_exp = max(max_exp, food.expiration)
    return max_exp
 
def histogramOfExpirations(fridge):
    max_exp = maxExpirationDay(fridge)
    histogram = [0] * (max_exp + 1)
    for food in fridge:
        histogram[food.expiration] += 1
    return histogram
 
def cumulativeSum(histogram):
    return [sum(histogram[:i+1]) for i in range(len(histogram))]
 
def sortFoodInFridge(fridge):
    histogram = histogramOfExpirations(fridge)
    cumulative = cumulativeSum(histogram)
    sorted_fridge = [None] * len(fridge)
 
    for food in fridge:
        pos_ind = cumulative[food.expiration] - 1
        sorted_fridge[pos_ind] = food
        cumulative[food.expiration] -= 1
 
    return sorted_fridge
 
def reverseFridge(fridge):
    return fridge[::-1]
 
def eatFood(name, fridge):
    food_to_remove = None
    for food in fridge:
        if food.name == name:
            if food_to_remove is None or food.expiration < food_to_remove.expiration:
                food_to_remove = food
 
    if food_to_remove is not None:
        new_fridge = [food for food in fridge if food != food_to_remove]
        return new_fridge
    else:
        return fridge