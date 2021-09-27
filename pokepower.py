#!/usr/bin/env python

import json
from pathlib import Path
import sys

data = json.loads(Path("./data.json").read_text())
key = sys.argv[1]
value = sys.argv[2]
for pokemon in data:
    if "name" == key.lower():
        if pokemon["name"] == value.lower():
            print(pokemon)
    if "entry_dex_number" == key.lower():
        if pokemon["entry_dex_number"] == int(value.lower()):
            print(pokemon)

# print('Pokedex:')
# print(json.dumps(data, indent=4))
# print(sys.argv)
