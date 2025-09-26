#testando as coodernadas
import pyxel as px

class Engine:
	def __init__(self):
		px.init(128,128,title="Escape Room")
		px.load('1.pyxres')
		px.run(self.draw,self.update)

	def update(self):
		pass
	
	def draw(self):
		px.cls(2)
		px.bltm(0,0,1,128,0,128,128,1,0,1.0)
		px.bltm(49,57,1,50,50,30,14)
		px.mouse(True)

Engine()