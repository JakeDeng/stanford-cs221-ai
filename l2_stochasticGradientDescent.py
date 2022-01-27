import numpy as np
import random

def run():
    #Modeling: what we want to compute
    #generate aritifical data
    true_w = np.array([1,2,3,4,5])
    d = len(true_w)
    points = []
    for i in range(10000):
        x = np.random.randn(d)
        y = true_w.dot(x) + np.random.randn()
        points.append((x,y))
    
    def F(w):
        return sum((w.dot(x) - y)**2 for x,y in points) / len(points)
    
    def dF(w):
        return sum(2*(w.dot(x) - y)*x for x,y in points) / len(points)

    #stochastic. pick from index i
    def sF(w,i):
        x,y = points[i]
        return (w.dot(x) - y)**2
    
    def sdF(w,i):
        x,y = points[i]
        return 2*(w.dot(x) - y)*x
    
    #algorithms: how we compute it
    def gradientDescent(F,dF,d):
        w = np.zeros(d)
        eta = 0.1
        for t in range(100):
            value = F(w)
            gradient = dF(w)
            w = w - gradient*eta
            print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))

    def stochasticGradientDescent(sF,sdF,d,n):
        w = np.zeros(d)
        eta = 1
        numUpdates = 0
        for t in range(500):
            #for i in range(n):#shouldn't be all the points in practice
            i = random.randint(0, n)
            value = sF(w,i)
            gradient = sdF(w,i)
            numUpdates += 1
            eta = 1 / numUpdates
            w = w - gradient*eta
            print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))

    #gradientDescent(F,dF,d)
    stochasticGradientDescent(sF,sdF,d,len(points))
            
            

    