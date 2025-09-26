#Tela de Fim/Conclusão

import pyxel as px
import frames.py

scores = "tempos.txt" #para mostrar os melhores tempos

class End:
	def __init__(self):
		frame = Frames()
		self.tempo_final = frame.cronometro()
		self.tempos = []
		self.top5 = []
		self.top5()
		px.run(self.update,self.draw)
		
	def update(self):
		if px.btnp(px.KEY_Q):
			px.quit()

	def draw(self):
		px.cls(0)
		px.text(60,20,f"Tempo atual:{tempo_final}s",7)
		px.text(60,20,f"RANKING:",10)
		for i,j in enumerate(self.top5[:5]):
			px.text(60,20+i*10,f"{i+1}: {j} s",11)
		px.text(60,20,f"Precione Q para sair",6)

	def top5(self):
		if not os.path.exists(scores):
			self top5 = []
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