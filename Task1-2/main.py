with open('recipes.txt', 'r') as f:
    cook_book = {}
    for s in f:
        res = s.split()
        print(res)
