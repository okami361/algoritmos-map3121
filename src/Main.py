import math
from dicotomia import Dicotomia
from substituicoes import Substituicoes

def main():
    #Dicotomia
    print("\nDicotomia")
    y = lambda x: math.pow(x,2) - 5
    dicotomia = Dicotomia()
    dicotomia.resolver(y,2,3,0.01)
    

    #Substituicoes
    #f(x) = X**2 + 1.96x - 2.08
    print("\n\n\nSubstituicoes")
    y = lambda x: 2.08/(x + 0.96)
    substituicoes = Substituicoes()
    substituicoes.resolver(y, 10, 1.2)

if __name__ == "__main__":
    main()