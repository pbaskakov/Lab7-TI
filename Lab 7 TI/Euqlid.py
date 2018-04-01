def extended_Euqlid(a,b):
    r=[a,b]
    x=[1,0]
    y=[0,1]
    while (r[0]%r[1]!=0):
        q=r[0]//r[1]
        r.append(r[0]%r[1])
        r.pop(0)
        x.append(x[0]-q*x[1])
        x.pop(0)
        y.append(y[0]-q*y[1])
        y.pop(0)
    return x[1]%b