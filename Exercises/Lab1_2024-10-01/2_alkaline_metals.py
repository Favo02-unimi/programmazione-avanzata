from operator import itemgetter

alkaline_earth_metals = [
  ("barium", 56),
  ("beryllium", 4),
  ("calcium", 20),
  ("magnesium", 12),
  ("radium", 88),
  ("strontium", 38)
]

print("Highest atomic number:", max(alkaline_earth_metals, key=itemgetter(1))[0])

alkaline_earth_metals = dict(alkaline_earth_metals)

noble_gases = {
  "helium": 2,
  "neon": 10,
  "argon": 18,
  "krypton": 36,
  "xenon": 54,
  "radon": 86
}

merged = alkaline_earth_metals | noble_gases

print("All sorted:", sorted(merged.items()))
