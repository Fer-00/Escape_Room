import pyxel as px #controla a fase em si
import frames

class Fase01:
	def __init__(self):
		self.frame = frames.Frames()
		self.lista_frames = []
		self.clicaveis = [] #coordenadas de objetos fixos clicaveis e seus id (bau, relogio, porta)

	def transicao(self,atual,prox):
		if prox > atual:
			return -1
		elif prox > atual:
			return 1
		else:
			return 0
			
	def setarFrames(self,aqui,la):
		aux = transicao(aqui,la)
		#comando para recuperar indice do aqui
		return self.lista_frames[index + aux]

	def jogo_start(self):
		pass

	def fase01(self):
		px.load('1.pyxres')
		self.corFundo = 0
		px.cls(self.corFundo)	
		px.bltm(0,0,1,0,0,128,128,0,0,1.0)

	def fase02(self):
		pass

	def fase03(self):
		pass

	def fase04(self):
		pass