import json
import shutil
import tempfile
import os

arquivo_produto = 'Produtos.json'
contagem_produtos = 1
lista_produtos = []

class Financeiro():
    def __init__(self, id, produto, quantidade):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade

    def cadastrar_produto(self):
        Produto = {}
        Produto['ID'] = self.id
        Produto['Produto'] = str(self.produto)
        Produto['Quantidade'] = int(self.quantidade)
        lista_produtos.append(Produto.copy())
        print(lista_produtos)
        produtos = json.dumps(lista_produtos,indent=3)
        with open('Produtos.json', 'w', encoding='utf-8') as outfile:
            outfile.write(produtos)
        print(f'O produto {Produto} foi realizado com sucesso!')
        return os.path.exists('Produtos.json')

    def editar_produto(self):
        with open('Produtos.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            alterar = int(input('Informe o ID para alteração: '))
            for dado in dados:
                if alterar == int(dado['ID']):
                    dado['Produto'] = input('Produto: ')
                    dado['Quantidade'] = int(input('Quantidade: '))  
            json.dump(dados, out, ensure_ascii=False, indent=3)
        shutil.move(out.name, 'Produtos.json')


    def excluir_produto(self):
        with open('Produtos.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            excluir = int(input('Informe o ID para exclusão: '))
            for dado in dados:
                if excluir == int(dado['ID']):
                    print(f'O produto {dado["ID"]} foi excluido com sucesso!')
                    dado.clear()
            json.dump(dados, out, ensure_ascii=False, indent=5)
        shutil.move(out.name, 'Produtos.json')


    def armazem_produtos(self):
        while True:
            resp = input('Deseja alterar a quantidade de algum item? ').upper()
            if resp == 'N':
                break
            elif resp == 'S': 
                print('De qual item deseja alterar a quantidade? ')
                print()
                with open('Produtos.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
                    dados = json.load(arq)
                    for dado in dados:
                        print(dado)
                    alterar = int(input('Informe o ID para alterar quantidade: '))
                    for dado in dados:
                        if alterar == int(dado['ID']):
                            dado['Quantidade'] = int(input('Digite a quantidade: ')) 
                            print(f'O produto {dado["Produto"]} teve sua quantidade alterada para {dado["Quantidade"]}!')
                    json.dump(dados, out, ensure_ascii=False, indent=3)
                shutil.move(out.name, 'Produtos.json')
                break
          