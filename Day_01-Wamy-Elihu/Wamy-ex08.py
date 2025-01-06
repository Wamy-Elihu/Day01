def trouver_maximum():
    
    nombres = [float(input(f"Entrez le nombre {i+1} : ")) for i in range(3)]
    maximum = max(nombres)
    print(f"Le plus grand nombre est : {maximum}")

trouver_maximum()