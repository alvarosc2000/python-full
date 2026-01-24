def duplicados():
    my_list = []
    valor = int(input("Introduce valor: "))
    while(valor >= 0):
        my_list.append(valor)
        valor = int(input("Introduce valor: "))

    print("La lista tras añadir los valores")
    for elem in range(len(my_list)):
        print(my_list[elem])
    
    lista_duplicados = []
    lista_sin_duplicados = []

    for i in range(len(my_list)):
        if my_list.count(my_list[i]) > 1 and  my_list[i] not in lista_duplicados:
            lista_duplicados.append(my_list[i])
        elif my_list[i] not in lista_duplicados:
            lista_sin_duplicados.append(my_list[i])

    return lista_duplicados, lista_sin_duplicados

# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    dupli, sin_dupli = duplicados()
    print("Duplicados:", dupli) 
    print("Sin duplicados:", sin_dupli) 