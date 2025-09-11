#responsável por controlar os frames do jogo, as trocas entre eles e o que vai aparecer sobre todos eles

import pyxel as px

class Frames:
	def __init__(self):
		self.inventario = []
		self.item = [] #item,img,usos
		self.corFundo = 2
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')

	def addItem(self):
		pass

	def removeItem(self):
		pass

	def getItem(self):
		pass

	def ctlInventario(self):
		pass

	def telaInicial(self):
		px.cls(self.corFundo)	

	def jogo_start(self):
		self.corFundo = 0
		px.cls(self.corFundo)	
		px.bltm(0,0,1,0,0,128,128,0,0,1.0)

	def telaFinal(self):
		pass