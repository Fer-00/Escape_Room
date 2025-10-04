import json, os, pyxel

class Itens(object):
	def __init__(self,**kwargs):
#		print("Construtor")
#		if isinstance(kwargs, dict):
		if len(kwargs) != 0:
#			print("if construtor")
			for key,valor in kwargs.items():
#				print("seta")
				setattr(self,key,valor)
		else:
			try:
#				print("Abertura do Arquivo")
				with open('itens.json','r') as file:
					json_itens = json.load(file)
					self.itens = [Itens(**json_itens[item]) for item in json_itens.keys()]
					print(self.itens)
					for item in self.itens:
						print(item.nome,"-",item.comprimento,"-",item.altura)
			except ValueError as e:
				print("Erro: ",str(e))
	
	def __repr__(self):
		return f"<Item {self.__dict__}>"
	
	def __del__(self):
		pass

	def criaObjeto(self,nome,x,y):
#		if nome not in self.itens:
#			raise ValueError(f"Item {nome} não existe")
#		else:
		for item in self.itens:
#			print(item.nome)
			if nome == item.nome:
				pyxel.blt(x, y, 0,item.x,item.y,item.comprimento,item.altura,item.transparencia) #checar esse comando
			else:
				pass