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
		self.item.criaObjeto("Hud",100,100)
		if self.x == 0:
			self.item.criaObjeto("Martelo",105,104)
		elif self.x == 1:
			self.item.criaObjeto("Chave",104,106)
		elif self.x == 2:
			self.item.criaObjeto("Bilhete",100,100)
		elif self.x == 3:
			self.item.criaObjeto("Ferramenta",102,102)
		
		self.item.criaObjeto("Porta",0,0)
		self.item.criaObjeto("Porta",50,50)
		
		px.mouse(True)

Engine()