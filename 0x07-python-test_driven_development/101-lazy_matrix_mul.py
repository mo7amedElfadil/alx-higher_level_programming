#!/usr/bin/python3
"""Defining lazy_matrix_mul module
The module supplies one function, lazy_matrix_mul().
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices using numpy's dot method
    """
    return np.matmul(m_a, m_b)
