#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import end, home, fase_01

class Engine:
	def __init__(self):
		self.final = end.End(True)
		self.inicial = home.Home()
		self.fases = fase_01.Fase01()
		self.x = 0 #controla as trocas do inventário
		
		global id #Controla os frames/fases
		id = 1 #Controla os frames/fases
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		px.run(self.draw,self.update)

	def update(self):
		global id #Controla os frames/fases
		self.mouse_x = px.mouse_x
		self.mouse_y = px.mouse_y

		if self.fases.lenInventario() > 0: #Verifica se o inventário é maior que 0 para começar a mostrar ele
			self.fases.ctlInventario(self.x) #Usa o self.x para saber em qual item do inventário ele está

		if px.btnp(px.KEY_Q): #Usa a tecla q para trocar entre o inventário
			if self.fases.lenInventario() > 0: 
				if self.x == self.fases.lenInventario() - 1: # se self.x tiver o mesmo do inventário - 1, correspondendo ao último índice
					self.x = 0 #ele volta o self.x para 0
				else:
					self.x += 1 #Se não vai para o próximo item
				
		elif id == 1 and (px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN)): #Controla os frames/fases 
			id = 0 #Abre a fase 1
		elif id == 1 and (self.mouse_x <= 79 and self.mouse_x >= 49) and (self.mouse_y <= 71 and self.mouse_y >= 57) and px.btn(px.MOUSE_BUTTON_LEFT):
			id = 0 #Abre a fase 1
		else:
			pass

		if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g": #Verifica se houve um clique do mouse com o item certo selecionado no inventário
			if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")): #Verifica se a área clicada é a correspondente do objeto selecionado no inventário
				print("INTERAGIU")
			else:
				print("Não INTERAGIU")

		elif px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 39 and self.mouse_x >= 26) and (self.mouse_y <= 109 and self.mouse_y >= 103)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome
		else:
			pass

	
	def draw(self):
		global id #Controla os frames/fases
		if id == 1: #Seta a Tela Inicial
			self.inicial.rodarInicial()
		elif id == 0: #Controla os frames/fases
			self.fases.fase01() #Seta a Fase 1
			#if len(self.fases.venceu()) > 0:
			#	self.final.tela_final(self.fases.venceu())
		else:
			pass

		
		px.mouse(True)

Engine()