import pyxel as px
import frames

#Tela de inicio/Welcome

class Home:
	def __init__(self):
		self.frame = frames.Frames()
		self.frame.telaInicial()
		px.run(self.draw,self.update)
	def update(self):
		self.mouse_x = px.mouse_x
		self.mouse_y = px.mouse_y
		if px.btnp(px.KEY_Q):
			px.quit()
		elif px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN):
			self.frame.jogo_start() #variável pertencente a frames que será declarada futuramente
		elif (self.mouse_x <= 64 and self.mouse_x >= 54) and (self.mouse_y <= 64 and self.mouse_y >= 54) and px.btn(px.MOUSE_BUTTON_LEFT):
			self.frame.jogo_start()
		else:
			pass
	def draw(self):
		pass
Home()