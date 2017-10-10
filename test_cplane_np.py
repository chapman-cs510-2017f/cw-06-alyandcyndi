#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Aly Baughman, Cynthia Parks
# Student ID: 1923165, 2303535
# Email: baugh107@mail.chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###

import cplane_np as cplane
import numpy as np

def test_cplanenp():
    result=cplane.ArrayComplexPlane(0,10,2,0,8,2)
    print(result)
    correct=[[  0.+0.j,  10.+0.j],[  0.+8.j, 10.+8.j]]
    print(correct)
    np.testing.assert_almost_equal(result.plane,correct)
    

def f(z):
    return z+1
    
def test_apply():
    result2=cplane.ArrayComplexPlane(0,10,2,0,8,2)
    print(result2)
    correct2=[[  0.+0.j,  10.+0.j],[  0.+8.j, 10.+8.j]]
    print(correct2)
    np.testing.assert_almost_equal(result2.plane,correct2)

    result3=result2.apply(f)
    print(result3)
    correct3=[[  1.+0.j,  11.+0.j],[  1.+8.j, 11.+8.j]]
    print(correct3)    
    np.testing.assert_almost_equal(result3.plane,correct3)