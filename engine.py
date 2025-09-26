#passar o motor do jogo para ca, deixar apenas os metodos nas outras
import pyxel as px
import frames, end, home
#, end, fase_01, home

class Engine:
	def __init__(self):
		self.frame = frames.Frames()
		self.final = end.End()
		self.inicial = home.Home()
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
#			self.corFundo = 4
#			px.cls(self.corFundo)
#			px.bltm(0,0,1,128,0,128,128,1,0,1.0)
#			px.bltm(49,57,1,65,26,30,14) #65 26 coordenadas do botão escape
			self.inicial.rodarInicial()
			id = 0
		elif id == 0:
			self.corFundo = 0
			px.cls(self.corFundo)	
			px.bltm(0,0,1,0,0,128,128,0,0,1.0)
			#px.text(5,118,"TEXTO",px.COLOR_WHITE)
		elif id == 2:
			self.final.tela_final()
			#tela final
		else:
			pass
		px.mouse(True)

Engine()