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
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if nome != "submarino":
            orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
            orientacao = "vertical" if orientacao_input == 1 else "horizontal"
        else:
            orientacao = "horizontal"  

        while not posicao_valida(frota, linha, coluna, orientacao, tamanho):
            print("Esta posição não está válida!")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "horizontal"

        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)

print(frota)
