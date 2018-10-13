#!/usr/bin/env python

from __future__ import print_function

def initialize_matrix(dim1,dim2,value=0):
    F = []
    for i in range(0,dim1):
        F.append([])
        for j in range(0,dim2):
            F[i].append(value)
    return F

def print_matrix(matrix,axis1,axis2):
    w = '{:<10}'
    print(w.format('') + w.format('0') + ''.join([w.format(char) for char in axis2]) + w.format('0'))
    for i, row in enumerate(matrix):
        print(w.format(axis1[i]) + ''.join(['{:<10.2e}'.format(item) for item in row]))
        
def print_matrix_p(matrix,axis1,axis2):
    w = '{:<10}'
    print(w.format('') + w.format('0') + ''.join([w.format(char) for char in axis2]) + w.format('0'))
    for i, row in enumerate(matrix):
        print(w.format(axis1[i]) + ''.join(['{:<10s}'.format(item) for item in row]))

def get_max_val_ind(values):
    max_val = values[0]
    max_ind = 0
    for ind, val in enumerate(values):
        if val>max_val:
            max_val = val
            max_ind = ind
    return max_val, max_ind
