import random
while True:
    puntos=0
    seguir=True
    
    while seguir:
        carta=random.randint(1,12)
        while carta==8 or carta==9:
            carta=random.randint(1,12)
        if carta==10 or carta==11 or carta==12:
            valor_carta=0.5
        else:
            valor_carta=carta
            
        print(f"La carta es: {carta} (Valor: {valor_carta})")
        puntos+=valor_carta
        print(f"Tu puntuación es: {puntos}")
        if puntos>7.5:
            print("¡Has perdido la partida!")
            seguir=False
        elif puntos==7.5:
            print("¡Enhorabuena,has ganado la partida!")
            seguir=False
        else:
            respuesta=input("¿Quieres otra carta? (si/no):").lower()
            if respuesta!="si":
                seguir=False

    if 6<=puntos<7:
        print("Has sido un poco conservador")
    elif puntos<6:
        print("Quizás tendrías que arriesgar un poco ¿no?")

    respuesta_repetir=input("¿Quieres repetir una nueva partida? (si/no): ").lower()
    if respuesta_repetir!="si":
        print("Fin de la partida")
        break
