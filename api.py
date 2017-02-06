__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import requests
import json
#importar a biblioteca json para tranformar seu conteúdo num dicionário.;

request = None;
title = 'Game of Thrones';
#title = input("Digite corretamente o nome que deseja buscar)
#instanciar a variável antes do try.
try:
    request = requests.get('http://www.omdbapi.com/?t=' + title)
    #return returRequest
except:
    print('Erro de conexão.')
    #return None
    exit()

returRequest = print(request.text)
returDicionary = json.loads(returRequest)

search = input('Digite um dos seguintes termos para buscar: Title, Director, Genre, Actors, Year ou full para ver tudo')
if search == 'full':
    print('Título', returDicionary['Title'])
    print('Ano', returDicionary['Year'])
    print('Gênero', returDicionary['Genre'])
    print('Diretor', returDicionary['Director'])
    print('Atores', returDicionary['Actors'])
else:
    print(returDicionary(search))
