
import pyxel as px

def martelo(x, y):
    px.blt(x, y, 0,54,116,5,10,0)

def chave(x, y):
    px.blt(x, y, 0,69,117,8,5,0)

def bilhete(x,y):
    px.blt(x, y, 0,48,128,15,15,0)

def ferramenta(x,y):
    px.blt(x, y, 0,67,130,11,11,0)

def bau(x,y):
    px.blt(x, y, 0,40,48,32,32,0)

def relogio(x,y):
    px.blt(x, y, 0,0,139,25,13,15)

def porta(x,y):
    px.blt(x, y, 0,0,64,32,64,15)

def placaEscape(x,y):
    px.blt(x, y, 0,33,17,40,14,0)

def HUD(x,y):
    px.blt(x, y, 0,48,96,16,16,15)

def cadeado(x,y):
    px.blt(x, y, 0,85,116,6,8,15)

def barricada(x,y):
    px.blt(x, y, 0,96,96,32,24,15)

def cofre(x,y):
    px.blt(x, y, 0,96,128,16,32,0)

def abajur(x,y):
    px.blt(x, y, 0,131,129,10,14,0)

def tubulacao(x,y):
    px.blt(x, y, 0,128,152,16,16,15)

def armario01(x,y):
    px.blt(x, y, 0,128,96,32,24,0)

def armario02(x,y):
    px.blt(x, y, 0,168,96,32,24,0)

def mesa_cabeceira(x,y):
    px.blt(x, y, 0,152,138,24,18,0)

def quadro01(x,y):
    px.blt(x, y, 0,192,136,16,16,0)

def quadro02(x,y):
    px.blt(x, y, 0,192,160,16,16,0)

def number(x,y,number):
    caracteres = ["!","?",":"]

    if number not in caracteres:
        px.blt(x, y, 0,number*4,163,3,5,0)

    elif number == "!":
        px.blt(x, y, 0,42,163,1,5,0)

    elif number == "?":
        px.blt(x, y, 0,44,163,2,5,0)

    elif number == ":":
        px.blt(x, y, 0,40,164,1,3,0)
                
