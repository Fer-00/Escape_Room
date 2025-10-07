import pyxel as px #controla a fase em si
import itens, time, end

class Fase01:
	def __init__(self):
		self.item = itens.Itens()
		self.fim = end.End()
		self.start_time = time.time()
		self.inventario = []
		self.obstaculos = []
		self.itensTela = []
		self.venceu = False
		self.item_inventario = -3

	def transicao(self):
		pass
			
	def setarFases(self):
		pass

	def ctlInventario(self, temp):
		self.item.criaObjeto("HUD02",110,110)
		if temp < self.lenInventario():
			self.item.criaObjetoInventario(self.inventario[temp])
			self.item_inventario = self.inventario[temp]
		else:
			pass

	def timer(self,x,y):
		elapsed = int(time.time() - self.start_time)
		minutos = elapsed // 60
		segundos = elapsed % 60
		self.tempo = str(minutos) + ":" + str(segundos)
		if minutos == 5:
			self.perdeu()
		px.text(x, y, f"{minutos:02}:{segundos:02}", 7)  # Mostra o tempo no canto

	def fase01(self):
		px.load('1.pyxres')
		px.cls(0)
		px.bltm(0,0,1,128,0,128,128,0,0,1.0)
		self.item.criaObjeto("porta",50,64)
		self.item.criaObjeto("placa",50,50)
		self.item.criaObjeto("mesinha_madeira",20,110)
		self.item.criaObjeto("chave_g",26,103)
		if "cadeado" in self.getObstaculos(): #por último para garantir que não seja sobreposto
			self.item.criaObjeto("cadeado",72,96)	#se cadeado esta na lista de obstaculos, printa ele, se não, não

	def fase02(self):
		px.load('1.pyxres')
		px.cls(0)
		px.bltm(0,0,1,128,0,128,128,0,0,1.0)
		

		self.item.criaObjeto("porta",50,64)
		self.item.criaObjeto("placa",50,50)

		self.item.criaObjeto("quadro_02",100,50)

		self.item.criaObjeto("armario_02_madeira",0,104)
		self.item.criaObjeto("relogio",3,91)
		self.item.criaObjeto("armario_02_madeira",0,64)
		self.item.criaObjeto("aquario",88,98)

		self.item.criaObjeto("quadro_vazio",90,70)
		self.item.criaObjeto("ferramenta",92,72)
		self.item.criaObjeto("chave_g",8,57)

		self.item.criaObjeto("HUD02",110,110)

		self.item.criaObjeto("mesinha_madeira",84,110)
		
		if "cadeado1" in self.getObstaculos(): #cadeado1 para não dar conflito
			self.item.criaObjeto("cadeado",72,96) #se estiver na lista de obstaculos, printa, senão não
		if "tabua_esq" in self.getObstaculos():
			self.item.criaObjeto("tabua_esq",50,100)
		


	def fase03(self):
		px.load('1.pyxres')
		px.cls(0)
		px.bltm(0,0,1,128,0,128,128,0,0,1.0)

		self.item.criaObjeto("porta",50,64)
		self.item.criaObjeto("placa",50,50)
	
		self.item.criaObjeto("bau",0,96)
		self.item.criaObjeto("cofre_madeira",84,96)
		self.item.criaObjeto("abajur_claro",87,82)	

		self.item.criaObjeto("quadro_01",00,76)
		self.item.criaObjeto("quadro_02",20,76)

		self.item.criaObjeto("armario_01_madeira",0,50)
		self.item.criaObjeto("armario_02_madeira",84,50)
		self.item.criaObjeto("relogio",88,37)	

		self.item.criaObjeto("HUD02",110,110)

		for i in range (10): #faz um monte de tubo no topo da tela
			self.item.criaObjeto("tubulacao",i*16,20)
		
		self.item.criaObjeto("pe_cabra",70,13)

		if "cadeado2" in self.getObstaculos(): #cadeado1 para não dar conflito
			self.item.criaObjeto("cadeado",72,96) #se estiver na lista de obstaculos, printa, senão não
		if "tabua_esq1" in self.getObstaculos():
			self.item.criaObjeto("tabua_esq",50,100)
		if "tabua_dir" in self.getObstaculos():
			self.item.criaObjeto("tabua_dir",0,100)
		else:
			self.item.criaObjeto("bau_aberto",0,96)
			self.item.criaObjeto("chave_g",10,100)

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

	def addItem(self, nome): # adiciona item ao inventário
		if nome not in self.inventario:
			self.inventario.append(nome)

	def removeItem(self,nome): # remove item do inventário
		if nome in self.inventario:
			self.inventario.remove(nome)
	

	def testaItem(self,item): #chamada toda vez que o item é utilizado para checar se ainda há usos
		if (self.item.getUsos(item) > 0):
			pass
		else:
			self.item.delete(item)

	def lenInventario(self):
		return len(self.inventario)	

	def clique(self,x,y,item_selecionado):
			if(self.item.clicado(x,y,item_selecionado)):
				return True
			else:
				return False

	def getItemSelecionado(self):
		return self.item_inventario

	def getObstaculos(self): #retorna a lista de obstaculos
		return self.obstaculos
	
	def removeObstaculo(self,obstaculo): #remove obstaculo da lista
		if obstaculo in self.obstaculos:
			self.obstaculos.remove(obstaculo)
		else:
			pass

	def addObstaculo(self,obstaculo): #adiciona obstaculo a lista de controle
		if obstaculo not in self.obstaculos:
			self.obstaculos.append(obstaculo)
		else:
			pass