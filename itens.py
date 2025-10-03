import json, os, pyxel

class Itens(object):
	def __init__(self,**kwargs):
		for key,valor in kwargs.items():
			setattr(self,key,valor)
	
	def __repr__(self):
		return f"<Item {self.__dict__}>"
	
	def __del__(self):
		return True

	def criaObjeto(self,nome,x,y):
		if nome not in self.itens:
			raise ValueError(f"Item {nome} não existe")
		else:
			pyxel.blt(x, y, 0,54,116,5,10,0) #checar esse comando


try:
	with open('itens.json','r') as file:
		json_itens = json.load(file)
		itens = [Itens(**json_itens[item]) for item in json_itens]
		for item in itens:
			print(item.nome,"-",item.comprimento,"-",item.altura)
except ValueError as e:
	print("Erro: ",str(e))