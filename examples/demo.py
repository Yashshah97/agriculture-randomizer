"""Demo for Agriculture Monte Carlo Engine."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import agriculture_randomizer

print("Agriculture Monte Carlo Engine", "v" + agriculture_randomizer.__version__)
print("modules:", [m for m in dir(agriculture_randomizer) if not m.startswith('_')])
