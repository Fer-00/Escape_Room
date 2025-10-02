#responsável por controlar os frames do jogo, as trocas entre eles e o que vai aparecer sobre todos eles

import pyxel as px
from objetos2 import *

class Frames:
	def __init__(self):
		self.lim = 300 #300 segundos = 5 minuntos o tempo que você tem para sair da sala
		self.inventario = []
		self.item = [] #item,usos
		self.corFundo = 2
		#px.mouse(visible=True)

	def venceu(self,tempo):
		with open("tempos.txt","a") as t:
			t.write(f"\n{tempo}")

	def addItem(self, obj, temp,x,y): #nome do objeto, numero setado previamente e listado na readme para facilitar a chamada de funções de plotagem de imagem no inventário
		self.item.extend((obj,1))
		if temp == 1:
			martelo(x,y)
		elif temp == 2:
			mapa(x,y)
		elif temp == 3:
			chave(x,y)
		else:
			pass
		#px.bltm(49,57,1,65,26,30,14)

	def testaItem(self,item): #chamada toda vez que o item é utilizado para checar se ainda há usos
		if (item[2] - 1) == 0:
			self.inventario.remove(item)		

	def getItem(self,item,x,y):
		self.inventario[item[1]] 
		#draw item no inventário
		px.rect(x-1,y-1,36,20,7) #se o item for selecionado

	def ctlInventario(self):
		if len(self.inventario) < 3 and len(self.inventario) >=0:
			return True
		elif len(self.inventario) == 3:
			return False
		else:
			pass
