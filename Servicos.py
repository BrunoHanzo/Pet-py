import json
import shutil
import tempfile
import os

arquivo_servico = 'Servicos.json'
contagem_servicos = 1
if os.path.exists('Servicos.json'):
    with open('Servicos.json', 'r', encoding='utf-8') as arq:
        lista_servicos = json.load(arq)
else:
    lista_servicos = []

if os.path.exists('Agendamento.json'):
    with open('Agendamento.json', 'r', encoding='utf-8') as arq:
        lista_agendamentos = json.load(arq)
else:
    lista_agendamentos = []


class Servicos():
    def __init__(self, id, tipo_servico, descricao, custo, duracao):
        self.id = id
        self.tipo_servico = tipo_servico
        self.descricao = descricao
        self.custo = str(custo).replace(',','.')
        self.duracao = duracao

    def salvar_servico(self):
        Servico = {}
        Servico['ID'] = self.id
        Servico['Tipo_Servico'] = str(self.tipo_servico)
        Servico['Descricao'] = str(self.descricao)
        Servico['Custo'] = float(self.custo)
        Servico['Duracao'] = str(self.duracao)
        lista_servicos.append(Servico.copy())
        print(lista_servicos)
        servicos = json.dumps(lista_servicos,indent=5)
        with open('Servicos.json', 'w', encoding='utf-8') as outfile:
            outfile.write(servicos)
        print(f'O servico {Servico} foi realizado com sucesso!')
        return os.path.exists('Servicos.json')

    def editar_servico(self):
        with open('Servicos.json', 'r', encoding='utf-8') as arq, tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            alterar = int(input('Informe o ID para alteração: '))
            for dado in dados:
                if alterar == int(dado['ID']):
                    dado['Tipo_Servico'] = input('Tipo_Servico: ')
                    dado['Descricao'] = input('Descrição: ')
                    self.custo = str(input('Custo: ')).replace(',','.')
                    dado['Custo'] = float(self.custo)
                    dado['Duracao'] = input('Duração: ')    
            json.dump(dados, out, ensure_ascii=False, indent=5)
        shutil.move(out.name, 'Servicos.json')


    def agendar_servico(self,horario,tutor):
        Agendamento = {}
        with open('Servicos.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            for dado in dados:
                print(dado)
            agendar = int(input('Informe o ID para agendar o serviço: '))
            for dado in dados:
                if agendar == int(dado['ID']):
                    Agendamento['Servico'] = agendar
                    Agendamento['Horario'] = horario
                    Agendamento['Cliente'] = tutor
                    lista_agendamentos.append(Agendamento.copy())
        agendamentos = json.dumps(lista_agendamentos, indent=3)
        with open('Agendamento.json', 'w') as outfile:
            outfile.write(agendamentos)
        print(f'O serviço foi agendado para as {Agendamento["Horario"]}!')
        return os.path.exists('Agendamento.json')
