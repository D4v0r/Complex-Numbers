import complejos as co
import numpy as np

def canicas(sistema, estado_inicial, clicks):
    '''Se simula el experimento de  las canicas despues de varios clicks'''
    
    for clik in range(clicks):
        estado_inicial = co.accion_matriz_vector(sistema, estado_inicial)  
    return estado_inicial

def ensamblar_sistemas (sistema_A, estado_inicial_A, sistema_B, estado_inicial_B, clicks):
    '''Ensambla dos sistemas y calcula su estado despues de cierto numero de clicks'''
    
    sistema_ensamblado = co.productoTensor(sistema_A, sistema_B)
    estados_ensamblados = co.productoTensor([estado_inicial_A], [estado_inicial_B])
    return canicas(sistema_ensamblado, estados_ensamblados[0], clicks)

def multiples_rendijas_cuantico(num_rendijas, num_blancos_pared, vector_de_probabilidad):
    '''Realiza el experimento de rendijas multiples con probabilidad ajustable'''
    
    num_paredes = num_rendijas + 1
    num_nodos = 2 * num_rendijas + num_paredes * num_blancos_pared + 1
    matriz_sistema = [[(0, 0) for j in range(num_nodos)]for i in range(num_nodos)]
    for i in range(num_nodos):
        for j in range(num_nodos):
            if ( j == 0 and ( i > 0 and i <= num_rendijas) ):
                matriz_sistema[j][i][0] = 1 / num_rendijas
            elif ( j > 0 and j < num_blancos_pared * num_paredes + num_rendijas):
                continue
            
    return matriz_sistema