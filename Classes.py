from Algoritmo import *
class Tarefas():
    def __init__(self, descricao, lista, nome):
        
        
        self.lista= lista
        
        self.descricao = descricao
        
        self.nome= nome
    

    def adicionar_tarefa(self, nome, descricao:str):
        self.nome= nome
        self.descricao = descricao
        self.lista = [self.nome, self.descricao]
        
        self.lista.append.listaT
     

    
    def excluir_tarefa():
        pass
    def listar_tarefas(self):
       for nome, descricao in self.lista ():
            print(f'Tarefas:{nome[0]}, Descricao: {descricao[1]}')    

