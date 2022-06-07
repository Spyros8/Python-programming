def mySqrt(x):
    #x = float(x)
    #if x < 0:
        #x = abs(x)
    #else:
     #   pass
    r = x
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r