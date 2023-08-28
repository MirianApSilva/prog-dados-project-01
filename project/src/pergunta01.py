from project.src.csvworker import csvWorker
from project.src.operatorworker import operatorWorker

def pergunta_01():
  # Inicialização de um Objeto 
  csvload = csvWorker()
  data = csvload.read_csv('project\src\dataset\steam_games.csv', ',', 'utf-8')

  # Inicialização de um Objeto 
  operatorload = operatorWorker()

  # Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
  # Transformação de Preço em Tipo (Gratuito ou Pago) (Função: price_transform)
  for row  in data:
    # Atribuição do Tipo de Preço
    # O resultado da função price_transform (gratuito ou pago) é atribuído a uma nova chave chamada 'typePrice' no dicionário 'row'.
    column = operatorload.price_transform(row['Price'])
    row['typePrice'] = column
    # Cálculo da Contagem de Tipos de Preço (Função: count_values)
    # A função count_values é chamada para calcular a contagem de tipos de preço (gratuito ou pago) a partir dos dados processados.
  totalGames = operatorload.count_values(data, 'typePrice')
  print(totalGames)
  # Resultados
  # O resultado final, armazenado na variável 'totalGames', conterá a contagem de jogos gratuitos e pagos na plataforma.
