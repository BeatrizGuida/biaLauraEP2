from funcoes import posicao_valida, define_posicoes, preenche_frota

lista_embarcacoes = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanho = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

for i in range(len(lista_embarcacoes)):
    nome = lista_embarcacoes[i]
    tamanho = lista_tamanho[i]
    quantidade = quantidades[i]

    for _ in range(quantidade):
        posicao_valida_flag = False

        while not posicao_valida_flag:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "horizontal" 

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                posicao_valida_flag = True
            else:
                print("Esta posição não está válida!")

print(frota)



from funcoes import (define_posicoes, preenche_frota, posicao_valida,
                     posiciona_frota, faz_jogada, afundados)

lista_embarcacoes = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
lista_tamanho = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

# Frota do oponente (dado enunciado)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

MAX = 9  # índices válidos 0..9

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    linha = 0
    while linha <= MAX:
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto = texto + f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        linha = linha + 1
    return texto


posiciona_frota(frota_oponente)

i = 0
while i < len(lista_embarcacoes):
    nome = lista_embarcacoes[i]
    tamanho = lista_tamanho[i]
    quantidade = quantidades[i]

    copia = 0
    while copia < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")

        # valida linha (0..9) 
        linha_ok = False
        while linha_ok == False:
            entrada_linha = input("Linha: ").strip()
            if entrada_linha.isdigit():
                valor_linha = int(entrada_linha)
                if 0 <= valor_linha <= MAX:
                    linha = valor_linha
                    linha_ok = True
                else:
                    print("Linha inválida!")
            else:
                print("Linha inválida!")

        # valida coluna (0..9)
        coluna_ok = False
        while coluna_ok == False:
            entrada_coluna = input("Coluna: ").strip()
            if entrada_coluna.isdigit():
                valor_coluna = int(entrada_coluna)
                if 0 <= valor_coluna <= MAX:
                    coluna = valor_coluna
                    coluna_ok = True
                else:
                    print("Coluna inválida!")
            else:
                print("Coluna inválida!")

        # orientacao (submarino: horizontal por padrão)
        if nome == "submarino":
            orientacao = "horizontal"
        else:
            orientacao_ok = False
            while orientacao_ok == False:
                escolha = input("[1] Vertical [2] Horizontal >").strip()
                if escolha == '1':
                    orientacao = "vertical"
                    orientacao_ok = True
                elif escolha == '2':
                    orientacao = "horizontal"
                    orientacao_ok = True
                else:
                    print("Escolha inválida. Digite 1 ou 2.")

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            copia = copia + 1
        else:
            print("Esta posição não está válida!")
    i = i + 1



# Cria tabuleiros

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

# total de navios do oponente (para verificar vitória)
total_navios_oponente = 0
chaves = list(frota_oponente.keys())
idx_chaves = 0
while idx_chaves < len(chaves):
    listas = frota_oponente[chaves[idx_chaves]]
    total_navios_oponente = total_navios_oponente + len(listas)
    idx_chaves = idx_chaves + 1


#  Loop principal 

jogando = True
while jogando == True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # obter uma jogada válida e inédita 
    jogada_valida = False
    while jogada_valida == False:
        # ler linha de ataque
        linha_ok = False
        while linha_ok == False:
            entrada_linha = input("Jogador, qual linha deseja atacar? ").strip()
            if entrada_linha.isdigit():
                valor_linha = int(entrada_linha)
                if 0 <= valor_linha <= MAX:
                    linha_atq = valor_linha
                    linha_ok = True
                else:
                    print("Linha inválida!")
            else:
                print("Linha inválida!")

        # ler coluna de ataque
        coluna_ok = False
        while coluna_ok == False:
            entrada_coluna = input("Jogador, qual coluna deseja atacar? ").strip()
            if entrada_coluna.isdigit():
                valor_coluna = int(entrada_coluna)
                if 0 <= valor_coluna <= MAX:
                    coluna_atq = valor_coluna
                    coluna_ok = True
                else:
                    print("Coluna inválida!")
            else:
                print("Coluna inválida!")

        valor_atual = tabuleiro_oponente[linha_atq][coluna_atq]
        ja_informada = False
        if str(valor_atual) == 'X' or str(valor_atual) == '-':
            ja_informada = True
        if ja_informada == True:
            print(f"A posição linha {linha_atq} e coluna {coluna_atq} já foi informada anteriormente!")
            jogada_valida = False
        else:
            jogada_valida = True

    # efetua a jogada
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_atq, coluna_atq)

    # verifica vitória
    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
    if navios_afundados == total_navios_oponente:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

# fim do arquivo
