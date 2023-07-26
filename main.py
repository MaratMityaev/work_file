import os.path
import os

with open('cook_book.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': int(quantity), 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients

def get_shop_list_by_dishes(person_count, dishes):
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                product = ingredients['product']
                quantity = ingredients['quantity'] * person_count
                measure = ingredients['measure']
                print(product, quantity, measure)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])





