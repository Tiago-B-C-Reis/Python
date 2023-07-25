"""Pretende-se criar um programa que recorra a classes que permita a criação de um menu de opções
    1. Criar
    2. Inserir
    3. Alterar
    4. Suprimir
    5. Fim
"""
#import os
from os import system
from time import sleep
#import time
class menu():
    opcoes=[]
    def __init__(self,lista):
        self.opcoes=lista
    
    def limparecran(self):
        #os.system("cls")
        system("cls")
        return
    
    def afixar(self):
        self.limparecran()
        print("Registo de dados")
        num=1
        for i in self.opcoes:
            print(f'{num}.{i}')
            num+=1
    
    def lervalidar(self):
        while True:
            self.afixar()
            op=int(input("Digite 1,2,3,4 ou 5: "))
            if op<1 or op>5:
                print("Opção Invalida!!!")
                sleep(2)
                continue
            else:
                break
        return op

class executarop():
    def __init__ (self,opc,lista):
        opc-=1
        if opc==0:
            print(f"Procedimento para {lista[opc]}")
        if opc==1:
            print(f"Procedimento para {lista[opc]}")
        if opc==2:
            print(f"Procedimento para {lista[opc]}")
        if opc==3:
            print(f"Procedimento para {lista[opc]}")
        sleep(2)
        return
            

if __name__=='__main__':
    lista=["Criar","Inserir","Alterar","Suprimir","Fim"]
    while True:
        opc=menu(lista).lervalidar()
        if opc==len(lista):
            break
        else:
            Exop=executarop(opc,lista)