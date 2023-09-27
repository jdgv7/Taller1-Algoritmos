def resta_valores(arreglo):
    nuevo_arreglo = []  # Crear una lista para almacenar el nuevo arreglo resultante

    for sublista in arreglo:
        nueva_sublista = [sublista[0]]  # Mantener el primer elemento (el string) sin cambios

        for valor in sublista[1:]:
            if valor > 1:
                nuevo_valor = valor - 2
                nueva_sublista.append(nuevo_valor)

        nuevo_arreglo.append(nueva_sublista)

    return nuevo_arreglo

# Ejemplo de uso
arreglo_original = [['000', 1, 12, 20, 28], ['001', 8, 14, 29], ['010', 7, 9, 22, 24], ['011', 4, 16, 18, 27], ['100', 3, 30], ['101', 2, 6, 10, 17, 23], ['110', 5, 15, 26], ['111', 11, 13, 19, 21, 25]]
nuevo_arreglo = resta_valores(arreglo_original)
print(nuevo_arreglo)
