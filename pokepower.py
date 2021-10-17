#!/usr/bin/env python

import json
from pathlib import Path
import sys
import argparse


parser = argparse.ArgumentParser(description='Find info about pokemon.', add_help=True)


group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--name',
                   type=str, help='the name of the pokemon you are searching for')
group.add_argument('--dex',
                   type=int, help='the entry dex number of the pokemon you are searching for')
group.add_argument('--type',                   
                   type=str, help='the type of pokemon you are searching for')
args = vars(parser.parse_args())

data = json.loads(Path("../pokemon.json/pokedex.json").read_bytes().decode('utf-8'))

name = args['name']
dex = args['dex']
poketype = args['type']
print('args', args)

found = []
for pokemon in data:
    if name and name.lower() == pokemon['name']['english'].lower():
        found.append(pokemon)
    if dex and dex == pokemon['id']:
        found.append(pokemon)
    if poketype:
        for temp in pokemon['type']:
            if poketype.lower() == temp.lower():
                found.append(pokemon)



if len(found) != 0:
    print(json.dumps(found, indent=1))
else:
    print("Could not find this pokemon. You might have entered it wrong, or we have not implemented it as of this moment.")
# print('Pokedex:')
# print(json.dumps(pokemon, indent=4))
# print(sys.argv)
