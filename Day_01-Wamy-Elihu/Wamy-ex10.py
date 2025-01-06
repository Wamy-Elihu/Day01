def moyenne_notes():
    
    notes = input("Entrez les notes séparées par des virgules : ")
    liste_notes = [float(note) for note in notes.split(",")]
    moyenne = sum(liste_notes) / len(liste_notes)
    print(f"La moyenne des notes est : {moyenne}")

moyenne_notes()