#!/usr/bin/python3
"""Defining matrix_mul module
The module supplies one function, matrix_mul().
"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices
    len of cols of m_a must equal len of rows of m_b
    i.e. (m, n) . (n, p)
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(mem, list) for mem in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(mem, list) for mem in m_b):
        raise TypeError("m_b must be a list of lists")
    elif len(m_a) == 0 or any(len(mem) == 0 for mem in m_a):
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or any(len(mem) == 0 for mem in m_b):
        raise ValueError("m_b can't be empty")
    elif not all(type(elem) in (int, float)
                 for mem in m_a for elem in mem):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(type(elem) in (int, float)
                 for mem in m_b for elem in mem):
        raise TypeError("m_b should contain only integers or floats")
    elif not all(len(mem) == len(m_a[0]) for mem in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(mem) == len(m_b[0]) for mem in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        result.append([])
        for j in range(len(m_b[0])):
            result[i].append(sum(m_a[i][k] * m_b[k][j]
                             for k in range(len(m_a[0]))))
    return result


m_a = [[a**2, b*a] * 100 for a,b in enumerate(range(100))]
matdiv = __import__("2-matrix_divided").matrix_divided
import numpy as np
m_b = np.transpose(matdiv(m_a, 10)).tolist()
print(np.shape(m_a))
print(np.shape(m_b))
for i in range(100):
    matrix_mul(m_a, m_b)
