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

alteracaoSite = input(print("O endereço padrão do site é: http://putsreq.com/WQ976gYl6AYqIsv9v8VR, deseja alterar? 1 para sim, 2 para não"))
if alteracaoSite == 1:
    site = input("Digite novo endereço")
else:
    site = ("http://putsreq.com/WQ976gYl6AYqIsv9v8VR")

def requisicoesExemplo(site):
        try:
            requisicaoGet = requests.get(site)
            requisicaoPost = requests.post(site)
            print("\n Informações sobre a requisição:")
            print(type(requisicaoGet))#tipo
            print(requisicaoGet)#status
            print(requisicaoGet.status_code)#status
            codigoFonte = (requisicaoGet.text)
            opcao = int(input(print("\n Você deseja ver o  código fonte da página?, 1 para sim, 2 para não.")))
            if opcao == 1:
                print(codigoFonte)#mostrou o código fonte do site
        except Exception as erro:
            print("\n Requisição deu erro:", erro)

requisicoesExemplo(site)



