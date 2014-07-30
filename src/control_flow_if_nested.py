#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

How to define if nested in Python?

¿Cómo definir if anidados en Python?
'''

#a conditional sentence can in turn contain other nested statement

#create a integer
n = 200

#check if n is less than 200
if n < 200:
    print('the value of n is less than 200')

    #check if n is equal to 150
    if n == 150:
        n = n / 5

    #check if n is equal to 100
    elif n == 100:
        n = n / 2

    #print the value of n
    print(n)
else:
    print('the value of n greater than or equal to 200')
