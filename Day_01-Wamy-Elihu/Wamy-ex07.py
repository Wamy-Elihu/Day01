def compter_voyelles():
    phrase = input("Entrez une phrase : ")
    voyelles = "aeiouyAEIOUY"
    compteur = sum(1 for lettre in phrase if lettre in voyelles)
    print(f"Npmbre de voyelles : {compteur}")

compter_voyelles()