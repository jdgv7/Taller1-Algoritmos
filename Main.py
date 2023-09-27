import FuncionesEstado as F;

Entrada1 = [0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1];
Entrada2 = [0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0];
Entrada3 = [0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0];

def EncontrarPosiciones(Estados,Array):
    Posiciones=[]
    for i in range(len(Estados)):
        Posiciones.append([Estados[i]]);
    for m in range(len(Estados)):
        Valor = Estados[m];
        for x in range(len(Array[0])):
            if((str(Array[0][x])+str(Array[1][x])+str(Array[2][x])) == str(Valor)):
                Posiciones[m].append(x+1);
    #print(Posiciones);
    return Posiciones;
    
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

def CrearEstados(Array):
    Estados =[];
    Estadoinicial="";
    Estadoinicial = Estadoinicial.zfill(len(Array));
    Estados.append(Estadoinicial)
    siquiente = Estadoinicial;
    for i in range((2**len(Array))-1):
        siquiente = '{:b}'.format(int(siquiente,2)+int(1))
        Estados.append(siquiente.zfill(len(Array)))
    print(Estados)
    print(Array)
    Posiciones= EncontrarPosiciones(Estados,Array);  
    PosicionesR= EncontrarPosicionesR(Posiciones);
    #print(Array)
    print('-------')
    print(Posiciones)
    print('*********')
    print(PosicionesR)
    #print('-------')
    # Punto 1
    #F.EstadoCanalF(Array,Posiciones)

    # Punto 2
    F.EstadoEstadoF(Array,Posiciones,Estados)

    # Punto 3
    #F.EstadoCanalP(Array,PosicionesR)
    
    # Punto 4
    #F.EstadoCanalP(Array,PosicionesR)
    
CrearEstados([Entrada1,Entrada2,Entrada3]);
