import json
import os
import shutil
import tempfile
import unittest

from Menu import *
from Clientes import *
from Servicos import *
from Financeiro import *

#Variaveis

#Cliente
arquivo_cliente = 'Clientes.json'
contagem_clientes = 1

#Servico
arquivo_servico = 'Servicos.json'
contagem_servicos = 1
lista_servicos = []
lista_agendamentos = []

#Financeiro
arquivo_produto = 'Produtos.json'
lista_produtos = []
contagem_produtos = 1

class Test_json_exists(unittest.TestCase):
    def test_Servicos_json(self):
        obj = Servicos(1,'vacinaçao','raiva','12,25','12 min')
        self.assertTrue(obj.salvar_servico(), 'Está cadastrando os serviços com sucesso, e criando um json chamado Servicos.json!')
        print()

    def test_Clientes_json(self):
        obj = Clientes(1,'Koby','Hanzo','Cachorro','31975473419')
        self.assertTrue(obj.salvar_cadastro(),'Está cadastrando os produtos com sucesso, e criando um json chamado Clientes.json!')
        print()

    def test_Financeiro_json(self):
        obj = Financeiro(1,'Vacina',25)
        self.assertTrue(obj.cadastrar_produto(), 'Está cadastrando os produtos com sucesso, e criando um json chamado Produtos.json!')

    def test_Agendamento_jsot(self):
        obj = Servicos(1,'vacinaçao','raiva','12,25','12 min')
        self.assertTrue(obj.agendar_servico('8:30','Iarin'),'Está cadastrando os produtos com sucesso, e criando um json chamado Agendamento.json!')

if __name__ == '__name__':
    print()
    unittest.main()
