# Abrindo o arquivo em modo de leitura
for i in range(2, 673):
    with open('GazetaDoPovo/' + str(i) + '.txt', 'r') as arquivo:
        # Lendo todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Apagando a segunda linha do arquivo
    try:
        del linhas[1]

        # Apagando as últimas 5 linhas do arquivo
        linhas = linhas[:-5]
    except:
        print('arquivo vazio')

    # Abrindo o arquivo em modo de escrita
    with open('GazetaDoPovo/' + str(i) + '.txt', 'w') as arquivo:
        # Escrevendo as linhas restantes no arquivo
        for linha in linhas:
            arquivo.write(linha)