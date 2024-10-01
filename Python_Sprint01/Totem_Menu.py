estacoes = {
    "Estação A": ["Estação B", "Estação C", "Estação D", "Estação E"],
    "Estação C": ["Estação A", "Estação F", "Estação B"],
    "Estação B": ["Estação C", "Estação A"],
    "Estação D": ["Estação A", "Estação E"],
    "Estação E": ["Estação D", "Estação A"],
    "Estação F": ["Estação C"]
}

pontos_de_interesse = {
    'Estação A': ['Museu', 'Shopping'],
    'Estação C': ['Parque', 'Estadio'],
    'Estação D': ['Hospital', 'Faculdade'],
    'Estação F': ['Terminal de onibus', 'Lugar historico'],
}

programa_menu = True

while programa_menu:  #Mantem o programa rodando
    print('Bem vindo ao Metro Smart!')
    print('Selecione como deseja continuar: ')
    print('A - Ver rotas de metro e estações')
    print('B - Encontrar conexões entre duas estações')
    print('C - Pontos de turismo próximos')
    print('D - Finalizar programa')
    escolha = input()
    if escolha == 'A':    #Pega todas as variaveis dentro de "estacoes" e mostra ao usuário
        print("Conexões de metro e estações disponiveis: ")
        for linha, estacao in estacoes.items():
            print(f"{linha}: {', '.join(estacao)}")
            
    elif escolha == 'B':
        estacao_inicial = input("Digite a estação de inicio: ")  #Pega a estação inicial e final do usuario
        estacao_final = input("Digite a estação de destino: ")
        
        if estacao_inicial in estacoes and estacao_final in estacoes: #Analisa se as estações citadas estão dentre as disponiveis 
            if estacao_final in estacoes[estacao_inicial]:   #Analisa se a rota da estação inicial passa pela final
                print(f"Você pode viajar diretamente de {estacao_inicial} para {estacao_final}.")
            else:
                rota_encontrada = False #Afirma que não foi encontrada uma rota direta
                for estacao_conectada in estacoes[estacao_inicial]: #cria uma variavel "estacao_conectada" que analisa se ela existe entre a inicial e final
                    if estacao_final in estacoes[estacao_conectada]:
                        print(f"Iniciando em {estacao_inicial} é possivel ir para {estacao_final} passando por {estacao_conectada}.")
                        rota_encontrada = True  #Afirma que uma rota foi encontrada
                if not rota_encontrada:
                    print(f"Não foram encontradas rotas diretas ou indiretas de {estacao_inicial} para {estacao_final}.")
        else:
            print('Uma ou todas estações citadas são inválidas, por favor tente novamente.')
            
    elif escolha == 'C':   #Pega a estação atual do usuário e afirma se existe algum ponto de turismo próximo
        estacao_atual = input("Insira a estação atual: ")
        
        if estacao_atual in pontos_de_interesse:
            print(f"Existem os seguintes pontos de turismo próximos em {estacao_atual}: {', '.join(pontos_de_interesse[estacao_atual])}")
        else:
            print(f"Não há pontos de turismo próximos de {estacao_atual}.")
            
    elif escolha == 'D':   
        programa_menu = False   #Afirma que o programa foi encerrado e finaliza ele
        print('Encerrando programa')
        
    else:
        print('Comando inválido, por favor tentar outro.')