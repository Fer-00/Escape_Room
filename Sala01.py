from objetos2 import * 

import pyxel as px
import time
import itens

class Jogo:
    def __init__(self):
        self.barricade01 = 35
        self.barricade02 = 70
        self.x = 0
        self.start_time = time.time()  # Marca o início do jogo
        px.init(128, 128, title="Escape Room")
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

        if self.mouse_x >= 35 and self.mouse_x <= 65 and self.mouse_y >= 64 and self.mouse_y <= 100 and px.btn(px.MOUSE_BUTTON_LEFT) and self.x == barricada_value["valor"]:
            print("passou por aqui")
            self.barricade01 = 1000
            self.barricade02 = 1000
            barricada(self.barricade01,self.barricade02)
        
            

    def draw(self):
        

        px.cls(0)
        px.bltm(0,0,1,256,0,128,128,0,0,1.0)
        px.mouse(True)

        HUD02(100,100)
        
        for i in range (10): #faz um monte de tubo no topo da tela
            tubulacao(i*16,0)

        armario01(10,31)
        armario02(42,31)

        mesa_cabeceira(70,110)
        abajur(77,96)

        porta(35,64)
        barricada01(self.barricade01,self.barricade02)
        barricada(35,100)
        cofre(18,96)
        cadeado(23,107)
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