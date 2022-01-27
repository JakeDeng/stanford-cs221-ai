def run():
    points = [(2,4), (4,2)]

    print(type(points))
    #tuple is ordered and unchangeable
    print(type(points[0]))
    
    def F(w):
        return sum((w*x - y)**2 for x,y in points)
    
    def dF(w):
        return sum(2*w*x**2 - 2*x*y for x,y in points)
    
    #Gradient descent
    w = 0
    factor = 0.01
    for t in range(50):
        value = F(w)
        gradient = dF(w)
        w = w - gradient*factor
        print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))