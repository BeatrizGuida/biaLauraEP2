from funcoes import posicao_valida, define_posicoes, preenche_frota

lista_embarcacoes= ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanho=[4, 3, 2, 1]

dicio_frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for i in range(len(lista_embarcacoes)):
    nome= lista_embarcacoes[i]
    tamanho= lista_tamanho[i]
    inicial= input(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')

    linha= int(input('Qual linha voce deseja posicionar sua frota'))
    coluna= int(input('Qual coluna voce deseja posicionar sua frota'))

    if nome != 'submarino':
        orientacao= input('Qual a orientação da sua frota, sendo 1[vertical], 2[horizontal]')

    posicao= posicao_valida(dicio_frota, linha, coluna, orientacao, tamanho)

    while posicao != True:
        print('Esta posição não está válida!')
        linha= int(input('Qual linha voce deseja posicionar sua frota'))
        coluna= int(input('Qual coluna voce deseja posicionar sua frota'))
        if nome != 'submarino':
            orientacao= input('Qual a orientação da sua frota, sendo 1[vertical], 2[horizontal]')

    else:
        def_posi= define_posicoes(linha, coluna, orientacao,tamanho)
        frota= preenche_frota (dicio_frota, nome, linha, coluna, orientacao, tamanho)

print(dicio_frota)
