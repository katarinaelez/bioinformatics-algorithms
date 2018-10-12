#!/usr/bin/env python

from __future__ import print_function
from utils import print_matrix, print_matrix_p

import hmm

#define model
states = ['b','y','n','e']
transitions = {('b','y') : 0.2,
               ('b','n') : 0.8,
               ('y','y') : 0.7,
               ('y','n') : 0.2,
               ('y','e') : 0.1,
               ('n','n') : 0.8,
               ('n','y') : 0.1,
               ('n','e') : 0.1
    }
emissions = {'y' : {'A':0.1, 'C':0.4, 'G':0.4, 'T':0.1},
             'n' : {'A':0.25, 'C':0.25, 'G':0.25, 'T':0.25}
    }

#check probability values
assert hmm.check_transitions(states,transitions) != 'error'
assert hmm.check_emissions(states,emissions) != 'error'

#sequence
sequence = 'ATGCG'

#forward algorithm
F = hmm.forward(states,transitions,emissions,sequence)
print_matrix(F,states,sequence)
print('\n')

#backward algorithm
F = hmm.backward(states,transitions,emissions,sequence)
print_matrix(F,states,sequence)
print('\n')

#viterbi algorithm
F, FP = hmm.viterbi(states,transitions,emissions,sequence)
print_matrix(F,states,sequence)
print('\n')
print_matrix_p(FP,states,sequence)
print('\n')
path = hmm.traceback(states,FP)
print(path)
print('- '+' '.join(sequence)+' -')
