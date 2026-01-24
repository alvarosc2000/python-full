def primer_numero_repetido(cadena):
    numero = -1
    contador = 0
    for i in range(len(cadena)-1):
      for j in range(i+1, len(cadena)):
         if numero == -1 and contador == 0 and cadena[i] == cadena[j]:
            numero = cadena[i]
            contador += 1
    return numero

print(primer_numero_repetido([2, 1, 3, 5, 3, 2]))
print(primer_numero_repetido([1, 2, 3, 4]))