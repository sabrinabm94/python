__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import requests
import json
import time

#key = input('Digite sua key')
wantLeave = 'n'

def exit():
    wantLeave = 'n'
    time.sleep(2)
    wantLeave = input(print("\n Want to leave? enter 's' for yes or 'n' to continue"))

    if wantLeave == 's':
        print('exit...')
        time.sleep(1)
    else:
        if wantLeave == 'n':
            print('Program restarted')
            time.sleep(1)

            while wantLeave == 'n' and wantLeave != 's':
                key = '9213a83088707d804aaa325e91881e5c'
                city = input('Digite o nome da cidade (letras minísculas e sem acertos):\n')
                concatKey = '&appid='+ key
                concatVariables = city+concatKey
                try:
                    request = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+concatVariables)
                    #request = request.get('http://api.openweathermap.org/data/2.5/weather?q=joinville&appid=9213a83088707d804aaa325e91881e5c')
                    returDicionary = json.loads(request.text)
                    print('Information Found!')

                    search = input("Please enter with 'full' to see everting \n Or one of the terms for select search: 'name', 'wind', 'coor' ou 'main'.\n")
                    if search == 'full':
                        print('Name: ', returDicionary['name'])
                        #print('Country: ', returDicionary['country'])
                        print('Wind: ', returDicionary['wind'])
                        print('Coordinates: ', returDicionary['coord'])
                        print('Weather: ', returDicionary['main'])
                        exit()
                    else:
                        try:
                            if search == 'name' or 'wind' or 'coord' or 'main':
                                print(search, ' ',(returDicionary[search]))
                                exit()
                            except:
                                print('Sorry, the informed search term is invalid.')
                                exit()

                            except:
                                print('Connection error, try again')
                                exit()


