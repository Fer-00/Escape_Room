import json, os, pyxel, fase_01

class Itens():
	def __init__(self,**kwargs):
		if len(kwargs) != 0:
			for key,valor in kwargs.items():
				setattr(self,key,valor)
		else:
			try:
				with open('itens.json','r') as file:
					json_itens = json.load(file)
					self.itens = [Itens(**json_itens[item]) for item in json_itens.keys()]
			except ValueError as e:
				print("Erro: ",str(e))
	
	def __repr__(self):
		return f"<Item {self.__dict__}>"
	
	def __del__(self):
		pass

	def criaObjeto(self,nome,x,y):
		for item in self.itens:
			if nome == item.nome:
				item.xTela = x
				item.yTela = y
				pyxel.blt(item.xTela, item.yTela, 0,item.x,item.y,item.comprimento,item.altura,item.transparencia)
			else:
				pass


	def criaObjetoInventario(self,temp):
		for item in self.itens:
			if temp == item.nome:
				if item.nome == "chave_g":
					pyxel.blt(112, 115, 0,item.x,item.y,item.comprimento,item.altura,item.transparencia)
				elif item.nome == "ferramenta":
					pyxel.blt(112, 114, 0,item.x,item.y,item.comprimento,item.altura,item.transparencia)
				elif item.nome == "pe_cabra":
					pyxel.blt(112, 112, 0,item.x,item.y,item.comprimento,item.altura,item.transparencia)
			
			else:
				pass

	def clicado(self,x,y,selecionado):
		itemInventario = self.getItem2(selecionado)
		itemClicado = self.getItem(x,y,itemInventario)
		if (itemClicado == itemInventario) and itemClicado != 0:
			return True

	def getItem2(self,nome):
		for item in self.itens:
			if item.nome == nome:
				return item.valor	
	
	def getItem(self,x,y,item_selecionado):
		for item in self.itens:
			if (x >= item.xTela and x <= item.xTela + item.comprimento) and (y >= item.yTela and y <= item.yTela + item.altura) and item.valor == item_selecionado:
				return item.valor
			else:
				pass

	def delete(self,nome):
		for item in self.itens:
			if item.nome == nome:
				del item

	def getId(self,nome):
		for item in self.itens:
			if item.nome == nome:
				return item.id