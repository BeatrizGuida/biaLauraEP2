from funcoes import posicao_valida, define_posicoes, preenche_frota

lista_embarcacoes = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanho = [4, 3, 2, 1]

dicio_frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for i in range(len(lista_embarcacoes)):
    nome = lista_embarcacoes[i]
    tamanho = lista_tamanho[i]

    print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
    

    while True:  
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if nome != 'submarino':
            orientacao_num = int(input('Orientação (1 - vertical, 2 - horizontal): '))
            if orientacao_num == 1:
                orientacao = 'vertical'
            elif orientacao_num == 2:
                orientacao = 'horizontal'
            
        else:
            orientacao = None  

        if posicao_valida(dicio_frota, linha, coluna, orientacao, tamanho):
            dicio_frota = preenche_frota(dicio_frota, nome, linha, coluna, orientacao, tamanho)
            break  
        else:
            print('Esta posição não está válida! Tente novamente.')

print(dicio_frota)

