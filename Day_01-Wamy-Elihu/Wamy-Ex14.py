def calculer_factoriel():
  
    nombre = int(input("Entrez un nombre entier : "))
    factoriel = 1
    for i in range(1, nombre + 1):
        factoriel *= i
    print(f"Le factoriel de {nombre} est : {factoriel}")

calculer_factoriel()
