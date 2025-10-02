import json, os

class Itens():
	def __init__(self):
		try:
			with open('itens.json','r') as file:
				json_itens = json.load(file)
				print(json_itens)
		except ValueError as e:
			print("Erro: ",str(e))
#	def objeto(self):
Itens()