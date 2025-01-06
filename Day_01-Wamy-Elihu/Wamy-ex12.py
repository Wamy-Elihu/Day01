import random
import string

def generateur():

    longueur = int(input("Entrez la longueur souhaitée du mot de passe : "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    print(f"Votre mot de passe sera : {mot_de_passe}")

generateur()