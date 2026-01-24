def reverse(cadena):
    cd = ""
    for i in range(len(cadena)-1,-1,-1):
        cd += cadena[i]
    return cd


print(reverse("Hola Mundo"))