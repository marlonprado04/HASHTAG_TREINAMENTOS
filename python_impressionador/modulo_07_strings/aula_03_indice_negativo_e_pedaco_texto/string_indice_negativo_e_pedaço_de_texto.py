# -*- coding: utf-8 -*-
"""String Indice Negativo e Peda�o de Texto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-0xQfysuzoVE8Q5bDi4dFwNo-E7sNwi

Texto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
Para pegar um texto de tr�s para frente: texto[�ndice] -> onde �ndice � negativo
Para pegar o peda�o de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]
"""

email = 'lira@gmail.com'
nome = 'Jo�o Paulo Lira'

"""Exerc�cios para Fixa��o:
Basta completar os prints de forma correta
"""

print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + '?')
print('�ltimo Caractere ' + '?')
print('Servidor do email ' + '?')