def trier_liste():
  
    nombres = input("Entrez une liste de nombres séparés par des virgules : ")
    liste_nombres = [float(nombre) for nombre in nombres.split(",")]
    liste_nombres.sort()
    print("Nombres triés :", liste_nombres)

trier_liste()
