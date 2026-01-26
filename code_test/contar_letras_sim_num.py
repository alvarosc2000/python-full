def contador_util(cadena):
    cont_num = 0
    cont_car = 0
    cont_ext = 0

    cadena_aux = cadena.lower()

    for i in range(len(cadena_aux)):
        if cadena_aux[i].isdigit():
            cont_num += 1
        elif cadena_aux[i].isalpha():
            cont_car += 1
        else:
            cont_ext += 1
    
    print()