#Tela de Fim/Conclusão
import pyxel as px
import os

scores = "tempos.txt" #para mostrar os melhores tempos

class End:
	def __init__(self, ganhou = False):
		self.tempos = []
		self.populaTop5()

	def tela_final(self, tempo_final = "Você Perdeu!!"):
		px.cls(0)
		px.text(40,10,"FIM DE JOGO",8)
		px.text(30,20,f"Tempo atual:{tempo_final}s",7)
		px.text(30,30,f"RANKING:",10)
		for i,j in enumerate(self.tempos[:5]):
			minutos = j//60
			segundos = j % 60
			px.text(60,40+i*10,f"{i+1}: {minutos}:{segundos} s",11)

#		px.text(30,20,"OBRIGADO POR JOGAR!",7)
		px.text(30,90,"Por: Adriane e Victtor",7)

		px.text(20,110,"Precione ESC para sair",6)

	def populaTop5(self):
		if not os.path.exists(scores):
			print("if not os.path")
			self.top5 = []
			return
		with open(scores,"r") as f:
			linhas = f.readlines()
		for linha in linhas:
			try:
				aux = linha.split(",")
				tempo = int(aux[0].strip())
				self.tempos.append(tempo)
			except Exception as e:
				print(str(e))
		self.tempos = sorted(self.tempos)