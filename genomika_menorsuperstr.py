#########################################################################
#                    Estagio Genomika Diagnosticos 2017                 #
#                                                                       #
# Lucas Glasner Regis    #     lgr3@cin.ufpe.br      #     9 9872 2412  #
#                                                                       #
# Nao tratei bases (checar por A, C, G, T) nem numero de bases pois por #
# minha interpretacao do texto, era "dado que" seriam reads de bases e  #
# nao maiores que 1000 reads de ate 1000 bases. Logo, estando sob essas #
# condicoes, eu nao precisaria checar/validar isto nem levantar erros.  #
# Pesquisei em numpy para ver se isso era uma deixa para tipar fortemen-#
# te os reads e/ou otimizar o algoritmo mas deixei em Python puro mesmo.#
#########################################################################

#############################
#  FUNCAO Menor SuperString #
def menorsuperstr(reads, superstr=''):                  # escolha por funcao recursiva pois demanda iteracoes
    if len(reads) == 0:
        return superstr                                     # Caso Base = nao tendo mais reads, return a superstring

    if len(superstr) == 0:                              # INICIO = se superstr vazia,
        superstr = reads.pop(0)                             # superstr recebe o 1o read (topo da lista)
        return menorsuperstr(reads, superstr)               # recursa, passando a superstr (atual) como parametro

    for i in range(len(reads)):                         # APARTIR da 2nd PASS =
        R = reads[i]                                        # para cada read R
        L = len(R)                                          # L = tamanho de R

        for j in range(L/2):                            # Para j em pelo menos metade do tamanho do read
            k = L - j                                       # k serve como posicionador de encaixe

            if superstr.startswith(R[j:]):              # tenta encaixar no inicio (str.startswith() Method)
                reads.pop(i)                                # se sim, remove o read e reitera/recursa
                return menorsuperstr(reads, R[:j] + superstr)    # com a superstr atualizada

            if superstr.endswith(R[:k]):                # tenta encaixar no final (str.startswith() Method)
                reads.pop(i)                                # se sim, mesma coisa
                return menorsuperstr(reads, superstr + R[k:])    # modificando o tail do slice/slicing

##########
#  MAIN  #
if __name__ == "__main__":

    reads_input = open("input.txt").read().splitlines()     # tal funcao da uma lista/array das linhas sem o "\n"

    print menorsuperstr(reads_input)                        # acabei de lembrar que deveria exportar "output.txt"
                                                            # vou commitar assim e mudo depois [LEMBRETE!!!]
