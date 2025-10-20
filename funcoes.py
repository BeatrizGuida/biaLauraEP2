#EX 1
def define_posicoes(linha, coluna, orientacao,tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    return posicoes  

def preenche_frota (dicio_frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in dicio_frota:
        dicio_frota[nome_navio] += [lista]
    else:
        dicio_frota[nome_navio]= [lista]

    return dicio_frota


def faz_jogada (tabuleiro, linha, coluna):
    item= tabuleiro[linha][coluna]
    if item == 0:
        tabuleiro[linha][coluna]= '-'
    elif item == 1:
        tabuleiro[linha][coluna]= 'X'
    
    return tabuleiro


def posiciona_frota(dicionario_frota):
    tabuleiro= [[0 for _ in range(10)] for _ in range(10)]
    for navio in dicionario_frota:
        for posicao in dicionario_frota[navio]:
            for coordenada in posicao:
                linha= coordenada[0]
                coluna= coordenada[1]
                tabuleiro[linha][coluna]= 1
    return tabuleiro