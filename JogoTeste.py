from objetos2 import * 
import pyxel as px
import time

class Jogo:
    def __init__(self):
        self.x = 0
        self.start_time = time.time()  # Marca o início do jogo
        px.init(128, 128, title="Escape Room")
        px.load('1.pyxres')
        px.run(self.draw,self.update)

        
    def update(self):
        if px.btnp(px.KEY_Q):
            if self.x < 4:
                self.x += 1
            else:
                self.x = 0
            

    def draw(self):
        px.bltm(0,0,1,256,0,128,128,0,0,1.0)
        bau(10,96)

        relogio(13,83)
        HUD(100,100)
        if self.x == 0:
            martelo(105,104)
        elif self.x == 1:
            chave(104,106)
        elif self.x == 2:
            bilhete(100,100)
        elif self.x == 3:
            ferramenta(102,102)

# Calcula tempo decorrido
        elapsed = int(time.time() - self.start_time)
        minutos = elapsed // 60
        segundos = elapsed % 60
        px.text(16, 88, f"{minutos:02}:{segundos:02}", 7)  # Mostra o tempo no canto





        

Jogo()