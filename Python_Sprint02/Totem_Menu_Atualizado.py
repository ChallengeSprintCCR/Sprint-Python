estacoes = {
    "Sé": ["Consolação", "Paraíso", "Brás", "Liberdade"],
    "Consolação": ["Sé", "Paulista", "Paraíso"],
    "Paraíso": ["Consolação", "Sé"],
    "Brás": ["Sé", "Liberdade"],
    "Liberdade": ["Brás", "Sé"],
    "Paulista": ["Consolação"]
}

pontos_de_interesse = {
    'Sé': ['Catedral da Sé', 'Pateo do Collegio'],
    'Consolação': ['Avenida Paulista', 'MASP'],
    'Brás': ['Museu do Imigrante', 'Shopping Vautier'],
    'Paulista': ['Instituto Moreira Salles', 'Livraria Cultura']
}


def exibir_conexoes(estacoes):
    print("Conexões de metro e estações disponíveis: ")
    for linha, estacao in estacoes.items():
        print(f"{linha}: {', '.join(estacao)}")

def encontrar_conexao(estacoes, estacao_inicial, estacao_final):
    if estacao_inicial in estacoes and estacao_final in estacoes:
        if estacao_final in estacoes[estacao_inicial]:  
            return f"Você pode viajar diretamente de {estacao_inicial} para {estacao_final}."
        else:  
            for estacao_conectada in estacoes[estacao_inicial]:
                if estacao_final in estacoes[estacao_conectada]:
                    return f"Iniciando em {estacao_inicial}, é possível ir para {estacao_final} passando por {estacao_conectada}."
            return f"Não foram encontradas rotas diretas ou indiretas de {estacao_inicial} para {estacao_final}."
    else:
        return 'Uma ou todas estações citadas são inválidas, por favor tente novamente.'

def mostrar_pontos_interesse(pontos_de_interesse, estacao_atual):
    if estacao_atual in pontos_de_interesse:
        return f"Existem os seguintes pontos de turismo próximos em {estacao_atual}: {', '.join(pontos_de_interesse[estacao_atual])}"
    else:
        return f"Não há pontos de turismo próximos de {estacao_atual}."

def menu_metro_smart(estacoes, pontos_de_interesse):
    programa_menu = True
    while programa_menu:  
        print('Bem-vindo ao Metro Smart!')
        print('Selecione como deseja continuar: ')
        print('A - Ver rotas de metro e estações')
        print('B - Encontrar conexões entre duas estações')
        print('C - Pontos de turismo próximos')
        print('D - Finalizar programa')
        escolha = input()

        if escolha == 'A':
            exibir_conexoes(estacoes)

        elif escolha == 'B':
            estacao_inicial = input("Digite a estação de início: ")
            estacao_final = input("Digite a estação de destino: ")
            resultado = encontrar_conexao(estacoes, estacao_inicial, estacao_final)
            print(resultado)

        elif escolha == 'C':
            estacao_atual = input("Insira a estação atual: ")
            resultado = mostrar_pontos_interesse(pontos_de_interesse, estacao_atual)
            print(resultado)

        elif escolha == 'D':
            programa_menu = False  
            print('Encerrando programa')

        else:
            print('Comando inválido, por favor tente novamente.')

menu_metro_smart(estacoes, pontos_de_interesse)
