from funcoes import posicao_valida, define_posicoes, preenche_frota

embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for nome, tamanho, quantidade in embarcacoes:
    for _ in range(quantidade):
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
                    print('Orientação inválida! Digite 1 ou 2.')
                    continue
            else:
                orientacao = None  
            
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            else:
                print('Esta posição não está válida! Tente novamente.')

print(frota)
