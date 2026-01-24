"""
Docstring for refresher.assignment_list
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

zoo = ["oso","jirafa","leon","loro","tigre"]
print(zoo)
zoo.remove("leon")
zoo.remove("oso")
print(zoo)

zoo2 = ["oso","jirafa","leon","loro","tigre"]
print(zoo2[0:3])