#!/usr/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

robo = ChatBot("Estudo")

conversa = open("falas.txt","r")
conversaSalva = open("falas.txt","a")
data = conversa.read()
robo.set_trainer(ListTrainer)
robo.train(data)
conversaSalva.write(data)
while True:
    pergunta = input()
    resposta = robo.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print(resposta)
        conversaSalva.write(" ' " + pergunta + " ' " + ",")
        conversaSalva.write(" ' " + str(resposta) + " ' " + ",")
    else:
        print("Nao sei")
