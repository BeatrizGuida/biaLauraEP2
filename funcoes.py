#EX 1
def define_posicoes(linha, coluna, orientacao,tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
<<<<<<< HEAD
            posicoes.append((linha + i, coluna))
    return posicoes  


def preenche_frota (dicio_frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in dicio_frota:
        dicio_frota[nome_navio] += lista
    else:
        dicio_frota[nome_navio]= lista

    return dicio_frota
=======
            posicoes.append([linha + i, coluna])
    return posicoes  
>>>>>>> 0065d6562a5202dc857956fbc90484347f024230
