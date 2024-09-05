import random
random.seed()
x=random.randint(1,100)
intento1=0
intento2=0
acierto=False
while acierto ==False:
    p1 = int(input("Turno jugador 1:"))
    intento1=intento1+1
    if (p1 > x):
        print("El número2",p1,"es mayor que X")
    if (p1 < x):
        print("El número",p1,"es menor que X")
    if (p1 == x):
        acierto = True
        print ("Gana el jugador 1 en",intento1,"intentos")
    p2 = int(input("Turno jugador 2:"))
    itnento2=intento2+1
    if (p2 > x):
        print("El número2",p2,"es mayor que X")
    if (p2 < x):
        print("El número",p2,"es menor que X")
    if (p2 == x):
        acierto = True
        print ("Gana el jugador 2 en",intento2,"intentos")