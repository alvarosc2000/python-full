from collections import Counter

texto = "hola mundo hola python mundo python hola"
lista_palabras = texto.split()
conteo_palabras = Counter(lista_palabras)
print(conteo_palabras) # Salida: Counter({'hola': 3, 'mundo': 2, 'python': 2})
