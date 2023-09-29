import pandas as pd

def EstadoCanalF(Array,Posiciones,tam):
    # print(type(Posiciones))
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
            y +=1
    # print(lista1)
    # print(lista2)
    # print(lista3)
    
    my_dic["A"] = lista1
    my_dic["B"] = lista2
    my_dic["C"] = lista3
    print(my_dic)
    print("\n")

    proporcion_dict = {}

    for key, value in my_dic.items():
        proporciones = []
        for sublist in value:
            total_elementos = len(sublist) - 1  # Restamos 1 para no contar el primer elemento
            total_unos = sum(sublist[1:])  # Sumamos todos los unos en la sublista
            proporcion = total_unos / total_elementos if total_elementos > 0 else 0  # Evitamos la división por cero
            proporciones.append([sublist[0], proporcion])
        proporcion_dict[key] = proporciones

    print(proporcion_dict)
    print("\n")

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame({key: [val[1] for val in value] for key, value in proporcion_dict.items()}, index=[val[0] for val in next(iter(proporcion_dict.values()))])

    # Renombrar las columnas con los nombres de las claves
    df.columns = proporcion_dict.keys()

    print(df)

# --------------------------------------------------------------------------------



def EstadoEstadoF(Array,Posiciones,Estados):
    Estados=[["Estado",]]
    for x in range(len(Posiciones)):
        print(Posiciones[x][0])
        Estados[0].append(Posiciones[x][0])
        Estados.append([Posiciones[x][0]])
        #for x in range(len(Posiciones[x])):
        #   print(Estados.index(Posiciones[x][0]))

    print(Estados[0])
    print(Estados[1])
    print(Estados[2])
    print(Estados[3])
    print(Estados[4])
    print(Estados[5])
    print(Estados[6])
    print(Estados[7])

    for x in range(len(Posiciones)):
        print("Siquientes Elementos de "+Posiciones[x][0])
        y=0
        while y<len(Posiciones[x])-1 and  Posiciones[x][y+1] != 30:
            print("elemento de siquiente posicion :")
            print(str(Array[0][Posiciones[x][y+1]])+
                  str(Array[1][Posiciones[x][y+1]])+
                  str(Array[2][Posiciones[x][y+1]]))
            y+=1;
# --------------------------------------------------------------------------------

# Punto 3
def EstadoCanalP(Array,Posiciones):
    for x in range(len(Posiciones)):
        print(Posiciones[x][0]+" Sus siquientes Posiciones son: ")
        y = 0
        while y<len(Posiciones[x])-1 and Posiciones[x][y+1] != 30 :
            print("siquiente elemento por posicion posicion:")
            print(Array[0][Posiciones[x][y+1]])
            print(Array[1][Posiciones[x][y+1]])
            print(Array[2][Posiciones[x][y+1]])
            y +=1
# --------------------------------------------------------------------------------

# Punto 4
def EstadoEstadoP(Array,Posiciones,Estados):
    Estados=[["Estado",]]
    for x in range(len(Posiciones)):
        print(Posiciones[x][0])
        Estados[0].append(Posiciones[x][0])
        Estados.append([Posiciones[x][0]])
        #for x in range(len(Posiciones[x])):
        #   print(Estados.index(Posiciones[x][0]))

    print(Estados[0])
    print(Estados[1])
    print(Estados[2])
    print(Estados[3])
    print(Estados[4])
    print(Estados[5])
    print(Estados[6])
    print(Estados[7])

    nuevos = []

    print("---------")
    for x in range(len(Posiciones)):
        print("Siquientes Elementos de "+Posiciones[x][0])
        y=0
        while y<len(Posiciones[x])-1 and  Posiciones[x][y+1] != 30:
            print(str(Array[0][Posiciones[x][y+1]])+
                  str(Array[1][Posiciones[x][y+1]])+
                  str(Array[2][Posiciones[x][y+1]]))
            nuevos.append(str(Array[0][Posiciones[x][y+1]])+
                  str(Array[1][Posiciones[x][y+1]])+
                  str(Array[2][Posiciones[x][y+1]]))
            y+=1;
        print("\n");
    print(nuevos)


