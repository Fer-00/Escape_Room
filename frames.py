#responsável por controlar os frames do jogo, as trocas entre eles e o que vai aparecer sobre todos eles

import pyxel as px

scores = "tempos.txt" #para mostrar os melhores tempos

class Frames:
	def __init__(self):
		self.inventario = []
		self.item = [] #item,usos
		self.corFundo = 2
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		#px.mouse(visible=True)

	def addItem(self, obj, posImg): #nome do objeto, qual a imagem que corresponde a ele na lista de imagens
		self.item.extend((obj,1))
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

'''	def telaInicial(self):
		px.cls(self.corFundo)

	def telaFinal(self):
		pass'''

'''	def jogo_start(self): #migrar para draw
		self.corFundo = 0
		px.cls(self.corFundo)	
		px.bltm(0,0,1,0,0,128,128,0,0,1.0)'''