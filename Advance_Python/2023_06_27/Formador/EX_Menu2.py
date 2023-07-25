"""Pretende-se criar um programa que recorra a classes que permita a criação de um menu de opções
    1. Criar
    2. Inserir
    3. Alterar
    4. Suprimir
    5. Fim
    
    
    Areas
    1.Quadrado/Retangulo
    2.Triangulo
    3.Cincunferencia
    4.Trapezio
    5.Fim
"""
#import os
from os import system
from time import sleep
import math
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
        print("Areas de figuras geometricas")
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
            print("Se pretender a area do quadrado mantenha o valor dos lados iguais Lado1=Lado2")
            Lado1=float(input("Digite o valor do lado 1: "))
            Lado2=float(input("Digite o valor do lado 2: "))
            print(f"A área do quadrado/retangulo é = {Lado1*Lado2}")
        if opc==1:
            print(f"Procedimento para {lista[opc]}")
        if opc==2:
            Raio=float(input("Digite o valor do raio da circunferência: "))
            print(f"A área da circunferência é = {math.pi*math.pow(Raio,2)}")
        if opc==3:
            print(f"Procedimento para {lista[opc]}")
        sleep(6)
        return
            

if __name__=='__main__':
    lista=["Quadrado/Retangulo","Triangulo","Circunferencia","Trapezio","Fim"]
    while True:
        opc=menu(lista).lervalidar()
        if opc==len(lista):
            break
        else:
            Exop=executarop(opc,lista)