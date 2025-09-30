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
    px.blt(x, y, 0,0,64,32,64,0)

def placaEscape(x,y):
    px.blt(x, y, 0,33,17,40,14,0)

def HUD(x,y):
    px.blt(x, y, 0,48,96,16,16,15)

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
                   
