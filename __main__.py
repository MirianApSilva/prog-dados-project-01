"""CLI entry point."""
from project.src.pergunta01 import *
from project.src.pergunta02 import *
from project.src.pergunta03 import *

def main():
    """"""
    print('----------- Iniciando Processamento dos Dados ----------- ')
    print('----------- Buscando Dados                    ----------- ')
    print('----------- Segue resposta da 1ª pergunta     ----------- ')
    pergunta_01()
    print('----------- Buscando Dados                    ----------- ')
    print('----------- Segue resposta da 2ª pergunta     ----------- ')
    pergunta_02()
    print('----------- Buscando Dados                    ----------- ')
    print('----------- Segue resposta da 3ª pergunta     ----------- ')
    pergunta_03()

if __name__ == "__main__":
    main()