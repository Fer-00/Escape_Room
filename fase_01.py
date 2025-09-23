import pyxel as px #controla a fase em si
import frames.py

class Fase01:
	def __init__(self):
		frame = Frames()

	def transicao(self,atual,prox):
		pass

	def cronometro(self):
		global tempo
		tempo = px.frame_count // 30
		if tempo == 300:
			px.text(50,50,"VOCÊ PERDEU",px.COLOR_WHITE)

##	def timer(self):
	def venceu(self):
		with open("tempos.txt","a") as t:
			t.write(f"\n{tempo}")
			
	def getUP(self): #teto
		pass

	def getFront(self): #parede da porta
		pass

	def getRight(self): # parede da direita
		pass

	def getLeft(self): # parede da esquerda
		pass

	def getDown(self): # piso
		pass

	def getBotton(self): # parede do fundo
		pass

	def update(self):
		pass

	def draw(self):
		pass