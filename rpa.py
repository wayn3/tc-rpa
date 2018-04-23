#!/usr/bin/env python3

import numpy as np

def b_vec(a_vec):
    a1,a2,a3 = a_vec[0],a_vec[1],a_vec[2]
    b1 = np.cross(a2,a3)/np.dot(a1, np.cross(a2,a3))                         
    b2 = np.cross(a3,a1)/np.dot(a2, np.cross(a3,a1))                         
    b3 = np.cross(a1,a2)/np.dot(a3, np.cross(a1,a2))                         
    return np.array([b1,b2,b3])*2.0*np.pi

def r_mesh(a, m):
    r = m[1:] - m[0]
    r_mesh = np.dot(np.concatenate([r, -r]),a)
    #r_mesh = np.dot(r,a)
    return r_mesh

def tc_rpa(a, r_mesh, q):
    b = b_vec(a)
    q_mesh = np.dot(q[1:],b)
    j = 0 
    for q in q_mesh:
        jnn = 0
        for r in r_mesh:
            jnn += 1.0 - np.exp(np.dot(q,r)*1j)
        j += 1.0/jnn

    print("{:6.3f}".format(1.0/j*len(q_mesh)/len(r_mesh)))
    
if __name__ == "__main__":
    q = np.genfromtxt('q_10.dat')

    a_1 = np.array([[0.0,0.5,0.5],
                    [0.5,0.0,0.5],
                    [0.5,0.5,0.0]])

    a_2 = np.array([[ 2.075181,-2.934749, 3.594319],
                    [ 4.150362, 2.934749, 0.000000],
                    [-2.075181, 2.934749, 3.594319]])

    a_3 = np.array([[6.661684,0.000000,3.846125],
                    [2.220561,6.280696,3.846125],
                    [0.000000,0.000000,7.692251]])

    m_1 = np.array([[0.0,0.5,0.0],
                    [0.0,0.0,0.5],
                    [0.0,0.0,0.0],
                    [0.5,0.0,0.0]])

    m_2 = np.array([[0.0,0.0,0.0],
                    [0.5,0.0,0.5],
                    [-0.5,0.0,0.5],
                    [-0.5,0.0,-0.5],
                    [0.5,0.0,-0.5],
                    [0.0,0.5,0.5],
                    [0.0,-0.5,0.5],
                    [0.0,-0.5,-0.5],
                    [0.0,0.5,-0.5],
                    [0.5,0.5,0.0],
                    [-0.5,0.5,0.0],
                    [-0.5,-0.5,0.0],
                    [0.5,-0.5,0.0]])

    m_3 = np.array([[0.5,0.0,0.5],
                    [0.0,0.5,0.5],
                    [0.5,0.5,0.5],
                    [0.5,0.5,0.0]])

    a = a_2; m = m_2

    r_mesh = r_mesh(a,m)
    tc_rpa(a, r_mesh, q) 
