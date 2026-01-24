"""
String formatting
"""

first_name = "Alvaro"
print(f"Hi {first_name}")

sentence = "Hi {} {}"
last_name = "Perez"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")