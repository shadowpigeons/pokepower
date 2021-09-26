#!/usr/bin/env python

import json
from pathlib import Path

data = json.loads(Path("./data.json").read_text())



print('Bulbasaur: pokedex #1')
print(json.dumps(data, indent=4))
