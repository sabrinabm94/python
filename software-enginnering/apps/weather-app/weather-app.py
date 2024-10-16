__author__ = "Sabrina"
# -*- coding: utf-8 -*-
import requests
import json
import time

wantLeave = "n"
API_KEY = "70048041a843054b2b98174e3afae944"


def exit_program():
    global wantLeave
    wantLeave = input("\nWant to leave? Enter 's' for yes or 'n' to continue: ")

    if wantLeave == "s":
        print("Exiting...")
        time.sleep(1)
    elif wantLeave == "n":
        print("Program restarted")
        time.sleep(1)


def main():
    global wantLeave
    while wantLeave == "n":
        city = input(
            "Enter the name of your city (lowercase and without special characters):\n"
        )
        try:
            if API_KEY and city:
                request = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
                )
                responseDictionary = request.json()

                # Verifica se a cidade foi encontrada
                if request.status_code == 200:
                    print("Information Found!")
                    search = input(
                        "Please enter 'full' to see everything or one of the terms: 'name', 'wind', 'coord', or 'main':\n"
                    )
                    if search == "full":
                        print("Name:", responseDictionary["name"])
                        print(
                            f"Wind: "
                            f"speed: {responseDictionary['wind']['speed']}, "
                            f"deg: {responseDictionary['wind']['deg']}"
                        )
                        print(
                            f"Coordinates: "
                            f"lon: {responseDictionary['coord']['lon']}, "
                            f"lat: {responseDictionary['coord']['lat']}"
                        )
                        print(
                            f"Weather: temperature min: {responseDictionary['main']['temp_min']}, "
                            f"temperature max: {responseDictionary['main']['temp_max']}, "
                            f"humidity: {responseDictionary['main']['humidity']}"
                        )
                    elif search in ["name", "wind", "coord", "main"]:
                        print(f"{search.capitalize()}: {responseDictionary[search]}")
                    else:
                        print("Sorry, the informed search term is invalid.")
                else:
                    print(
                        f"Error {request.status_code}: {responseDictionary.get('message', 'City not found.')}"
                    )
            else:
                print("Error: incomplete data")

            exit_program()

        except requests.exceptions.RequestException as e:
            print("Connection error:", e)
            exit_program()


if __name__ == "__main__":
    main()
