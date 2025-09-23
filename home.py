import pyxel as px
import frames

#Tela de inicio/Welcome

class Home:
	def __init__(self):
		self.frame = frames.Frames()
		global id
		id = 1
		px.run(self.draw,self.update)
	def update(self):
		global id
		self.mouse_x = px.mouse_x
		self.mouse_y = px.mouse_y
		if px.btnp(px.KEY_Q):
			px.quit()
		elif px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN):
			#self.frame.jogo_start() #variável pertencente a frames que será declarada futuramente
			id = 0
		elif (self.mouse_x <= 64 and self.mouse_x >= 54) and (self.mouse_y <= 64 and self.mouse_y >= 54) and px.btn(px.MOUSE_BUTTON_LEFT):
			#self.frame.jogo_start()
			id = 0
		else:
			pass
	def draw(self):
		global id
		if id == 1:
			self.corFundo = 4
			px.cls(self.corFundo)
			px.bltm(0,0,1,128,0,128,128,1,0,1.0)
			px.bltm(49,57,1,65,26,30,14)
			px.mouse(True)
		elif id == 0:
			self.corFundo = 0
			px.cls(self.corFundo)	
			px.bltm(0,0,1,0,0,128,128,0,0,1.0)
			#px.text(5,118,"TEXTO",px.COLOR_WHITE)
			px.mouse(True)
		else:
			pass
Home()