def suma_pares_potencia_dos(numbers):
    from collections import defaultdict

    freq = defaultdict(int)
    contador = 0

    for x in numbers:
        potencia = 1
        while potencia <= 2**31:
            necesario = potencia - x
            contador += freq[necesario]
            potencia <<= 1  # siguiente potencia de 2

        freq[x] += 1

    return contador

print(suma_pares_potencia_dos([1, -1, 2, 3]))      # 5
print(suma_pares_potencia_dos([2]))                # 1
print(suma_pares_potencia_dos([-2, -1, 0, 1, 2]))  # 5
print(suma_pares_potencia_dos([]))                 # 0
