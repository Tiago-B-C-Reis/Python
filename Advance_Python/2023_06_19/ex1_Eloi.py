##DUAL-Curso Python####
## Aula nº6          ##
##Eloi Leitão 2023 ####

import math
class temperatura():

        #contrutor

    #atributos
    def __init__(self, C1,F1):
        
        self.__celsius = C1
        self.__fahrenheit = F1


    #getters
    def getcelsius(self):
        return f"{self.__celsius:2.2f}"
    def getfahrenheit(self):
        return f"{self.__fahrenheit:2.2f}"
    
    #setters
    def setcelsius(self, C1):
        self.__celsius = C1
        self.__fahrenheit=math.floor((self.__celsius*1.8+32))
    def setfahrenheit(self, F1):
        self.__fahrenheit = F1
        self.__celsius=math.floor(((self.__fahrenheit-32)/1.8))
    #metodos
    def convertFahrenheit(self):
         return f"{math.floor((self.__celsius*1.8+32)):2.2f}"
    
    def convertcelsius(self):
         return f"{math.floor((self.__fahrenheit*1.8+32)):2.2f}"

    def getdadaC(self):
        self.setcelsius(float(input("Qual o Valor em Celsius? ")))
    def getdadaF(self):
        self.setfahrenheit(float(input("Qual o Valor em Fahrenheit? ")))

if __name__=="__main__":

    e=temperatura(0,0)
   
    e.getdadaC()
    print("Valor em Celsius " + e.getcelsius())
    print("Valor em Fahrenheit " + e.getfahrenheit())

#### em Fahrenheit
    print("Agora com entrada em Fahrenheit")

    e.getdadaF()
    print("Valor em Celsius " + e.getcelsius())
    print("Valor em Fahrenheit " + e.getfahrenheit())

 