import json
import os

from Menu import *
from Clientes import *
from Servicos import *
from Financeiro import *

#Variaveis

#Cliente
arquivo_cliente = 'Clientes.json'

#Servico
arquivo_servico = 'Servicos.json'
lista_servicos = []
lista_agendamentos = []

#Financeiro
arquivo_produto = 'Produtos.json'
lista_produtos = []


class Choices():
    def __init__(self, choice):
        self.choice = choice

    def choice_cliente(self):
        contagem_clientes = 1
        print()
        cliente = Clientes(0,0,0,0,0)
        while True:
            Menu.MenuClientes()
            if os.path.exists(arquivo_cliente) == False:
                print('Não existe clientes cadastrados!')
                print('O que deseja cadastrar?')
                print()
                opcao_clientes = 1
            else:
                opcao_clientes = int(input())

            if opcao_clientes == 1:
                    while True:
                        cliente = Clientes(contagem_clientes,input('Pet: '),input('Tutor: '),input('Tipo_animal: '),input('Contato: '))
                        contagem_clientes += 1
                        cliente.salvar_cadastro()
                        resp = input('Deseja continuar? [S/N] ').upper()
                        if resp == 'N':
                            break


            elif opcao_clientes == 2:
                    while True:
                        cliente.editar_cadastro()
                        resp = input('Deseja editar mais algum cadastro? [S/N] ').upper()
                        if resp == 'N':
                            break

            elif opcao_clientes == 3:
                    while True:
                        cliente.excluir_cadastro()
                        resp = input('Deseja excluir mais algum cadastro? [S/N] ').upper()
                        if resp == 'N':
                            break

            elif opcao_clientes == 4:
                    break


    def choice_servicos(self):
        contagem_servicos = 1
        print()
        servico = Servicos(0,0,0,0,0)
        while True:
            Menu.MenuServicos()
            if os.path.exists(arquivo_servico) == False:
                print('Não existe serviços cadastrados!')
                print('O que deseja cadastrar?')
                print()
                opcao_servicos = 1
            else:
                opcao_servicos = int(input())

            if opcao_servicos == 1:
                    while True:
                        servico = Servicos(contagem_servicos,input('Tipo_Serviço: '),input('Descrição: '),str(input('Custo: ').replace(',','.')),input('Duração: '))
                        contagem_servicos += 1
                        servico.salvar_servico()
                        resp = input('Deseja adicionar mais serviços? [S/N] ').upper()
                        if resp == 'N':
                            break

            elif opcao_servicos == 2:
                    while True:
                        with open('Servicos.json', 'r') as f:
                            dados = json.load(f)
                            if len(dados) < 1:
                                print('Não possui serviços cadastrados!')
                                break
                            else:
                                servico.editar_servico()
                                resp = input('Deseja editar mais serviços? [S/N] ').upper()
                                if resp == 'N':
                                    break

            elif opcao_servicos == 3:
                    while True:
                        with open('Servicos.json', 'r') as f:
                            dados = json.load(f)
                            if len(dados) < 1:
                                print('Não possui serviços cadastrados!')
                                break
                            else:
                                servico.agendar_servico(input('Horário: '),input('Tutor: '))
                                resp = input('Deseja agendar mais serviços? [S/N] ').upper()
                                if resp == 'N':
                                    break

            elif opcao_servicos == 4:
                    break
        
    def choice_financeiro(self):
        contagem_produtos = 1
        print()
        estoque = Financeiro(0,0,0)
        while True:
            Menu.MenuFinanceiro()
            financeiro = int(input())
            if financeiro == 1:
                Menu.MenuEstoque()
                if os.path.exists(arquivo_produto) == False:
                    print('Não existe produtos cadastrados!')
                    print('O que deseja cadastrar?')
                    print()
                    opcao_estoque = 1
                else:
                    opcao_estoque = int(input())

                if opcao_estoque == 1:
                    while True:
                        estoque = Financeiro(contagem_produtos,input('Produto: '), input('Quantidade: '))
                        contagem_produtos += 1
                        estoque.cadastrar_produto()
                        resp = input('Deseja adicionar mais items? ').upper()
                        if resp == 'N':
                            break
                                    
                if opcao_estoque == 2:
                    while True:
                        estoque.editar_produto()
                        resp = input('Deseja editar mais algum produto? ').upper()
                        if resp == 'N':
                            break
                
                if opcao_estoque == 3:
                    while True:
                        estoque.excluir_produto()
                        resp = input('Deseja excluir mais produtos? ').upper()
                        if resp == 'N':
                            break
                                    
                if opcao_estoque == 4:
                    Menu.MenuArmazem()
                    estoque.armazem_produtos()
                    input('Pressione ENTER para sair!')

                if opcao_estoque == 5:
                    break

            elif financeiro == 2:
                valor_inicial = 100
                Menu.MenuCaixa(valor_inicial)
                input('Aperte a tecla ENTER para sair!')
            
            elif financeiro == 3:
                break