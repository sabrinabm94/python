__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import requests
import json
import time

#key = input('Digite sua key')
sair = 'n'

def questionarSair():
    sair = 'n'
    time.sleep(2)
    sair = input(print("\nDeseja sair?, digite 's' para sim ou 'n' para continuar"))

    if sair == 's':
        print('Programa encerrado')
        time.sleep(1)
        #colocar um die aqui

    else:
        if sair == 'n':
            print('Programa reiniciado')
            time.sleep(1)

while sair == 'n' and sair != 's':
    key = '9213a83088707d804aaa325e91881e5c'
    city = input('Digite o nome da cidade (letras minísculas e sem acertos):\n')
    concatKey = '&appid='+ key
    concatVariables = city+concatKey
    try:
        request = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+concatVariables)
        #request = request.get('http://api.openweathermap.org/data/2.5/weather?q=joinville&appid=9213a83088707d804aaa325e91881e5c')
        returDicionary = json.loads(request.text)
        print('Informações encontradas !')

        search = input("Digite um dos termos ('name', 'wind', 'coor' ou 'main') para resultados específicos, ou 'full' para ver tudo.\n")
        if search == 'full':
            print('Nome:', returDicionary['name'])
            #print('País:', returDicionary['country'])
            print('Vento:', returDicionary['wind'])
            print('Coordenadas:', returDicionary['coord'])
            print('Clima:', returDicionary['main'])
            questionarSair()

        else:
            try:
                if search == 'name' or 'wind' or 'coord' or 'main':
                    print(search, ' ',(returDicionary[search]))
                    questionarSair()
            except:
                print('Desculpe, o termo não encontrado.')
                questionarSair()

    except:
        print('Erro de conexão.')
        #return None
        exit()


