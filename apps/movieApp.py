__author__ = 'Sabrina'
# -*- coding: utf-8 -*-
import requests
#request installer: pip install requests
#upgrade: pip install requests --upgrade
import json
#import json library

request = None
title = 'Game of Thrones'
#title = input("Please enter the name you want to search")
try:
    request = requests.get('http://www.omdbapi.com/?t=' + title)
    #return returRequest
except:
    print('Connection error')
    #return None
    exit()

    returDicionary = json.loads(request.text)

    search = input('Enter any of the following terms to search for: Title, Director, Genre, Actors, Year or full to see all')
    if search == 'full':
        print('Title', returDicionary['Title'])
        print('Year', returDicionary['Year'])
        print('Genre', returDicionary['Genre'])
        print('Director', returDicionary['Director'])
        print('Actors', returDicionary['Actors'])
    else:
        try:
            if search == 'Title' or 'Year' or 'Genre' or 'Actors':
                print(search, ' ',(returDicionary[search]))
            except:
                print('Sorry, the typed term was not found.')

