#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import end, home, fase_01

class Engine:
	def __init__(self):
		self.final = end.End(True)
		self.inicial = home.Home()
		self.fases = fase_01.Fase01()
		self.x = 0 #controla as trocas do inventário

		self.x_timer = 6
		self.y_timer = 96
		
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
			self.fases.addObstaculo("cadeado")
		elif id == 1 and (self.mouse_x <= 79 and self.mouse_x >= 49) and (self.mouse_y <= 71 and self.mouse_y >= 57) and px.btn(px.MOUSE_BUTTON_LEFT):
			id = 0 #Abre a fase 1
			self.fases.addObstaculo("cadeado")
		else:
			pass

		if id == 0:
			if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g": #Verifica se houve um clique do mouse com o item certo selecionado no inventário
				if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado' in self.fases.getObstaculos()): #getObstacucos retorna toda a lista na fases
					self.fases.removeObstaculo("cadeado") #remove o obstaculo da lista de obstaculos no fases
				elif (self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado' not in self.fases.getObstaculos()): #getObstacucos retorna toda a lista na fases
					self.fases.removeItem("chave_g")
					self.fases.addObstaculo("cadeado1") #Adiciona os obstaculos da próxima fase / cadeado1 para não dar conflito
					self.fases.addObstaculo("tabua_esq") #Adiciona os obstaculos da próxima fase
					self.x = 0 #Zera a x por precaução
					id = 2
				else:
					pass

			elif px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 39 and self.mouse_x >= 26) and (self.mouse_y <= 109 and self.mouse_y >= 103)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome

			else:
				pass
						
		if id == 2:
			self.fases.timer(self.x_timer,self.y_timer) #Mostra o timer na tela
			
			if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g" and len(self.fases.getObstaculos()) != 0 : #Verifica se houve um clique do mouse com o item certo selecionado no inventário e se o invetário de obstacúlos não está vazio

				if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado1' in self.fases.getObstaculos()) and ('tabua_esq' not in self.fases.getObstaculos()): #Verifica se a área clicada é a correspondente do objeto selecionado no inventário
					#Objetos sobrepostos, clica em um some o outro
					#Solução: o cadeado só pode ser clicado depois que a tábua não está mais lá
					self.fases.removeObstaculo("cadeado1") #remove cadeado da lista de obstaculos, 

			elif px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "ferramenta" and len(self.fases.getObstaculos()) != 0:
				if(self.fases.clique(self.mouse_x,self.mouse_y,"ferramenta")) and ('tabua_esq' in self.fases.getObstaculos()):
					self.fases.removeObstaculo("tabua_esq")
			elif ((px.btnp(px.MOUSE_BUTTON_LEFT)) and (self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and len(self.fases.getObstaculos()) == 0):
				self.fases.removeItem("chave_g")
				self.fases.removeItem("ferramenta")
				self.fases.addObstaculo("cadeado2") #Adiciona os obstaculos da próxima fase / cadeado1 para não dar conflito
				self.fases.addObstaculo("tabua_esq1") #Adiciona os obstaculos da próxima fase
				self.fases.addObstaculo("tabua_dir") #Adiciona os obstaculos da próxima fase
				self.x = 0
				id = 3
			else:
				pass

			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 21 and self.mouse_x >= 8) and (self.mouse_y <= 63 and self.mouse_y >= 57)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome

			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 103 and self.mouse_x >= 92) and (self.mouse_y <= 83 and self.mouse_y >= 72)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("ferramenta") #Adiona item ao invetário pelo nome
		
		if id == 3:
			self.x_timer = 91
			self.y_timer = 42
			self.fases.timer(self.x_timer,self.y_timer) #Mostra o timer na tela

			if px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "chave_g" and len(self.fases.getObstaculos()) != 0 : #Verifica se houve um clique do mouse com o item certo selecionado no inventário e se o invetário de obstacúlos não está vazio

				if(self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and ('cadeado2' in self.fases.getObstaculos()) and ('tabua_esq1' not in self.fases.getObstaculos()): #Verifica se a área clicada é a correspondente do objeto selecionado no inventário
					self.fases.removeObstaculo("cadeado2") #remove cadeado da lista de obstaculos, 

			elif px.btnp(px.MOUSE_BUTTON_LEFT) and self.fases.getItemSelecionado() == "pe_cabra" and len(self.fases.getObstaculos()) != 0:
				if(self.fases.clique(self.mouse_x,self.mouse_y,"pe_cabra")) and ('tabua_esq1' in self.fases.getObstaculos()) and ('tabua_dir' in self.fases.getObstaculos()):
					self.fases.removeObstaculo("tabua_esq1")					

				elif(self.fases.clique(self.mouse_x,self.mouse_y,"pe_cabra")) and ('tabua_dir' in self.fases.getObstaculos()) and ('tabua_esq1' not in self.fases.getObstaculos()):
					self.fases.removeObstaculo("tabua_dir")

				else:
					pass

			elif ((px.btnp(px.MOUSE_BUTTON_LEFT)) and (self.fases.clique(self.mouse_x,self.mouse_y,"chave_g")) and len(self.fases.getObstaculos()) == 0):
				self.fases.venceu()
				id = 4
			else:
				pass

			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 79 and self.mouse_x >= 70) and (self.mouse_y <= 24 and self.mouse_y >= 13)): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("pe_cabra") #Adiona item ao invetário pelo nome

			if px.btnp(px.MOUSE_BUTTON_LEFT) and ((self.mouse_x <= 23 and self.mouse_x >= 10) and (self.mouse_y <= 106 and self.mouse_y >= 100)) and ('tabua_dir' not in self.fases.getObstaculos()): #Se clicar no item ele é adicionado ao inventário
				self.fases.addItem("chave_g") #Adiona item ao invetário pelo nome
			
	def draw(self):
		global id #Controla os frames/fases
		if id == 1: #Seta a Tela Inicial
			self.inicial.rodarInicial()
		elif id == 0: #Controla os frames/fases
			self.fases.fase01() #Seta a Fase 1
		elif id == 2:
			self.fases.fase02() #Seta a Fase 2
		elif id == 3:
			self.fases.fase03() #Seta a Fase 3
		elif id == 4:
			self.final.tela_final(self.fases.getTempo()) #Seta a Tela Final
			
		px.mouse(True)