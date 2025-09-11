#responsável por controlar os frames do jogo, as trocas entre eles e o que vai aparecer sobre todos eles

import pyxel as px

class Frames:
	def __init__(self):
		self.inventario = []
		self.item = [] #item,img,usos
		self.imgs = []
		self.corFundo = 2
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		#px.mouse(visible=True)

	def addItem(self, obj, posImg): #nome do objeto, qual a imagem que corresponde a ele na lista de imagens
		self.item.extend((obj,img[posImg],1))

	def removeItem(self,item, uso):
		if (item[2] - uso) == 0:
			self.inventario.remove(item)		

	def getItem(self,item):
		self.inventario[item[1]] 
		#draw item no inventário


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