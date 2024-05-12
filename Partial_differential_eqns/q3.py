# Bisection method

def nth_root(n,a,eps):
    x_min=0
    x_max= max(1,a)
    while(x_max-x_min>eps):
        x_avg= (x_max+x_min)/2
        f= x_avg**n -a
        if(f>0):
            x_max= x_avg
        else:
            x_min=x_avg
    return x_avg

print(nth_root(4,81,1e-6))