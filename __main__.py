
import numpy as np

# number of coordinates
n = 5
# points in the form [x,y]
bot = [30,30]  # (a,p)
top = [70,100] # (b,q)

# we transform the function `y = e^( l ln(x) )`
# such that the endpoints are `bot` and `top`
#   l=1 is linear
#   l=e is exponential
# https://www.desmos.com/calculator/zwrydth5ot
def curve_exp(l,x):
    a,b,p,q = bot[0],top[0],bot[1],top[1]
    if x <= a: return p
    if x >= b: return q
    return p + (q-p) * np.exp(l*np.log( (x-a) / (b-a) ))

# print `n` coordinates
l = np.e
for i in range(n):
    x = bot[0] + i * ( top[0] - bot[0] ) / (n-1)
    y = curve_exp(l,x)
    print(f"({x},{y})")
