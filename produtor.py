# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:43:27 2022

@author: Gabriel Sampaio de Oliveira
"""

import socket
import pickle
import time
import numpy as np

# Abrindo e lendo todo o arquivo ratings.dat dividindo a string em uma lista onde cada linha é um item
lines = open("ratings.dat").read().splitlines()

# Criando host e porta para conexão com o produtor
host = '127.0.0.1'
port = 44444

s = socket.socket()
s.bind((host, port))

s.listen(1)
print("Aguardando consumidor...")

(connect, a) = s.accept()
print("Consumidor conectado!")

# Enviando dados para o consumidor
# Escolhendo 100 linhas aleatórias e adicionando quebra de linha
while True:
    
    content = ''
    lines = np.random.choice(lines, 100)
    
    for line in lines:
        if(content == ''):content = line
        else: content += '\n' + line
        
    # Serializando o pickle
    data = pickle.dumps(content)
    connect.send(data)
    
    print("\n100 filmes aleatórios enviados!")
    
    # Espera 25s para enviar novas linhas
    time.sleep(25)