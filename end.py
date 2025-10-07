#Tela de Fim/Conclusão
import pyxel as px
import os

scores = "tempos.txt" #para mostrar os melhores tempos

class End:
	def __init__(self, ganhou = False):
		#self.tempo_final = self.frame.cronometro()
		self.tempos = []
		self.top5 = []
		self.populaTop5()

	def tela_final(self, tempo_final = "Você Perdeu!!"):
		px.cls(0)
		px.text(40,10,"FIM DE JOGO",8)
	#	px.text(30,20,f"Tempo atual:{tempo_final}s",7)
	#	px.text(30,30,f"RANKING:",10)
	#	for i,j in enumerate(self.top5[:5]):
	#		px.text(60,20+i*10,f"{i+1}: {j} s",11)
	#	px.text(30,40,f"Precione ESC para sair",6)

		px.text(30,20,"OBRIGADO POR JOGAR!",7)
		px.text(40,40,"Feito por:",7)
		px.text(30,50,"Adriane e Victtor",7)

		px.text(20,100,"Precione ESC para sair",6)
	def populaTop5(self):
		if not os.path.exists(scores):
			self.top5 = []
			return
		with open(scores,"r") as f:
			linhas = f.readlines()
		for linha in linhas:
			try:
				tempo = int(linha.strip())
				self.tempos.append(tempo)
			except ValueError:
				pass
		self.tempos = sorted(self.tempos)