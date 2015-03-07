#!/usr/bin/env python

'''

Compiled by	:	Felix Francis (felixfrancier@gmail.com)

Description	:       Generate a symmetric matrix from a lower triangular matrix. The out_put.txt file can be used as the input for softwares like phylipo

'''

############################################################
#### PYTHON FUNCTIONS
############################################################
import csv
import numpy as np
import shlex
import time

############################################################
#### Time to run the code: start timer
############################################################
t0 = time.time()

############################################################
#### Code
############################################################




f2 = open("symmetric_distance_matrix.txt", "w")                                     # Open file for writing the out put data    
                                         

with open('test_matrix.txt') as input_data:                                         # Open the input file with the lower triangular matrix
    data = [map(str,row) for row in csv.reader(input_data)]
    data = data [1:]
    index_names = []
    data2 = []
    max_count = len(data)
    f2.write('\t'+ str(len(data)) + '\n')
    for i in xrange(len(data)):
        data[i] = [','.join(shlex.split(str(data [i] [0])))]
        data[i] = (data [i] [0]).split(",")
        difference = max_count -(len(data[i])-1)
        data[i].extend(['0.0']*(difference))
        index_names.append(data[i] [0])
        data2.append(data[i] [1:])

matrix = np.asarray(data2)

matrix[np.triu_indices_from(matrix,k=1)]=matrix[np.tril_indices_from(matrix,k=-1)]      # Get symmetric matrix from a lower triangular matrix
list2 = matrix.tolist()                                                                 # Convert matrix(array) back to list
for i in xrange(len(list2)):
    print('\t'.join(map(str,list2[i])))

for i in xrange(len(list2)):
    f2.write (index_names [i] + '\t'+ '\t'+ ('\t'.join(map(str,list2[i]))) + '\n')

f2.close()                                                                              # Close the out put file


############################################################
#### Time to run the code: end timer
############################################################
t1 = time.time()
total = t1-t0
print '\n', "Time to run code = ", total, " seconds", '\n'




