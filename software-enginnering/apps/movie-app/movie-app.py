__author__ = "Sabrina"
# -*- coding: utf-8 -*-
import requests
import json

title = "Game of Thrones"
key = "634a203c"

try:
    if title and key:
        request = requests.get(f"https://www.omdbapi.com/?t={title}&apikey={key}")
        responseDictionary = json.loads(request.text)

        if request.status_code == 200 and "Title" in responseDictionary:
            search = input(
                "Enter Title, Director, Genre, Actors, Year, or full to see all: "
            )
            if search == "full":
                print("Title:", responseDictionary["Title"])
                print("Year:", responseDictionary["Year"])
                print("Genre:", responseDictionary["Genre"])
                print("Director:", responseDictionary["Director"])
                print("Actors:", responseDictionary["Actors"])
            elif search in responseDictionary:
                print(f"{search}: {responseDictionary[search]}")
            else:
                print("Sorry, the typed term was not found.")
        else:
            print(f"Error: {responseDictionary.get('Error', 'Movie not found')}")
    else:
        print("Error: incomplete data")

except requests.exceptions.RequestException as e:
    print("Connection error:", e)
