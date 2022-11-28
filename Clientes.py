import json
import shutil
import tempfile
import os

arquivo_cliente = 'Clientes.json'
contagem_clientes = 1
if os.path.exists('Clientes.json'):
    with open('Clientes.json', 'r', encoding='utf-8') as arq:
        lista_cliente = json.load(arq)
else:
    lista_cliente = []

class Clientes():
    def __init__(self, id, pet, tutor, tipo_animal, contato ):
        self.id = id
        self.pet = pet
        self.tutor = tutor
        self.tipo_animal = tipo_animal
        self.contato = contato

    def salvar_cadastro(self):
        Cadastro = {}
        Cadastro['ID'] = self.id
        Cadastro['Pet'] = self.pet
        Cadastro['Tutor'] = self.tutor
        Cadastro['Tipo_Animal'] = self.tipo_animal
        Cadastro['Contato'] = self.contato
        lista_cliente.append(Cadastro.copy())
        print(lista_cliente)
        clientes = json.dumps(lista_cliente,indent=5)
        with open('Clientes.json', 'w', encoding='utf-8') as outfile:
            outfile.write(clientes)
        print(f'O cadastro {Cadastro} foi realizado com sucesso!')
        return os.path.exists('Clientes.json')

    def editar_cadastro(self):
        with open('Clientes.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            alterar = int(input('Informe o ID para alteração: '))
            for dado in dados:
                if alterar == int(dado['ID']):
                    dado['Pet'] = input('Pet: ')
                    dado['Tutor'] = input('Tutor: ')
                    dado['Tipo_Animal'] = input('Tipo_Animal: ')
                    dado['Contato'] = input('Contato: ')    
            json.dump(dados, out, ensure_ascii=False, indent=5)
        shutil.move(out.name, 'Clientes.json')


    def excluir_cadastro(self):
        with open('Clientes.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            excluir = int(input('Informe o ID para exclusão: '))
            for dado in dados:
                if excluir == int(dado['ID']):
                    print(f'O ID {dado["ID"]} foi excluido com sucesso!')
                    dado.clear()
            json.dump(dados, out, ensure_ascii=False, indent=5)
        shutil.move(out.name, 'Clientes.json')

