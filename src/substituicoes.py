class Substituicoes:
    def resolver(self, funcao, iteracoes, chute):
        for i  in range(iteracoes):
            chute = funcao(chute)
            print("n=",i," aproximacao encontrada:", chute)

        