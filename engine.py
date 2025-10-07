#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import end, home, fase_01

class Engine:
	def __init__(self):
		self.final = end.End(True)
		self.inicial = home.Home()
		self.fases = fase_01.Fase01()
		self.x = 0 #controla as trocas do inventário

		self.obstaculos01 = ["cadeado"]
		self.obstaculos02 = ["cadeado","tabua_esq"]

		self.x_cadeado01 = 72
		self.y_cadeado01 = 96

		self.x_cadeado02 = 72
		self.y_cadeado02 = 96

		self.x_tabua_esq02 = 50
		self.y_tabua_esq02 = 100
		
		
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

		if id == 0:
				
			if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g": #Verifica se houve um clique do mouse com o item certo selecionado no inventário
				if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado' in self.obstaculos01): #Verifica se a área clicada é a correspondente do objeto selecionado no inventário
					print("removendo cadeado")
					print(self.obstaculos01)
					self.obstaculos01.remove("cadeado")
					self.fases.delete("cadeado") 
					#self.x_cadeado01 = 1000
					#self.y_cadeado01 = 1000
				elif (self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado' not in self.obstaculos01):
					print("passando para próxima fase")
					self.fases.removeItem("chave_g")
					id = 2
					
				else:
					print("Não INTERAGIU")

			elif px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 39 and self.mouse_x >= 26) and (self.mouse_y <= 109 and self.mouse_y >= 103)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome
			
			
		if id == 2:
				
			if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g": #Verifica se houve um clique do mouse com o item certo selecionado no inventário
				if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado' in self.obstaculos02): #Verifica se a área clicada é a correspondente do objeto selecionado no inventário
					print("removendo cadeado")
					print(self.obstaculos02)
					self.obstaculos02.remove("cadeado")
					self.x_cadeado02 = 1000
					self.y_cadeado02 = 1000
				if(self.fases.clique(self.mouse_x,self.mouse_y,"ferramenta")) and ('tabua_esq' in self.obstaculos02):
					print("removendo tabua")
					print(self.obstaculos02)
					self.obstaculos02.remove("tabua_esq")
					self.x_tabua_esq02 = 1000
					self.y_tabua_esq02 = 1000
				
				if ((self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) or (self.fases.clique(self.mouse_x,self.mouse_y,"ferramenta"))) and ('cadeado' not in self.obstaculos01) and ('tabua_esq' not in self.obstaculos02):
					id == 3
				else:
					print("Não INTERAGIU")

			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 21 and self.mouse_x >= 8) and (self.mouse_y <= 63 and self.mouse_y >= 57)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome
				print("pegou chave")
			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 103 and self.mouse_x >= 92) and (self.mouse_y <= 83 and self.mouse_y >= 72)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("ferramenta") #Adiona item ao invetário pelo nome
				print("pegou ferramenta")
		"""if self.obstaculos01 == [] and id == 0: #Verifica se os obstáculos da fase 1 foram todos removidos
			id = 2	#começa a fase 2
			pass
		elif self.obstaculos02 == [] and id == 2: #Verifica se os obstáculos da fase 2 foram todos removidos
			id = 3	#começa a fase 3	
			pass"""






		

	def draw(self):
		global id #Controla os frames/fases
		if id == 1: #Seta a Tela Inicial
			self.inicial.rodarInicial()
		elif id == 0: #Controla os frames/fases
			self.fases.fase01() #Seta a Fase 1
			#px.blt(self.x_cadeado01, self.y_cadeado01, 0,85,116,6,8,15)
			
			#if len(self.fases.venceu()) > 0:
			#	self.final.tela_final(self.fases.venceu())
		elif id == 2:
			self.fases.fase02() #Seta a Fase 2
			px.blt(self.x_cadeado02, self.y_cadeado02, 0,85,116,6,8,15)
			px.blt(self.x_tabua_esq02, self.y_tabua_esq02, 0,96,96,32,24,15)

		elif id == 3:
			self.fases.fase03() #Seta a Fase 3
		else:
			pass

		
		px.mouse(True)

Engine()