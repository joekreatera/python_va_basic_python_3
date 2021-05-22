# (-b +- srqrt(b*2 - 4a*c))/(2*a)
from math import sqrt

def solve(pa=1, pb=2, pc =1):
    disc =pb**2 - 4*pa*pc
    
    if( disc < 0):
        return float('-inf'),float('inf') 
    x1 = -pb + sqrt( disc )
    x2 = -pb - sqrt( disc  )
    
    return x1/(2*pa) ,  x2/(2*pa)

    
# a(x*x^2) + bx + cm = 0 
s1, s2 = solve()
print(f's: ({s1} {s2}) ')

s1, s2 = solve(pb=10)
print(f's: ({s1} {s2}) ')

s1, s2 = solve(pc=5, pb=10)
print(f's: ({s1} {s2}) ')

s1, s2 = solve(2,8,2)
print(f's: ({s1} {s2}) ')

s1, s2 = solve(1,1,1)
print(f's: ({s1} {s2}) ')
