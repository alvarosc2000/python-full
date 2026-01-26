def reverse(cadena):
    cf = ""
    for i in range(len(cadena)-1,-1,-1):
        cf += cadena[i]
    return cf


print(reverse("Hola Mundo"))