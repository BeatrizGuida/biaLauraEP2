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


def afundados(dicio_frota, tabuleiro):
    soma = 0
    for nome, listas in dicio_frota.items():
        for navio in listas:
            partes_navio = 0
            partes_acertadas = 0
            for posicao in navio:
                partes_navio += 1
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    partes_acertadas += 1
            if partes_navio == partes_acertadas:
                soma += 1
    return soma



def posicao_valida (dicio_frota, linha, coluna, orientacao, tamanho):
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for l, c in posicoes_novo_navio:
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False

    for lista_navios in dicio_frota.values():
        for navio in lista_navios:
            for posicao in navio:
                if posicao in posicoes_novo_navio:
                    return False

   return True

   
