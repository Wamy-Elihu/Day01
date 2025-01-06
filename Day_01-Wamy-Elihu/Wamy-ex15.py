import random

def nombre_mystere():
    nombre_secret = random.randint(1, 1000)
    essais = 10

    print("Le nombre mystère entre 1 et 1000. Vous avez 10 petits essais pour le deviner et montrer votre valeur alors soyez vigilants...")

    for _ in range(essais):
        devine = int(input("Entrez votre idée: "))
        if devine < nombre_secret:
            print("Trop bas !")
        elif devine > nombre_secret:
            print("Trop haut !")
        else:
            print("CONGRATULATION! INCREDIBLE! Vous avez deviné le nombre exact.")
            return
    print(f"Désolé, vous avez échoué. Le nombre était {nombre_secret}, dommage.")

nombre_mystere()
