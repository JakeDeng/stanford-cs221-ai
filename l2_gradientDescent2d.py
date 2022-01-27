import numpy as np

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
    
    #algorithms: how we compute it
    def gradientDescent(F,dF,d):
        w = np.zeros(d)
        eta = 0.1
        for t in range(100):
            value = F(w)
            gradient = dF(w)
            w = w - gradient*eta
            print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))

    gradientDescent(F,dF,d)
            
            

    