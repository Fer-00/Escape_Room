from objetos import * 
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
        px.bltm(0,0,1,258+126,0,128,128,0,0,1.0)

        HUD(100,100)
        
        for i in range (10): #faz um monte de tubo no topo da tela
            tubulacao(i*16,0)

        armario01(10,31)
        armario02(42,31)

        mesa_cabeceira(70,110)
        abajur(77,96)

        porta(35,64)
        barricada(35,65)
        barricada(35,100)
        cofre(18,96)
        relogio(28,18)

        quadro01(90,31)
        quadro02(105,50)

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
        px.text(31, 23, f"{minutos:02}:{segundos:02}", 7)  # Mostra o tempo no canto





        

Jogo()