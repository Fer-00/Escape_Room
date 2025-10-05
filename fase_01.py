import pyxel as px #controla a fase em si
import itens, time, end

class Fase01:
	def __init__(self):
		self.item = itens.Itens()
		self.fim = end.End()
		self.start_time = time.time()
		self.inventario = []
		self.venceu = False

	def transicao(self):
		pass
			
	def setarFases(self):
		pass

	def timer(self):
		elapsed = int(time.time() - self.start_time)
		minutos = elapsed // 60
		segundos = elapsed % 60
		self.tempo = str(self.minutos) + ":" + str(self.segundos)
		if minutos == 5:
			self.perdeu()
		px.text(31, 23, f"{minutos:02}:{segundos:02}", 7)  # Mostra o tempo no canto

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

	def venceu(self,tempo):
		if self.venceu == True:
			with open("tempos.txt","a") as t:
				t.write(f"\n{self.tempo}")
			return tempo
		else:
			return ""

	def perdeu(self):
		self.fim.tela_final()

	def addItem(self, nome): # return id
		self.inventario.addend(self.item.getId(nome))

	def testaItem(self,item): #chamada toda vez que o item é utilizado para checar se ainda há usos
		if (self.item.getUsos(item) > 0):
			pass
		else:
			self.item.delete(item)

	def lenInventario(self):
		return len(self.inventario)		

	def ctlInventario(self, id = 0):
		self.item.criaObjeto("Hud",100,100)
		if id in self.inventario:
			self.item.criaObjetoInventario(id)