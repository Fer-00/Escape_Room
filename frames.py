#responsável por controlar os frames do jogo, as trocas entre eles e o que vai aparecer sobre todos eles

import pyxel as px

class Frames:
	def __init__(self):
		global tempo
		self.lim = 300 #300 segundos = 5 minuntos o tempo que você tem para sair da sala
		self.inventario = []
		self.item = [] #item,usos
		self.corFundo = 2
		#px.mouse(visible=True)

	def cronometro(self):
		tempo = px.frame_count // 30
		if tempo == 300:
			tempo = 1000
		return tempo

	def timer(self,inicio,atual):
		self.regressivo = (atual - inicio)// 30 #30 fps
		self.sobra = self.lim - self.regressivo
		return self.sobra

	def venceu(self):
		with open("tempos.txt","a") as t:
			t.write(f"\n{tempo}")

	def addItem(self, obj, temp,x,y): #nome do objeto, numero setado previamente e listado na readme para facilitar a chamada de funções de plotagem de imagem no inventário
		self.item.extend((obj,1))
		if temp == 1:
			self.martelo(x,y)
		elif temp == 2:
			self.mapa(x,y)
		elif temp == 3:
			self.chave(x,y)
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

#métodos para contruir imagens com mais efiência e em telas diferentes
	
	def relogio(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)

	def mesa(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def martelo(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def quadro(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def mapa(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def bau(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def porta(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def tijolos(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		
	def escape(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)

	def carta(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
	def chave(self,x,y):
		px.load('1.pyxres')
		px.bltm(49,57,1,65,26,30,14)
		

'''	def telaInicial(self):
		px.cls(self.corFundo)

	def telaFinal(self):
		pass'''

def jogo_start(self):
		px.load('1.pyxres')
		self.corFundo = 0
		px.cls(self.corFundo)	
		px.bltm(0,0,1,0,0,128,128,0,0,1.0)