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


from funcoes import posiciona_frota, faz_jogada, afundados

# dicionario dado no enunciado
frota_jogador = {
    "porta-aviões": [[[0, 0], [0, 1], [0, 2], [0, 3]]],
    "navio-tanque": [[[2, 1], [3, 1], [4, 1]], [[9, 0], [9, 1], [9, 2]]],
    "contratorpedeiro": [[[5, 4], [5, 5]], [[6, 7], [7, 7]], [[1, 9], [2, 9]]],
    "submarino": [[[3, 4]], [[4, 8]], [[8, 9]], [[0, 9]]]
}

frota_oponente = {
    "porta-aviões": [[[1, 1], [1, 2], [1, 3], [1, 4]]],
    "navio-tanque": [[[3, 3], [3, 4], [3, 5]], [[6, 0], [6, 1], [6, 2]]],
    "contratorpedeiro": [[[5, 6], [5, 7]], [[8, 3], [8, 4]], [[2, 8], [3, 8]]],
    "submarino": [[[9, 9]], [[0, 0]], [[4, 5]], [[7, 3]]]
}

# tabuleiros
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_oponente_visivel = [[' ' for _ in range(10)] for _ in range(10)]

# loop principal do jogo 
jogando = True

while jogando:
    print("Seu tabuleiro:")
    for linha in tabuleiro_jogador:
        print(' '.join(str(item) for item in linha))

    print("Tabuleiro do oponente:")
    for linha in tabuleiro_oponente_visivel:
        print(' '.join(linha))

    jogada_valida = False
    while not jogada_valida:
        linha_ataque = int(input("Digite a linha de ataque (0-9): "))
        coluna_ataque = int(input("Digite a coluna de ataque (0-9): "))

        if tabuleiro_oponente_visivel[linha_ataque][coluna_ataque] in ['-', 'X']:
            print("Você já jogou nessa posição! Escolha outra.")
        else:
            jogada_valida = True  # sai do while

    # atualiza tabuleiros com o resultado da jogada
    if tabuleiro_oponente[linha_ataque][coluna_ataque] == 1:
        print("Acertou um navio!")
        tabuleiro_oponente[linha_ataque][coluna_ataque] = 'X'
        tabuleiro_oponente_visivel[linha_ataque][coluna_ataque] = 'X'
    else:
        print("Errou o tiro!")
        tabuleiro_oponente[linha_ataque][coluna_ataque] = '-'
        tabuleiro_oponente_visivel[linha_ataque][coluna_ataque] = '-'

    # verifica navios afundados
    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
    print(f"Navios afundados do oponente: {navios_afundados}")

    if navios_afundados == 10:
        print("Parabéns! Você venceu a batalha!")
        jogando = False
