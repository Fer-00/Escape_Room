#testando as coodernadas
import pyxel as px
import itens

class Engine:
	def __init__(self):
		self.item = itens.Itens()
		self.x = 0
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		px.run(self.draw,self.update)

	def update(self):
		self.mouse_x = px.mouse_x
		self.mouse_y = px.mouse_y

		if px.btnp(px.KEY_Q):
			if self.x < 4:
				self.x += 1
			else:
				self.x = 0

		if px.btn(px.MOUSE_BUTTON_LEFT):
			if self.x == 1:
				if(self.item.clicado(self.mouse_x,self.mouse_y,"Chave")):
					print("INTERAGIU")
				else:
					pass
			else:
				pass

	
	def draw(self):
		px.cls(2)
		#px.bltm(0,0,1,128,0,128,128,1,0,1.0)
		#px.bltm(49,57,1,50,50,30,14)
		self.item.criaObjeto("HUD",100,100)
		if self.x == 0:
			self.item.criaObjeto("martelo",105,104)
		elif self.x == 1:
			self.item.criaObjeto("chave",104,106)
		elif self.x == 2:
			self.item.criaObjeto("bilhete",100,100)
		elif self.x == 3:
			self.item.criaObjeto("ferramenta",102,102)
		
		self.item.criaObjeto("porta",0,0)
		self.item.criaObjeto("porta",50,50)
		px.blt(10, 10, 0,82,131,13,6,15)
		px.mouse(True)

Engine()