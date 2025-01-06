def calculatrice()
    print("choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez le numéro de l'opération (1/2/3/4) : ")

    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Emtrez le deuxième nombre : "))

    if choix == '1' :
        print(f"Résultat : {num1} + {num2} = {num1 + num2}")
    elif choix == '2':
        print(f"Résultat : {num1} - {num2} = {num1 - num2}")
    elif choix == '3':
        print(f"Résultat : {num1} * {num2} = {num1 * num2}")
    elif choix == '4':
        if num2 != 0:
            print(f"Résultat : {num1} / {num2} = {num1 / num2}")
        else:
            print("Erreur : Division par zéro.")
    else:
        print("Choix invalide.")

calculatrice()