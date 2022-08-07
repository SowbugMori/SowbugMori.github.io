import js
from js import alert
import random

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
    diff_div = js.document.getElementById("diff_div")
    if decided_diff == 'Amateur':
        diff_div.style.color = '#1cb2d2'
    elif decided_diff == 'Intermediate':
        diff_div.style.color = '#8dd21c'
    elif decided_diff == 'Professional':
        diff_div.style.color = '#ea8f36'
    elif decided_diff == 'Nightmare':
        diff_div.style.color = '#d74c4c'
        
    # Debug
    pyscript.write("items_div", separator.join(map(str, decided_items)))
    pyscript.write("map_div", decided_map)
    pyscript.write("diff_div", decided_diff)

def get_challenge(self):
    title, desc = random.choice(list(Challenge.items()))
    pyscript.write("title_div", title)
    pyscript.write("desc_div", desc)
