import pyxel as px #controla a fase em si
import frames.py

class Fase01:
	def __init__(self):
		frame = Frames()
		lista_frames = []
		clicaveis = [] #coordenadas de objetos fixos clicaveis e seus id (bau, relogio, porta)

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
		return lista_frames[index + aux]

	def fase01(self):
		pass

	def fase02(self):
		pass

	def fase03(self):
		pass

	def fase04(self):
		pass

	def update(self):
		pass

	def draw(self):
		pass