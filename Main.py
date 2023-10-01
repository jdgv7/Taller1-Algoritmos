import FuncionesEstado as F

Entrada1 = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1]
Entrada2 = [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
Entrada3 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1,0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

def EncontrarPosiciones(Estados, Array):
    Posiciones = []
    for i in range(len(Estados)):
        Posiciones.append([Estados[i]])
    for m in range(len(Estados)):
        Valor = Estados[m]
        for x in range(len(Array[0])):
            if ((str(Array[0][x])+str(Array[1][x])+str(Array[2][x])) == str(Valor)):
                Posiciones[m].append(x+1)
    return Posiciones


def EncontrarPosicionesR(Posiciones):
    arregloR = []

    for sublista in Posiciones:
        nueva_sublista = [sublista[0]]
        for valor in sublista[1:]:
            if valor > 1:
                nuevo_valor = valor - 2
                nueva_sublista.append(nuevo_valor)
        arregloR.append(nueva_sublista)
    return arregloR


def mostrar_menu(Array,Posiciones,Estados,PosicionesR):
    print("Menu:")
    print("1. Estado Canal F")
    print("2. Estado Estado F")
    print("3. Estado Canal P")
    print("4. Estado Estado P")
    print("5. Salir")
   
    opcion = input("Selecciona una opción (1/2/3/4/5): ")
    
    if opcion == "1":
        # Punto 1: Llama a la función correspondiente
        F.EstadoCanalF(Array, Posiciones)
    elif opcion == "2":
        # Punto 2: Llama a la función correspondiente
        F.EstadoEstadoF(Array, Posiciones, Estados)
    elif opcion == "3":
        # Punto 3: Llama a la función correspondiente
        F.EstadoCanalP(Array, PosicionesR)
    elif opcion == "4":
        # Punto 4: Llama a la función correspondiente
        F.EstadoEstadoP(Array, PosicionesR, Estados)
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")


def CrearEstados(Array):
    Estados = []
    Estadoinicial = ""
    Estadoinicial = Estadoinicial.zfill(len(Array))
    Estados.append(Estadoinicial)
    siquiente = Estadoinicial
    for i in range((2**len(Array))-1):
        siquiente = '{:b}'.format(int(siquiente, 2)+int(1))
        Estados.append(siquiente.zfill(len(Array)))

    Posiciones = EncontrarPosiciones(Estados, Array)
    PosicionesR = EncontrarPosicionesR(Posiciones)

    # # Punto 1
    # F.EstadoCanalF(Array,Posiciones)

    # # Punto 2
    # F.EstadoEstadoF(Array,Posiciones,Estados)

    # # Punto 3
    # print("\n")
    # print(Posiciones)
    # print("\n")
    # print(PosicionesR)
    print(Estados)
    # print("\n")
    # F.EstadoCanalP(Array, PosicionesR)

    # # Punto 4
    # F.EstadoEstadoP(Array,PosicionesR,Estados)
    # mostrar_menu(Array,Posiciones,Estados,PosicionesR)


CrearEstados([Entrada1, Entrada2, Entrada3])

