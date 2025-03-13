import random
alias=input("Introduce tu alias:")

while True:
    jugador1=0
    banca1=0

    while True:
        carta=random.randint(1,12)
        while carta==8 or carta==9:
            carta=random.randint(1,12)
        if carta>=10:
            valor_carta=0.5
        else:
            valor_carta=carta
        
        print(f"{alias} recibe carta ({carta}) (Valor:{valor_carta})")
        jugador1+=valor_carta
        print(f"Puntos de {alias}:{jugador1}")

        if jugador1>=7.5:
            if jugador1==7.5:
                print("Has alcanzado 7.5 exactos")
            else:
                print("Te has pasado de 7.5")
            break

        respuesta=input("¿Quieres otra carta?(si/no):").lower()
        if respuesta!="si":
            break

    if jugador1<=7.5:
        while banca1<5.0 and banca1<=7.5:
            input("Da al Enter para que la Banca reciba una carta.")
            carta=random.randint(1,12)
            while carta==8 or carta==9:
                carta=random.randint(1,12)
            if carta>=10:
                valor_carta=0.5
            else:
                valor_carta=carta
            
            print(f"La Banca recibe carta ({carta}) (Valor:{valor_carta})")
            banca1+=valor_carta
            print(f"Puntos de la Banca:     {banca1}")

    if jugador1>7.5 and banca1>7.5:
        print("jugador y banca superan 7.5. Pierden los dos")
    elif jugador1>7.5:
        print(f"{alias} se ha pasado de 7.5. Gana la Banca")
    elif banca1>7.5:
        print("La Banca se ha pasado de 7.5. Gana el Jugador")
    elif jugador1==7.5 and banca1<7.5:
        print("Gana el Jugador")
    elif jugador1>banca1:
        print(f"{alias} tiene más puntos. Gana el Jugador")
    elif jugador1==banca1:
        print("Empate")
    else:
        print("La Banca tiene más puntos. Gana la Banca")

    var1=input("¿Quieres una nueva partida?(si/no):").lower()
    if var1!="si":
        print("Fin de la partida")
        break
