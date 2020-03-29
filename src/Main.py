import math
from dicotomia import Dicotomia

def main():
    y = lambda x: math.pow(x,2) - 5
    dicotomia = Dicotomia()
    dicotomia.resolver(y,2,3,0.01)

if __name__ == "__main__":
    main()