import js
from js import alert
import random
from item_list import Items, Maps, Difficulty

separator = ', '

def get_items(quantity):

    # Random Items
    quantity = int(Element('quantity-input').element.value)
    if quantity > 14:
        quantity=14

    decided_items = random.sample(Items,k=quantity)


    # Random Map
    decided_map = str(random.choice(Maps))

    # Random Difficulty
    decided_diff = str(random.choice(Difficulty))

    # Debug
    #print("Items: ",decided_items, "Map: ",decided_map, "Diff: ",decided_diff)
    pyscript.write("items_div", separator.join(map(str, decided_items)))
    pyscript.write("map_div", decided_map)
    pyscript.write("diff_div", decided_diff)