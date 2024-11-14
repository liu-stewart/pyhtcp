from pymatgen.core import Structure

pos = Structure.from_file("source/Si111.vasp")
print(pos.as_dataframe())