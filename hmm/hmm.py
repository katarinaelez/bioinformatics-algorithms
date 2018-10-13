#!/usr/bin/env python

import numpy as np

from utils import initialize_matrix, get_max_val_ind

def check_transitions(states,transitions):
    for state in states:
        if state != 'e':
            p_sum = 0
            for transition in transitions.keys():
                if state == transition[0]:
                    p_sum+=transitions[transition]
            if round(p_sum,3) != 1:
                return 'error'

def check_emissions(states,emissions):
    for state in states:
        if state != 'b' and state != 'e':
            p_sum = 0
            for emission in emissions[state].keys():
                p_sum+=emissions[state][emission]
            if round(p_sum,3) != 1:
                return 'error'

def forward(states,transitions,emissions,sequence):
    F = initialize_matrix(len(states),len(sequence)+2)
    F[0][0] = 1
    for i in range(1,len(states)-1):
        F[i][1] = transitions[(states[0],states[i])]*emissions[states[i]][sequence[0]]
    for j in range(2,len(sequence)+1):
        for i in range(1,len(states)-1):
            p_sum = 0
            for k in range(1,len(states)-1):
                p_sum += F[k][j-1]*transitions[(states[k],states[i])]*emissions[states[i]][sequence[j-1]]
            F[i][j] = p_sum
    p_sum = 0
    for k in range(1,len(states)-1):
        p_sum += F[k][len(sequence)]*transitions[(states[k],states[-1])]
    F[-1][-1] = p_sum
    return F

def backward(states,transitions,emissions,sequence):
    F = initialize_matrix(len(states),len(sequence)+2)
    F[-1][-1] = 1
    for i in range(1,len(states)-1):
        F[i][-2] = transitions[(states[i],states[-1])]
    for j in range(len(sequence)-1,0,-1): 
        for i in range(1,len(states)-1):
            p_sum = 0
            for k in range(1,len(states)-1):
                p_sum += F[k][j+1]*transitions[(states[i],states[k])]*emissions[states[k]][sequence[j]]
            F[i][j] = p_sum
    p_sum = 0
    for k in range(1,len(states)-1):
        p_sum += F[k][1]*transitions[(states[0],states[k])]*emissions[states[k]][sequence[0]]
    F[0][0] = p_sum
    return F

def viterbi(states,transitions,emissions,sequence):
    F = initialize_matrix(len(states),len(sequence)+2)
    FP = initialize_matrix(len(states),len(sequence)+2,states[0])
    F[0][0] = 1
    for i in range(1,len(states)-1):
        F[i][1] = transitions[(states[0],states[i])]*emissions[states[i]][sequence[0]]
    for j in range(2,len(sequence)+1):
        for i in range(1,len(states)-1):
            values = []
            for k in range(1,len(states)-1):
                values.append(F[k][j-1]*transitions[(states[k],states[i])]*emissions[states[i]][sequence[j-1]])
            max_val, max_ind = get_max_val_ind(values)
            F[i][j] = max_val
            FP[i][j] = states[max_ind+1]
    values = []
    for k in range(1,len(states)-1):
        values.append(F[k][len(sequence)]*transitions[(states[k],states[-1])])
    max_val, max_ind = get_max_val_ind(values)
    F[-1][-1] = max_val
    FP[-1][-1] = states[max_ind+1]
    return F, FP

def traceback(states,FP):
    path = ['e'] # the last element of the path is the end state
    current = FP[-1][-1] # the current state is the one written in the last cell of the matrix
    for i in range(len(FP[0])-2,0,-1): # loops on the symbols
        path = [current] + path # appends the current state to the path
        current = FP[states.index(current)][i] # finds the index of the current state in the list of states and moves to the corresponing row of FP 
    path = ['b'] + path # the first element of the path is the begin state
    return ' '.join(path) # transforms the list into a string where elements are separated by spaces
