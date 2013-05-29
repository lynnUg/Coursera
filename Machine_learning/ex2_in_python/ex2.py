#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from numpy import newaxis, r_, c_, mat, e
from numpy.linalg import *
def predict(theta, X):
    #print( sigmoid(X * c_[theta])).shape
    p = sigmoid(X * c_[theta]) >= 0.5
    #print p.shape
    return p
def sigmoid(z):
    g=1./(1+e**(-z.A))
    return g
def computeCost(X,y, theta):
    m=X.shape[0]
    #print type(X*c_[theta])
    prediction=sigmoid(X*c_[theta])
    Cost_postive=y.T.dot(np.log(prediction))
    Cost_negative=(1-y).T.dot(np.log(1-prediction))
    Cost=-(1./m)*(Cost_negative+Cost_postive)
    #print Cost[0][0]
    return Cost[0][0]
if __name__ == '__main__' :
    print 'hello'
    data=np.loadtxt('ex2data1.txt',delimiter=',' )
    X=mat(c_[data[:,:2]])
    y=c_[data[:,2]]

    m,n=X.shape
    X=c_[np.ones(m),X]

    initial_theta=np.zeros(n+1)

    cost,grad=computeCost(X,y,initial_theta),None

    options = {'full_output': True, 'maxiter': 400}
 
    theta, cost, _, _, _ = \
        optimize.fmin(lambda t: computeCost(X,y,t), initial_theta, **options)
 
    print 'Cost at theta found by fminunc: %f' % cost
    print 'theta: %s' % theta
    
    prob = sigmoid(mat('1 45 85') * c_[theta])
    print 'For a student with scores 45 and 85, we predict an admission ' \
          'probability of %f' % prob
 
    p = predict(theta, X)
    print 'Train Accuracy:', (p == y).mean() * 100
