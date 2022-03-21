import libcplx as lc
def sum_vec_cplx(v1,v2):
    resul_1 = []
    resul_final = []
    for i in range(0,len(v1)):
        real = v1[i][0] + v2[i][0]
        resul_1.append(real)
        img = v1[i][1] + v2[i][1]
        resul_1.append(img)
        resul_final.append(resul_1)
        resul_1 = []
    return(resul_final)
def inv_ad_vec_cplx(v1,v2):
    resul_1 = []
    resul_final = []
    for i in range(0,len(v1)):
        real = v1[i][0] - v2[i][0]
        resul_1.append(real)
        img = v1[i][1] - v2[i][1]
        resul_1.append(img)
        resul_final.append(resul_1)
        resul_1 = []
    return(resul_final)
def product_esc_vec_cplx(a,v1):
    for i in range(0,len(v1)):
        v1[i] = v1[i] * a
    return(v1)
def sum_matriz(m1, m2):
    m = len(m1)
    n = len(m2[0])
    fila = [(0,0)] * n
    sum = [fila]* m
    for j in range(m):
        fila = [(0,0)] * n
        sum[j] = fila
        for k in range(n):
            sum[j][k] = lc.suma_cplx(m1[j][k],m2[j][k])
    return sum
def inv_ad(m1,m2):
    m = len(m1)
    n = len(m2[0])
    fila = [(0, 0)] * n
    sum = [fila] * m
    for j in range(m):
        fila = [(0, 0)] * n
        sum[j] = fila
        for k in range(n):
            sum[j][k] = lc.resta_cplx(m1[j][k], m2[j][k])
    return sum
def transp(matriz):
    fin = len(matriz)
    c = len(matriz[0])
    fila = [(0,0)] * c
    transp = [fila] * fin
    for j in range(fin):
        fila = [(0,0)] * c
        transp[j] = fila
        for k in range(c):
            transp[j][k] = matriz[k][j]
    return transp
def conjugate_matriz(matriz):
    fin = len(matriz)
    c = len(matriz[0])
    fila = [(0,0)] * c
    conjugada = [fila] * fin
    for j in range(fin):
        fila = [(0,0)] * c
        conjugada[j] = fila
        for k in range(c):
            conjugada[j][k] = lc.conjugate_cplx(matriz[j][k])
    return conjugada
def dagger(matriz):
    fin = len(matriz)
    c = len(matriz[0])
    fila = [(0, 0)] * c
    adjunta = [fila] * fin
    matriz = conjugate_matriz(transp(matriz))
    for j in range(fin):
        fila = [(0, 0)] * c
        adjunta[j] = fila
        for k in range(c):
            adjunta[j][k] = matriz[j][k]
    return adjunta
def prod_matriz(m1,m2):
    fin = len(m1)
    c = len(m2)
    a = [[(0, 0) for i in range(c)] for i in range(fin)]
    for i in range(fin):
        for j in range(c):
            for k in range(fin):
                a[i][j] = lc.suma_cplx(a[i][j], lc.product_cplx(m1[i][k], m2[k][j]))
    return a
def matriz_accion_vec(matriz,vector):
    fin = len(matriz)
    a = [(0, 0)] * fin
    for j in range(fin):
        for k in range(fin):
            a[j] = lc.suma_cplx(a[j], lc.product_cplx(matriz[j][k], vector[k]))
    return a
def prod_int_vec(v1,v2):
    num = len(v1)
    x = (0, 0)
    s = [(0, 0)] * num
    for i in range(num):
        s[i] = lc.product_cplx(lc.conjugate_cplx(v1[i]), v2[i])
        x = lc.suma_cplx(s[i], x)
    return (x)
def norm_vec(v):
    num = len(v)
    s = (0, 0)
    for i in range(num):
        s = lc.suma_cplx(lc.product_cplx(v[i], v[i]), s)
    s = lc.mod_cplx(s)
    print(s)
def dist_vec(v1,v2):
    num = len(v1)
    s = 0
    for i in range(num):
        s = s + (lc.mod_cplx(lc.resta_cplx(v1[i], v2[i]))) ** 2
    s = s ** (1 / 2)
    return s
def si_matriz_unit(matriz):
    fin = len(matriz)
    a = [[(0, 0) for i in range(fin)] for i in range(fin)]
    p = [[(0, 0) for i in range(fin)] for i in range(fin)]
    for i in range(fin):
        a = prod_matriz(dagger(matriz), matriz)
    for i in range(fin):
        p[i][i] = (1, 0)
    x = a == p
    return x
def si_matriz_herm (matriz):
    fin = len(matriz)
    a = [[(0,0) for i in range (fin)] for i in range (fin)]
    a = dagger(matriz)
    x = a == matriz
    return x
def prod_ten (m1,m2):
    fin1 = len(m1)
    fin2 = len(m2)
    for i in range(fin1):
        for j in range(len(m1[i])):
            for k in range(fin2):
                m1[i][j] = m1[i][j] * m2[k]
    return(m1)
def productVectorReal(vec1,vec2):
    res = 0
    for i in range(len(vec1)):
        temp = vec1[i]*vec2[i]
        res += temp
    return res
def productRealMatrix(a,b):
    if len(a) != len(b[0]):
        print ("LAS MATRICES NO SON COMPLATIBLES PARA MULTIPLICAR")
        return -1
    else:
        result = [[None] * len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                col = [row[j] for row in b]
                result[i][j] = productVectorReal(a[i],col)
        return result
def matrixOnVectorReal(matrix,vector):
    result = []
    for i in range(len(matrix)):
        result.append(productVectorReal(vector,matrix[i]))
    return result
def matrixOnVector(matrix,vector):
    result = []
    for i in range(len(matrix)):
        result.append(productVector(vector,matrix[i]))
    return result
def productVector(vec1,vec2):
    res = (0+0j)
    for i in range(len(vec1)):
        temp = product(vec1[i],vec2[i])
        res = sum(res,temp)
    return res
def product(a,b):
    return a*b