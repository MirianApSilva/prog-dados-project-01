from project.src.csvworker import csvWorker
from project.src.operatorworker import operatorWorker

def pergunta_02():
    # Inicialização de um Objeto 
    csvload = csvWorker()
    data = csvload.read_csv('project\src\dataset\steam_games.csv', ',', 'utf-8')
    # Inicialização de um Objeto 
    operatorload = operatorWorker()
    # Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
    # Exemplo de uso:
    # Iteração sobre os Dados
    for row in data:
        # Extração do Ano da Data de Lançamento(Função:split_date)
        # Atribuição do Ano Extraído à Chave 'year'
        # O ano extraído da data de lançamento é atribuído a uma nova chave chamada 'year'.
        column = operatorload.split_date(row['Release date'], 'ano')
        row['year'] = column

    # Cálculo da Contagem de Anos Únicos(Função: count_values)
    # A função count_values é chamada para calcular a contagem de anos únicos a partir dos dados processados.
    # Ela recebe dois argumentos: o dicionario de dados 'data' e a coluna 'year' que representa os anos.
    groupValues = operatorload.count_values(data, 'year')

    # Identificação do(s) Ano(s) com o maior número de novos jogos(Funcao: list_highest_count)
    years = operatorload.list_highest_count(groupValues)
    print(years)
    # Resultados
    # O resultado final, armazenado na variável 'years', conterá os anos com o maior número de novos jogos e suas contagens correspondentes.