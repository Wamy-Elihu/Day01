import random 

def mes_devinettes():
    nombre_secret = random.randit(1, 100)
    devine = None

    while devine != nombre_secret:
        devine = int(input("DEvinez le nombre (entre 1 et 100) : "))
        if devine < nombre_secret:
            print("Trop bas ?")
        elif devine > nombre_secret:
            print("Trop haut !")
        else : 
            print ("DI MOLTO!! Tu es tombé juste.")

mes_devinettes()