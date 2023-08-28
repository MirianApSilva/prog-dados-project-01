from src.csvworker import csvWorker
from src.operatorworker import operatorWorker


# Inicialização de um Objeto 
csvload = csvWorker()
data = csvload.read_csv('project\src\dataset\sample.csv', ';', '1252')
#data = csvload.read_csv('project\src\dataset\steam_games.csv', ',', 'utf-8')

# Inicialização de um Objeto 
operatorload = operatorWorker()


# Chamada da Função top_10_melhores_avaliados
# Nesta seção, a função 'top_10_melhores_avaliados' é chamada para encontrar os 10 jogos mais bem avaliados
# A função recebe os dados do arquivo CSV lidos anteriormente como argumento.
resultado = operatorload.top_10_melhores_avaliados(data)

# Exibição do Resultado
# O resultado contendo informações sobre os 10 jogos mais bem avaliados é impresso na tela.
print(resultado)

# Pergunta 3: Apresente os 10 jogos mais bem avaliados 
# e retorne preço, a quantidade de reviews positivos e negativos.
