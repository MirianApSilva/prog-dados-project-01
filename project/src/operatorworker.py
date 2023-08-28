from datetime import datetime
from  project.src.csvworker import *

class operatorWorker:
  
  def __init__(self):
      ''' Este é o construtor da classe. Ele pode ser usado para inicializar atributos da classe.'''
      pass  # 'pass' indica que este construtor está vazio por enquanto.
    
  def count_values(self, data, columnGroup):
    '''
    Conta a ocorrência de valores em uma coluna específica de uma lista de dados e 
    calcula os percentuais totais.

    Args:
        data (list of dict): Uma lista de dicionários.
        columnGroup (str): O nome da coluna pela qual os dados serão agrupados e contados.

    Returns:
        dict: Um dicionário onde as chaves são os valores únicos encontrados na coluna de agrupamento
        e os valores são dicionários contendo a contagem de ocorrências e o percentual em relação ao
        número total de elementos na lista.
        
    Example:
        >>> data = [
                {'ID': 1, 'Group': 'A'},
                {'ID': 2, 'Group': 'B'},
                {'ID': 3, 'Group': 'A'},
                {'ID': 4, 'Group': 'C'},
                {'ID': 5, 'Group': 'B'},
            ]
        >>> columnGroup = 'Group'
        >>> result = count_values(data, columnGroup)
        >>> print(result)
        {'A': {'count': 2, 'percent': 40.0},
         'B': {'count': 2, 'percent': 40.0},
         'C': {'count': 1, 'percent': 20.0}}
    '''
    list_values = {}
    total_count = len(data)

    for row in data:
      group = str(row[columnGroup])
      if group not in list_values :
        list_values[group] = 1
      else:
        list_values[group] = list_values[group] + 1

     # Calcular o percentual total
    for key, value in list_values.items():
         percent = (value / total_count) * 100
         list_values[key] = {
             'count': value,
             'percent': percent
         }

    return list_values

  def price_transform(self, price):
    '''
    Verifica e retorna se um item é grátis ou pago com base no preço.

    Args:
        price (float): O preço do item a ser verificado.

    Returns:
        str: Uma string indicando se o item é "pago" ou "gratis" com base no preço fornecido.

    Example:
        >>> item_price = 0
        >>> result = price_transform(item_price)
        >>> print(result)
        'gratis'
        
        >>> item_price = 10.5
        >>> result = price_transform(item_price)
        >>> print(result)
        'pago'
    '''
    # Converte o preço para um valor em ponto flutuante
    value = float(price)
    
    if value > 0:
        # Se o preço for maior que 0, retorna 'pago'
        return 'pago'
    else:
        # Se o preço for igual a 0, retorna 'gratis'
        return 'gratis'
      
  def split_date(self, date, kind):
    '''
    Separa uma data em dia, mês e ano, de acordo com o tipo especificado.

    Args:
        date (str): A data no formato "dia/mes/ano".
        kind (str): O tipo de informação desejada: "dia", "mes" ou "ano".

    Returns:
        str: A parte da data especificada pelo tipo.

    Example:
        >>> date = "15/02/2022"
        >>> kind = "year"
        >>> resultado = split_date(data, kind)
        >>> print(resultado)
        '2022'
    '''
    try:
        date = datetime.strptime(date, '%b %d, %Y')
        date = date.strftime('%Y-%m-%d')
    except ValueError:
        return "Data inválida"
          
    spt_date = date.split('-')
    
    if kind == 'ano':
        return spt_date[0]
    elif kind == 'mes':
        return spt_date[1]
    elif kind == 'dia':
        return spt_date[2]
    else:
        return "Tipo de data inválido"

  def list_highest_count(self, data):
    '''
    Encontra e retorna o(s) ano(s) com a maior contagem de um dicionário de dados.
    Args:
        data (dict): Um dicionário onde as chaves são anos e os valores são dicionários com o campo 'count'.

    Returns:
        dict: Um dicionário contendo o(s) ano(s) com a maior contagem e suas contagens correspondentes.

    Exemplo:
        >>> data = {
                '2016': {'count': 2, 'percent': 10.0},
                '2020': {'count': 5, 'percent': 25.0},
                '2017': {'count': 2, 'percent': 10.0},
                '2019': {'count': 1, 'percent': 5.0},
                '2018': {'count': 3, 'percent': 15.0},
                '2012': {'count': 1, 'percent': 5.0},
                '2021': {'count': 2, 'percent': 10.0},
                '2011': {'count': 1, 'percent': 5.0},
                '2022': {'count': 3, 'percent': 15.0}
            }
        >>> resultado = listar_maior_contagem(data)
        >>> print(resultado)
        {'2018': 3, '2020': 5, '2022': 3}
    '''
    # Inicializa variáveis para rastrear a maior contagem e uma lista de anos empatados
    maior_contagem = -1
    list_empatados = []
    dict_values = {}

    # Itera pelo dicionário para encontrar a maior contagem
    for ano, dados in data.items():
        contagem = dados['count']
        if contagem > maior_contagem:
            maior_contagem = contagem
            list_empatados = [ano]
        elif contagem == maior_contagem:
            list_empatados.append(ano)
            
    # Ordena os anos empatados para consistência
    # Cria um dicionário com os anos empatados e suas contagens       
    for row in sorted(list_empatados):
        dict_values[row] =  data[row]['count']
             
    return dict_values

  def top_10_melhores_avaliados(self, data):
    dict_values = {}
   
    for row in data:
        total_reviews = float(row['Positive']) + float(row['Negative'])
        
        if total_reviews > 0:
            percent = (float(row['Positive']) / total_reviews) * 100
        else:
            percent = 0
            
        key = row['AppID']
        dict_values[key] = {
            'app_id': key,
            'Name': row['Name'],
            'total_reviews' :total_reviews,
            'percent_reviews' : percent,
            'positive_reviews' : float(row['Positive']),
            'negative_reviews' : float(row['Negative']),
            'price' : float(row['Price'])
            }
    #Classifica os jogos com base nas revisões positivas em ordem decrescente    
    sorted_list = sorted(dict_values.values(), key=lambda x:x['positive_reviews'], reverse=True)

    #Pega os 10 jogos mais bem avaliados (ou menos se houver menos de 10 jogos)
    top_10_jogos = sorted_list[:10]

    return top_10_jogos