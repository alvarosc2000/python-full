def  contador_palabras(cadena):
    contador = 0
    for elem in range(len(cadena)):
        if cadena[elem] == " ":
            contador+=1
    return contador

print(contador_palabras("Hola mundo desde Python"))