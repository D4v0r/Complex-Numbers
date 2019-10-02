import complejos as co
import numpy as np
import matplotlib.pyplot as plt

def dinamica_del_sistema(sistema, estado_inicial, clicks):
    '''Se simula el experimento de  las  caincas hallando 
       la dinamica_del_sistema despues de varios clicks'''
    
    for clik in range(clicks):
        estado_inicial = co.accion_matriz_vector(sistema, estado_inicial) 
    
    #Graficación de resultados
    labels = [  'Pto. '+ str(i) for i in range(len(sistema))]
    estado = [ c[0] for c in estado_inicial]
    index = np.arange(len(labels))
    plt.bar(index, estado)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index, labels, rotation=30)
    plt.title('Evolucion del sistema')
    plt.show()
    
    return estado_inicial

def ensamblar_sistemas (sistema_A, estado_inicial_A, sistema_B, estado_inicial_B, clicks):
    '''Ensambla dos sistemas y calcula su dinamica despues de cierto numero de clicks4'''
    
    sistema_ensamblado = co.productoTensor(sistema_A, sistema_B)
    estados_ensamblados = co.productoTensor([estado_inicial_A], [estado_inicial_B])
    return dinamica_del_sistema(sistema_ensamblado, estados_ensamblados[0],clicks)

def multiples_rendijas_cuantico(num_rendijas, num_blancos_pared, vector_probabilidad):
    '''Realiza el experimento de rendijas multiples con probabilidad ajustable'''
    
    num_paredes = num_rendijas + 1
    num_nodos = 2 * num_rendijas + num_paredes * num_blancos_pared + 1
    num_blancos_rendija = len(vector_probabilidad)
    matriz_sistema = [[(0, 0) for j in range(num_nodos)]for i in range(num_nodos)]
    posicion = 0
    for i in range(1, num_rendijas + 1):
        matriz_sistema[i][0][0] = 1/(num_rendijas**(1/2))
        posicion = i
    for i in range(1, num_rendijas + 1):
        for j in range(posicion, posicion + num_blancos_rendija + 1):
            matriz_sistema[j][i] = vector_probabilidad[i-1]
            
        
    return matriz_sistema