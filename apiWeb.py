__author__ = 'Sabrina'
# -*- coding: utf-8 -*-

import sys
import time
#instalar o request: -m pip install requests
import requests
#Beatiful soup: pip install bs4
import bs4
#get pegar informações
#post envia informações
#as informações do header não são sempre confiáveis, podendo ser alteradas.

siteUrl = input(print("The default site address is: http://putsreq.com/WQ976gYl6AYqIsv9v8VR /n Do you want to change? '1' for yes or '2' for no"))
if siteUrl == 1:
    site = input("Enter with the new address: ")
else:
    site = ("http://putsreq.com/WQ976gYl6AYqIsv9v8VR")

    def request(site):
        try:
            get = requests.get(site)
            post = requests.post(site)
            print("\n Order Information: ")
            print(type(get))
            print(get)
            print(get.status_code)
            getText = (get.text)
            option = int(input(print("\n Do you want to see the page source code ? '1' for yes or '2' for no.")))
            if option == 1:
                print(getText)
            except Exception as erro:
                print("\n Connection error: ", erro)

                request(site)



