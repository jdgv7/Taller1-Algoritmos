import pyphi
import numpy as np

data_dict = {
    '000': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    '001': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    '010': [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    '011': [0.0, 0.0, 0.0, 0.0, 0.9736842105263158, 0.02631578947368421, 0.0, 0.0],
    '100': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    '101': [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    '110': [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    '111': [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
}




# Convertir el diccionario en una lista de arreglos de NumPy
data_array_list = list(data_dict.values())

# Convertir la lista en un arreglo de NumPy
tpm = np.array(data_array_list)

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
print(subsystem.state)

mechanism = (A, B, C)
purview = (A, C)
mip = subsystem.effect_mip(mechanism, purview)
print(mip)

print("-----------------------------------------------")
mip_c = subsystem.cause_mip(mechanism, purview)
print(mip_c)

ces = pyphi.compute.ces(subsystem)
print(ces.labeled_mechanisms)

sia = pyphi.compute.sia(subsystem)
print(sia.phi)
print(sia.cut)