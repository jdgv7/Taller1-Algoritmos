import tkinter as tk
from Main import CrearEstados
from Main import CargarDatos
import pyphi
import numpy as np

# Función graficar
def graficar():
    # Convertir la lista en un arreglo de NumPy
    print(CrearEstados)
    tpm = np.array()

    cm = np.array([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ])

    network = pyphi.Network(tpm, cm=cm, node_labels=['A', 'B', 'C'])
    state = (1,0,0)
    nodes = ('A', 'B', 'C')
    subsystem = pyphi.Subsystem(network, state, nodes)

    A, B, C = subsystem.node_indices

    mechanism = (A, B, C)
    purview = (A, C)
    mip = subsystem.effect_mip(mechanism, purview)
    print(mip)
    
    mip_c = subsystem.cause_mip(mechanism, purview)
    print(mip_c)

    ces = pyphi.compute.ces(subsystem)
    print(ces.labeled_mechanisms)

    sia = pyphi.compute.sia(subsystem)
    print(sia.phi)
    print(sia.cut)

    # Muestra la información en una nueva ventana
    ventana_info = tk.Toplevel()
    etiqueta_info = tk.Label(ventana_info, text=f"MIP: {mip}\nMIP_C: {mip_c}\nCES Labeled Mechanisms: {ces.labeled_mechanisms}")
    etiqueta_info.pack(padx=10, pady=10)

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Haz clic en el botón para llamar a la función.")
etiqueta.pack(pady=10)

# Definir la función a llamar cuando se hace clic en el botón
def boton_clicado():
    # Llama a la función CrearEstados y luego graficar
    CrearEstados(CargarDatos()[0])

# Crear un botón
boton = tk.Button(ventana, text="Llamar a la función", command=boton_clicado)
boton.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()

    
