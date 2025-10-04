#testando as coodernadas
import pyxel as px
import itens

class Engine:
	def __init__(self):
		self.item = itens.Itens()
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		px.run(self.draw,self.update)

	def update(self):
		if (self.mouse_x <= 79 and self.mouse_x >= 49) and (self.mouse_y <= 71 and self.mouse_y >= 57) and px.btn(px.MOUSE_BUTTON_LEFT):
	
	def draw(self):
		px.cls(2)
		#px.bltm(0,0,1,128,0,128,128,1,0,1.0)
		#px.bltm(49,57,1,50,50,30,14)
		self.item.criaObjeto("Chave",50,50)
		px.mouse(True)

Engine()