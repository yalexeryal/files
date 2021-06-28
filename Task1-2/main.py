import os
from pprint import pprint


def read_to_list(file_name):
    file_path = os.getcwd()
    path_ = f'{file_path}/{file_name}'
    with open(path_) as f:
        lines = []
        for line in f:
            line = line.strip()
            if line:
                lines.append(line)
            continue
        lines = iter(lines)
    return lines


def new_cook_book(dishes):
        keys = ['ingredient_name', 'quantity', 'measure', ]
        cook_book = {}
        for name in dishes:
            cook_book[name] = []
            num = next(dishes)
            for _ in range(int(num)):
                structure = next(dishes)
                ingrid = structure.split(' | ')
                z = zip(keys, ingrid)
                ingredients = {k: v for (k, v) in z}
                cook_book[name].append(ingredients)
                continue
            continue
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = new_cook_book(read_to_list(file_name))
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                shop_list_item = dict(ingredient)
                quantity_ = int(shop_list_item['quantity']) * person_count
                if shop_list_item['ingredient_name'] in shop_list:
                    shop_list[shop_list_item['ingredient_name']]['quantity'] += quantity_

                else:
                    shop_list[shop_list_item['ingredient_name']] = \
                        {'measure':shop_list_item['measure'], 'quantity':quantity_}

    return shop_list

file_name = 'recipes.txt'
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос', 'Омлет'], 4))


