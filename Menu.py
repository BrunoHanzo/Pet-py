list_produtos = []
list_servico = []

from Financeiro import *

class Menu():
    def __init__(self) -> None:
        pass

    def MenuPrincipal():
        print(' ______________________________________________________________')
        print('|                BEM VINDO AO SISTEMA DO PET-PY                |')
        print('|______________________________________________________________|')
        print('|                      O que deseja fazer?                     |')
        print('|                                                              |')
        print('|  (C) Clientes    (S) Serviços    (F) Financeiro    (E) Sair  |')
        print('|______________________________________________________________|')

    def MenuClientes():
        print(' _________________________________________________')
        print('|                    CLIENTES                     |')
        print('|_________________________________________________|')
        print('|               Selecione a opção:                |')
        print('|_________________________________________________|')
        print('| [1] Fazer cadastro                              |')
        print('| [2] Editar cadastro existente                   |')
        print('| [3] Remover cadastro existente                  |')
        print('| [4] Sair                                        |')
        print('|_________________________________________________|')

    def MenuServicos():
        print(' _________________________________________________')
        print('|                   SERVIÇOS                      |')
        print('|_________________________________________________|')
        print('|               Selecione a opção:                |')
        print('|_________________________________________________|')
        print('| [1] Cadastrar serviço                           |')
        print('| [2] Editar serviço existente                    |')
        print('| [3] Agendar serviço existente                   |')
        print('| [4] Sair                                        |')
        print('|_________________________________________________|')

    def MenuFinanceiro():
        print(' _________________________________________________')
        print('|                   FINANCEIRO                    |')
        print('|_________________________________________________|')
        print('|               Selecione a opção:                |')
        print('|_________________________________________________|')
        print('| [1] Estoque                                     |')
        print('| [2] Fluxo de Caixa                              |')
        print('| [3] Sair                                        |')
        print('|_________________________________________________|')

    def MenuEstoque():
        print(' _________________________________________________')
        print('|                    ESTOQUE                      |')
        print('|_________________________________________________|')
        print('|               Selecione a opção:                |')
        print('|_________________________________________________|')
        print('| [1] Adicionar produto                           |')
        print('| [2] Editar produto existente                    |')
        print('| [3] Remover produto existente                   |')
        print('| [4] Armazem                                     |')
        print('| [5] Sair                                        |')
        print('|_________________________________________________|')

    def MenuArmazem():
        print(' _________________________________________________')
        print('|                    ARMAZÉM                      |')
        print('|_________________________________________________|')
        print('|          Items:             Quantidade:         |')
        with open('Produtos.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for dado in dados:
                print(f'|       {dado["Produto"]:<26}{dado["Quantidade"]:<16}|')
        print('|_________________________________________________|')

    def MenuCaixa(valor_caixa):
        print(' _______________________________________________________')
        print('|                       CAIXA                           |')
        print('|_______________________________________________________|')
        print('|         Descrição:          Fluxo de Caixa:           |')
        print('|        Valor Inicial           R$100.00               |')
        with open('Servicos.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for dado in dados:
                print(f'|{dado["Descricao"]:>16}                R${dado["Custo"]:.2f}                 |')
        print('|_______________________________________________________|')
        print('|                   Valor em caixa:                     |')
        print(f'|                      R${valor_caixa:.2f}                         |')
        print('|_______________________________________________________|')
