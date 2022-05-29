# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:43:27 2022

@author: Gabriel Sampaio de Oliveira
"""

import os
import sys
os.path.dirname(sys.executable)

import socket
import pickle

# O pacote findspark adiciona o PySpark ao sys.path em tempo de execução. 
import findspark

# Inicializar o PySpark com o findspark
findspark.init()

# Uma SparkSession pode ser usada para criar DataFrame, 
# registrar DataFrame como tabelas, executar SQL sobre tabelas, tabelas de cache e ler arquivos de parquet.
from pyspark.sql import SparkSession

# Buffer de 8mb
BUFFER = 8192

# Instanciando seção de faísca
spark = SparkSession.builder.getOrCreate()

# Abrindo o arquivo movies.dat e armazenando no dicionário o nome dos filmes
# A chave é o ID do filme e o valor é o nome
def filmes(arquivo):
    
    nomes_filmes = {}
    
    with open(arquivo, encoding= 'ISO-8859-1') as a:
        
        for line in a:
            index = line.split('::')
            key = int(index[0])
            nomes_filmes[key] = index[1]
            
    return nomes_filmes

nomes_filmes = filmes('movies.dat')

s = socket.socket()
# Conectando o socket com o producer
s.connect(('127.0.0.1', 44444))

data = s.recv(BUFFER)

# Recebendo as avaliações
while data:
    
    # Organizando os dados recebidos para utilizar métodos spark
    recebidos = pickle.loads(data)
    lista = recebidos.split('\n')
    mapred = spark.sparkContext.parallelize(lista)
    
    # Criando lista chave-valor (movieID: [rating, 1])
    ratings = mapred.map(lambda x: (int(x.split('::')[1]), [float(x.split('::')[2]), 1]))
    
    # Somando os pares com a mesma key para saber o total de avaliações e quantas vezes o filme foi avaliado
    ratingTotal = ratings.reduceByKey(lambda x, y: [x[0] + y[0], x[1] + y[1]])
    
    # Tirando a média das avaliações total
    ratingMedia = ratingTotal.mapValues(lambda x: x[0] / x[1])
    
    # Lista com ID do filme e sua avaliação média
    IDmedia = ratingMedia.map(lambda kv: (kv[1], kv[0]))
    
    # Organizando em ordem decrescente da avaliação média
    ordemDec = IDmedia.sortByKey(False)
    
    # 10 primeiros filmes
    final = ordemDec.take(10)
    
    # Exibindo resultado final dos 10 melhores filmes entre os que foram geraldos
    for result in final:
        print(nomes_filmes[result[1]],",", round(result[0], 2))

    data = s.recv(BUFFER)