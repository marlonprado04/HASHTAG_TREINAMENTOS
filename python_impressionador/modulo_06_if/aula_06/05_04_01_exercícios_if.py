# -*- coding: utf-8 -*-
"""05.04.01 Exerc�cios if.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JjcqciIJtjIfCFgoiGJIHEAwsVXTME1Z

# Exerc�cios com if

## 1. C�lculo de B�nus

- Crie um programa que calcule e d� um print no b�nus que os funcion�rios devem receber segundo a regra:

A meta � 1000 vendas.<br> 
Se o valor de vendas for maior ou igual a meta, o valor do b�nus do funcion�rio � 10% do valor de vendas.<br>
Caso contr�rio o valor de b�nus do funcion�rio � 0.<br>
Print o b�nus dos 3 funcion�rios
"""

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#crie seu c�digo aqui

"""Resposta:
O funcion�rio 1 ganhou 100 de b�nus
O funcion�rio 2 ganhou 0 de b�nus
O funcion�rio 3 ganhou 270 de b�nus

## 2. C�lculo de b�nus com uma nova regra

- Agora, crie um novo c�digo que calcule e d� um print no b�nus dos funcion�rios novamente. Por�m h� uma nova regra nesse 2� caso:

A meta � 1000 vendas<br>
Agora, os funcion�rios que venderem muito acima da meta ganham mais b�nus do que os outros. Ent�o o b�nus � definido da seguinte forma:<br>

- Se vendas funcion�rio for maior ou igual a 2000, ent�o o b�nus � de 15% sobre o valor de vendas
- Se vendas funcion�rio for menor do que 2000 e maior ou igual a 1000, ent�o o b�nus � de 10% sobre o valor de vendas
- Se vendas funcion�rio for menos do que 1000 ent�o o b�nus do funcion�rio � de 0.

Use as mesmas vari�veis de vendas_funcion�rios
"""

#crie seu c�digo aqui
#obs: h� 2 formas de fazer, com if dentro de if ou ent�o com if e elif. Escolha a que voc� preferir

"""Resposta:
O funcion�rio 1 ganhou 100 de b�nus
O funcion�rio 2 ganhou 0 de b�nus
O funcion�rio 3 ganhou 405 de b�nus
"""