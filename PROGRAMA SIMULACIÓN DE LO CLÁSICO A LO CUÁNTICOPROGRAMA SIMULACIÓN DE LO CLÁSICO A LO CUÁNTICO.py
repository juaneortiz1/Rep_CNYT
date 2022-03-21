import libvecsp  as l
import matplotlib.pyplot as plot
import numpy as np

"""Realiza la simulación del estado final de un sistema probabilístico después de t clicks.
    """
def systemAndDinamycsReal(matrix, vector, clicks):
    raisedMatrix = matrix
    for i in range(clicks-1):
        raisedMatrix = l.productRealMatrix(raisedMatrix, matrix)
    result = l.matrixOnVectorReal(raisedMatrix, vector)
    return result

""" Realiza la simulación del estado final de un sistema cuántico después de t clicks.
    """
def systemAndDinamycsQuantum(matrix, vector, clicks):
    raisedMatrix = matrix;
    for i in range(clicks-1):
        raisedMatrix = l.prod_matriz(raisedMatrix, matrix);
    result = l.matrixOnVector(raisedMatrix, vector);
    return result

""" Realiza la simulación del experimento de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
    """
def classicMultipleSlits(matrix,vector,clicks):
    if len(matrix) == 0 or len(vector) == 0:
        print("Operación no disponible.")
    elif len(matrix[0]) != len(vector):
        print("Operación no disponible.")
    else:
        cont = 1
        res=vector
        while cont <= clicks:
            res = l.matrixOnVectorReal(matrix,res)
            cont += 1
    return(res)





""" Realiza la simulación del experimento de las múltiples rendijas cuántico
    """
def quantumMultipleSlits(matrix,vector,clicks):
    if len(matrix) == 0 or len(vector) == 0:
        print("Operación no disponible.")
    elif len(matrix[0]) != len(vector):
        print("Operación no disponible.")
    else:
        cont = 1
        res=vector
        while cont <= clicks:
            res = l.matrixOnVector(matrix,res)
            cont += 1
        for i in range(len(res)):
            res[i] = abs(res[i].real)
    return(res)


""" Realiza el gráfico de probabilidades de estados de un vector dado
    """
def Graphs(vector, title):
    x = np.array([ x for x in range(len(vector))])
    y = np.array([round(vector[x]*100,2) for x in range(len(vector))])
    plot.bar( x,y , color ='b', align='centro')
    plot.title('Probabilidad de estados' + title)
    plot.show()

def Graphs2(vector):
    x = np.array([ x for x in range(len(vector))])
    y = np.array([round(vector[x][0]*100,2) for x in range(len(vector))])
    plot.bar( x,y , color ='b', align='centro')
    plot.title('Probabilidad de estados')
    plot.show()