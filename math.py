import numpy as np
import test

# a ist matrix und es soll A=L*L^T sein
# A hat dabei vorschrift A=A^T
def cholesky_verfahren(a):
    if test.test_cholesky_verfahren(a):
        if a.shape == (3,3):
            l_11 = sqrt(a[0,0])
            l_12 = a[0,1]/l_11
            l_13 = a[0,2]/l_11
            l_22 = sqrt(a[1,1]-quad(l_12))
            l_23 = (a[1,2]-l_12*l_13)/l_22
            l_33 = sqrt(a[2,2]-quad(l_13)-quad(l_23))

        l = np.array([[l_11, 0, 0],[l_12, l_22, 0],[l_13, l_23, l_33]])
        return l
    return "Matrix ist nicht positiv definit"

def gaußsche_eliminationsverfahren(a, b):
    a_b = np.insert(a, len(a), b, axis=1)
    if (a[0,0] == 0):
        zeile = suche_wert(a_b, 0)
    a_b = spalten_tauschen(a_b, zeile, 0)
    
    return a_b

def spalten_tauschen(a, s1, s2):
    a_s1 = a[s1].copy()
    a_s2 = a[s2].copy()
    a[s1] = a_s2
    a[s2] = a_s1
    return a

def suche_wert(a, zeile):
    i = len(a)-1
    while i>=0:
        if a[i, zeile] == 0:
            i=i-1
        else:
            return i

# s1 ist oben, daher s2-s1
def sub_spalten(a, s1, s2):
    

#print(suche_wert(np.array([[1,2,3],[4,5,6],[2,0,0]]),0))


print(gaußsche_eliminationsverfahren(np.array([[0,2,3],[1,2,3],[7,2,3]]), np.array([4,5,6])))

def sqrt(x):
    return np.sqrt(x)

def quad(x):
    return x**2

#print(np.array([[1, 2, 1], [2, 13, 2], [1, 2, 9]]))
#print(np.transpose(np.array([[1, 2, 3], [2, 13, 2], [1, 2, 9]])))
#print(cholesky_verfahren(np.array([[1, 2, 1], [2, 13, 2], [1, 2, 9]])))