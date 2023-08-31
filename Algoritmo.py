from Classes import *
import os

listaT=[]
sair = False
def main():
    lista1= Tarefas('1','Ir ao mercado', 'Indo no mercado')
        
    while sair == False:
            try:
                os.system("cls")
                print("---MENU---")
                print("01 - Adicionar na Lista")
                print("02 - Listar a Lista de Tarefas")
                print("03 - Excluir um elemento da lista")
                print("00 - SAIR")
                

                menu = int(input("Qual opção deseja?"))
                
                
                match menu:
                    case 1:
                        os.system("cls")
                        print("---Adicionando a lista---")
                        print("Informe o número da lista, depois o nome da tarefa e por ultimo sua descrição")
                        numero= input('')
                        nome= input('')     
                        descrição= input('')   

                        lista1.adicionar_tarefa(numero, nome, descrição)

                        os.system('pause')

                    case 2:
                        os.system("cls")
                        print("Lista de Tarefas")
                        lista1.listar_tarefas()
                        os.system("pause")
                    
                    case 3:
                          pass
            
            
            
            
            except Exception as erro:
                os.system('cls')
                print("Valor invalido")
                print(erro.__class__.__name__)
                os.system('pause')
                print("")