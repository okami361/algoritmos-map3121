class Dicotomia:
    def resolver(self, funcao, a, b, eps):
        if a>=b or funcao(a)*funcao(b) > 0:
            print(funcao(a))
            print("valores de intervalo invalidos")
            return
        erro = (b-a)/2
        contador_interacoes = 0
        chute=0
        while erro > eps:
            contador_interacoes += 1
            chute = (b+a)/2
            erro = (b-a)/2
            f_meio = funcao(chute)
            
            if f_meio == 0 :
                print("valor encontrado:",  chute)
            elif f_meio > 0 :
                b = chute
            else:
                a=chute

        print("aproximacao encontrada:", chute, " iteracoes:", contador_interacoes, " erro:", erro)




