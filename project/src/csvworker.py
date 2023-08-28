import csv
import random

class csvWorker:
  
  def __init__(self):
      ''' Este é o construtor da classe. Ele pode ser usado para inicializar atributos da classe.'''
      pass  #este construtor está vazio por enquanto.

  def read_csv(self, full_path, delimiter, encoding):
    '''
      Define a função read_csv que tem a finalidade de ler um arquivo CSV 
      e retornar seus dados em formato de lista de dicionários. \n
      
      Parâmetros:\n
        * full_path -> O caminho completo (incluindo o nome do arquivo) para o arquivo CSV que você deseja ler.
        * delimiter -> O caractere que é usado como delimitador no arquivo CSV (por exemplo, ',' para CSVs com vírgula ou ';' para CSVs com ponto e vírgula).
    
    '''   
    list_data = []
    
    try:
      with open(full_path, 'r', encoding= encoding) as csvfile:
        dataloaded = csv.DictReader(csvfile, delimiter= delimiter)
        for row in dataloaded:
         list_data.append(row)
        return list_data 
    except FileNotFoundError as error:
      return error

  def write_csv(self, columns, data):
    '''
      O resultado final será um arquivo CSV chamado 'sample.csv' com o cabeçalho definido pelos primeiro parametro
      e as linhas de dados provenientes dos dicionários dado pelo segundo parametro.
      
      Parametros:\n
       * columns -> Nome das colunas
       * data    -> Dicionario contendo os dados
       
    '''
    try:
      with open('dataset\data\sample.csv', 'w', newline='', encoding= 'utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= columns, delimiter= ';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    except PermissionError as perm :
        return perm
    except FileExistsError as ferr:
        return ferr

    
  def get_random_sample(self, data:list, size:int):   
    '''
    Esse código é usado para extrair uma amostra aleatória de uma lista de dados e armazená-la 
    em outra variável para análises ou processamento adicionais.\n
    
    Parametros:\n
     * data -> Esta é uma lista de dados da qual você deseja extrair uma amostra aleatória.
     * size -> Este é o tamanho da amostra aleatória que você deseja extrair da lista data.
    '''
    
    return random.sample(data,size)