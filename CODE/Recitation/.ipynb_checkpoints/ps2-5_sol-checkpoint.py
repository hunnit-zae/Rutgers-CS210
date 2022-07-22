import math
import sys

def quadraticSolver(a, b, c):
    discr = b**2 - 4*a*c
    if discr >= 0:
        root1 = (-b + math.sqrt(discr))/(2*a)
        root2 = (-b - math.sqrt(discr))/(2*a)
    else:
        root1 = str(-b/(2*a)) + " + " + "i"+str(math.sqrt(-1*discr)/(2*a))
        root2 = str(-b/(2*a)) + " - " + "i"+str(math.sqrt(-1*discr)/(2*a))
    print(f'Roots are: {root1} and {root2}')


quadraticSolver(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
