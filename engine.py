#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import frames, end, home, fase_01, time
#, end, fase_01, home

class Engine:
	def __init__(self):
		self.frame = frames.Frames()
		self.final = end.End()
		self.inicial = home.Home()
		self.fases = fase_01.Fase01()
		self.start_time = time.time()  # Marca o início do jogo
		self.minutos, self.segundos = 0,0
		global id
		id = 1
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		px.run(self.draw,self.update)

	def update(self):
		global id
		self.mouse_x = px.mouse_x
		self.mouse_y = px.mouse_y
		if px.btnp(px.KEY_Q):
			px.quit()
		elif px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN):
			id = 0
		elif (self.mouse_x <= 79 and self.mouse_x >= 49) and (self.mouse_y <= 71 and self.mouse_y >= 57) and px.btn(px.MOUSE_BUTTON_LEFT):
			id = 0
		else:
			pass
	
	def draw(self):
		global id
		if id == 1:
			self.inicial.rodarInicial()
		elif self.minutos == 5:
			#perdeu
			self.final.tela_final()
		elif id == 0:
			self.fases.fase01()
			elapsed = int(time.time() - self.start_time)
			self.minutos = elapsed // 60
			self.segundos = elapsed % 60
			px.text(100, 120, f"{self.minutos:02}:{self.segundos:02}", 7)  # Mostra o tempo no canto
		elif id == 2: #venceu
			tempo = str(self.minutos) + ":" + str(self.segundos)
			self.final.tela_final()
			#tela final 
		else:
			pass
		px.mouse(True)

Engine()