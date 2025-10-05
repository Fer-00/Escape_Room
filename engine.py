#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import end, home, fase_01

class Engine:
	def __init__(self):
		self.final = end.End(True)
		self.inicial = home.Home()
		self.fases = fase_01.Fase01()
		self_x = 0
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
			if self.fases.lenInventario > 0:
				self_x += 1
			self.fases.ctlInventario(self_x)
		elif id == 1 and (px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN)):
			id = 0
		elif id == 1 and (self.mouse_x <= 79 and self.mouse_x >= 49) and (self.mouse_y <= 71 and self.mouse_y >= 57) and px.btn(px.MOUSE_BUTTON_LEFT):
			id = 0
		else:
			pass
	
	def draw(self):
		global id
		if id == 1:
			self.inicial.rodarInicial()
		elif id == 0:
			self.fases.fase01()
			if len(self.fases.venceu()) > 0:
				self.final.tela_final(self.fases.venceu())
		else:
			pass
		px.mouse(True)

Engine()