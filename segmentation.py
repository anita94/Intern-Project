# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:32:51 2015

@author: Anita
"""

def get_frames(data,samprate):
    w=input('enter the width of each frame: ')
    o=input('enter the overlap percentage: ')
    a=0;j=0;n=0;
    for i in range(0,len(data),w):
        n=n+1
        i=i-o*w/100
    import numpy
    f=numpy.zeros((n+1,w))    
    while(j<n):
        k=0
        for i in range (a,a+w):
            f[j][k]=data[i]
            k=k+1
            a=a+1;
        j=j+1;
        a=a-o*w/100;
    return (f)        