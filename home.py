import pyxel as px
import itens

#Tela de inicio/Welcome

class Home:
	def __init__(self):
		pass

	def rodarInicial(self):
		self.corFundo = 4
		px.cls(self.corFundo)
		px.bltm(0,0,1,128,0,128,128,1,0,1.0)
		px.bltm(49,57,1,65,26,30,14)
