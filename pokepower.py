#!/usr/bin/env python

import json
from pathlib import Path
import sys

data = json.loads(Path("./data.json").read_text())
key = sys.argv[1]
value = sys.argv[2]
found = None
for pokemon in data:
    if "name" == key.lower():
        if pokemon["name"] == value.lower():
            #print(json.dumps(pokemon, indent=4))
            found = pokemon
    if "entry_dex_number" == key.lower():
        if pokemon["entry_dex_number"] == int(value.lower()):
            #print(json.dumps(pokemon, indent=4))
            found = pokemon

if found is not None:
    print(json.dumps(found, indent=1))
else:
    print("Could not find this pokemon. You might have spelled it wrong, or we have not implemented it as of this moment.")
# print('Pokedex:')
# print(json.dumps(pokemon, indent=4))
# print(sys.argv)
