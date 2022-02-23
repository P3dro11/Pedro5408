# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:46:05 2022

@author: Pedro
"""
#Pedro Barroso
#ID:005849424
#CSE 5350
#Fixed Point Iteration


import math

def g(x):
  return x ** 2 - 2

def fixed_iteration ( p0, tol, n0 ):
  # implement Fixed Iteration Method Here
  i = 1 

  while (i <= n0):
        p = g(p0)
    
        if((p-p0) < tol):
             print ("The procedure was successful.", p)
             return 
             i = i + 1
             p0 = p 
    
    
    
  # End of the function

fp = fixed_iteration( 1.5, 1e-4, 1000)

print( fp )

