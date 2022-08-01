import js
from js import alert
import random
from threading import Thread

from equipment import Items, Maps, Difficulty
from challenges import Challenge

separator = ', '

def get_items(quantity):

    # Random Items
    quantity = int(Element('quantity-input').element.value)
    if quantity < 0:
        alert(f'Minimum equipment quantity is 0.')
        quantity=0
    elif quantity > 22:
        alert(f'Max equipment quantity is 22.')
        quantity=22

    decided_items = random.sample(Items,k=quantity)

    # Random Map
    decided_map = str(random.choice(Maps))

    # Random Difficulty
    decided_diff = str(random.choice(Difficulty))

    # Debug
    pyscript.write("items_div", separator.join(map(str, decided_items)))
    pyscript.write("map_div", decided_map)
    pyscript.write("diff_div", decided_diff)

def get_challenge(self):
    title, desc = random.choice(list(Challenge.items()))
    pyscript.write("title_div", title)
    pyscript.write("desc_div", desc)