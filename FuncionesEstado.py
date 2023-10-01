import pandas as pd

def count_estados(Posiciones):
    diccionario_Posiciones = {}
    for sublista in Posiciones:
        llave = sublista[0]
        leng_sub = len(sublista) - 1
        diccionario_Posiciones[llave] = leng_sub
    return diccionario_Posiciones

def EstadoCanalF(Array,Posiciones):
    count_positions = count_estados(Posiciones)
    print("\n")
    print(count_positions)
    print("\n")
    my_dic = {}
    lista1 = [[] for _ in range(len(Posiciones))]
    lista2 = [[] for _ in range(len(Posiciones))]
    lista3 = [[] for _ in range(len(Posiciones))]

    for x in range(len(Posiciones)):      
        y = 0
        lista1[x].append(Posiciones[x][0])
        lista2[x].append(Posiciones[x][0])
        lista3[x].append(Posiciones[x][0])
        while y < len(Posiciones[x])-1 and Posiciones[x][y+1] != 30:
            lista1[x].append(Array[0][Posiciones[x][y+1]])
            lista2[x].append(Array[1][Posiciones[x][y+1]])
            lista3[x].append(Array[2][Posiciones[x][y+1]])
            y += 1
    
    my_dic["A"] = lista1
    my_dic["B"] = lista2
    my_dic["C"] = lista3

    nuevo_diccionario = {}
    for clave_principal, lista_secundaria in my_dic.items():
        nueva_lista = {}
        for elemento in lista_secundaria:
            clave_secundaria = elemento[0]
            nueva_lista[clave_secundaria] = elemento[1:]
        nuevo_diccionario[clave_principal] = nueva_lista
    
    print("\n")
    print(nuevo_diccionario)
    print("\n")

    resultados = {}
    for clave_principal, subdiccionario in nuevo_diccionario.items():
        sub_resultados = {}
        for subllave, lista in subdiccionario.items():
            cantidad_de_unos = lista.count(1)
            sub_resultados[subllave] = cantidad_de_unos
        # print(sub_resultados)
        # print("\n")
        division_resultados = {}
        for llave in sub_resultados:
            if llave in count_positions:
                print(f'{llave} === {sub_resultados[llave]} / { count_positions[llave]}')
                division_resultados[llave] = sub_resultados[llave] / count_positions[llave]
        print("\n")
        resultados[clave_principal] = division_resultados

    for data, val in resultados.items():
        print(f'{data}:{val}')

    print("\n")
    print(count_positions)
    print("\n")

    # # Crear un DataFrame a partir del diccionario
    # df = pd.DataFrame(resultados)
    # print(df)
# --------------------------------------------------------------------------------

# Punto 2
def EstadoEstadoF(Array,Posiciones,Estados):
    lista = []
    my_dic = {}
    for x in range(len(Posiciones)):        
        y=0
        while y < len(Posiciones[x])-1 and Posiciones[x][y+1] != 30:
            data = str(Array[0][Posiciones[x][y+1]])+ str(Array[1][Posiciones[x][y+1]])+ str(Array[2][Posiciones[x][y+1]])
            lista.append(data)
            y+=1;
        my_dic[Posiciones[x][0]] = lista
        lista = []
    
    # Diccionario resultante
    diccionario_r = {}

    # Recorremos el diccionario original
    for estado, sublistas in my_dic.items():
        temp_count = {} # Diccioanrio temporal
        for sublista in sublistas:
            if sublista in temp_count:
                temp_count[sublista] += 1
            else:
                temp_count[sublista] = 1
        for est in Estados:
            if est not in temp_count:
                temp_count[est] = 0
        diccionario_r[estado] = temp_count
   
    diccionario_Posiciones = count_estados(Posiciones)
   
    result_dict = {}

    for key2, value2 in diccionario_Posiciones.items():
        if key2 in diccionario_r:
            result_dict[key2] = {}
            for key1, value1 in diccionario_r[key2].items():
                result_dict[key2][key1] = value1 / value2

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(result_dict)
    df = df.sort_index(axis=0).sort_index(axis=1).transpose()
    print(df)

# --------------------------------------------------------------------------------
# Punto 3
def EstadoCanalP(Array,Posiciones):
    EstadoCanalF(Array,Posiciones)
# --------------------------------------------------------------------------------
# Punto 4
def EstadoEstadoP(Array,Posiciones,Estados):
    EstadoEstadoF(Array,Posiciones,Estados)
