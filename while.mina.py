while True:
    prix_ht = input("Entrez un prix HT (entrez 'O' pour terminer) : ")

    if prix_ht.lower() == 'o' or float(prix_ht) == 0:
        break

    else:
        prix_ht = float(prix_ht)
        prix_ttc = prix_ht * 1.20
        print("Le prix TTC est :", prix_ttc)

print("Fin du programme.")
