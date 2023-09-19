def EstadoCanalF(Array,Posiciones):
    for x in range(len(Posiciones)):
        print(Posiciones[x][0]+" Sus siquientes Posiciones son: ")
        y = 0
        while y<len(Posiciones[x])-1 and Posiciones[x][y+1] != 30 :
            print("siquiente elemento por posicion posicion:")
            print(Array[0][Posiciones[x][y+1]])
            print(Array[1][Posiciones[x][y+1]])
            print(Array[2][Posiciones[x][y+1]])
            y +=1
    print("Lo logre pero hay que hacerlo bonito :v")

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

    #for x in range(len(Posiciones)):
    #    print("Siquientes Elementos de "+Posiciones[x][0])
    #    y=0
    #    while y<len(Posiciones[x])-1 and  Posiciones[x][y+1] != 30:
    #        print("elemento de siquiente posicion :")
    #        print(str(Array[0][Posiciones[x][y+1]])+
    #              str(Array[1][Posiciones[x][y+1]])+
    #              str(Array[2][Posiciones[x][y+1]]))
    #        y+=1;
    #print("En Proceso EstadoEstadoF :v")

def EstadoCanalP(Array,Posiciones):
    print("En Proceso EstadoCanalP :v")

def EstadoEstadoP(Array,Posiciones):
    print("En Proceso EstadoEstadoP :v")