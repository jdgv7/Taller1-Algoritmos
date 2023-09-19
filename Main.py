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

def CrearEstados(Array):
    Estados =[];
    Estadoinicial="";
    Estadoinicial = Estadoinicial.zfill(len(Array));
    Estados.append(Estadoinicial)
    siquiente = Estadoinicial;
    for i in range((2**len(Array))-1):
        siquiente = '{:b}'.format(int(siquiente,2)+int(1))
        Estados.append(siquiente.zfill(len(Array)))
    Posiciones= EncontrarPosiciones(Estados,Array);  
    #F.EstadoCanalF(Array,Posiciones);
    print(Estados)
    F.EstadoEstadoF(Array,Posiciones,Estados);

CrearEstados([Entrada1,Entrada2,Entrada3]);


