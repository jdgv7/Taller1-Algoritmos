import FuncionesEstado as F;
import pandas as pd
import matplotlib.pyplot as plt

def CargarDatos():
    dataframe1 = pd.read_excel('Muestra7-8.xlsx', usecols="B:D",skiprows=[0,1],sheet_name="Muestra 8")

    dataframe1 = dataframe1.values.tolist()
    nuevos_arrays = [[] for _ in range(len(dataframe1[0]))]

    for x in range(len(dataframe1)):
        for y in range(len(dataframe1[0])):
            nuevos_arrays[y].append(dataframe1[x][y])

    return[nuevos_arrays]

def EncontrarPosiciones(Estados,Array):
    Posiciones=[]
    for i in range(len(Estados)):
        Posiciones.append([Estados[i]]);
    for m in range(len(Estados)):
        Valor = Estados[m];
        for x in range(len(Array[0])):
            if ''.join(str(Array[i][x]) for i in range(len(Array))) == str(Valor):
                Posiciones[m].append(x + 1)
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
    Porcentajes ={};
    Estados =[];
    Estadoinicial="";
    Estadoinicial = Estadoinicial.zfill(len(Array));
    Estados.append(Estadoinicial)
    siquiente = Estadoinicial;
    for i in range((2**len(Array))-1):
        siquiente = '{:b}'.format(int(siquiente,2)+int(1))
        Estados.append(siquiente.zfill(len(Array)))
    Posiciones= EncontrarPosiciones(Estados,Array);  
    PosicionesR= EncontrarPosicionesR(Posiciones);
   
    Porcentajes = F.EstadoEstadoP(Array,PosicionesR,Estados)
    A = F.DivisionElementos("AB/A=0",Porcentajes)
    
    print(A)

    # # ------------- GRAFICAS
    # # B = ['000', '001', '010', '011', '100', '101', '110', '111']
    # B = ['00', '01', '10', '11']
    
    # # Crear un DataFrame de Pandas
    # df = pd.DataFrame({'Probabilidades': A, 'Estados': B})

    # # Graficar con Matplotlib
    # plt.bar(df['Estados'], df['Probabilidades'])
    # plt.xlabel('Estados')
    # plt.ylabel('Probabilidades')
    # plt.title('Probabilidades para cada Estado')
    # plt.show()

CrearEstados(CargarDatos()[0]);