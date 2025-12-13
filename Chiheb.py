# khedimchihebeddine-M1-GDP ... 12/12/2025
# benammar icherak
# benhadji serradj hadjer 
# boukhobza ahmed ramy
# bendada firas walid
# belkhir manel

import pandas as pd
# Données : Séquences ADN , Longueur , pourcentage de GC 
data = {
          "Séquence": [
                    "ATGCGTACGTA","GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACCTAGC",
                    "TTAACCGGAT"      ],
          "Longueur": [12, 12 , 12, 10, 11, 10, 10],
          "Pourcentage_GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# 1) Créer et afficher le tableau
# Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("Tableau initial :")
print(df)

# 2) Afficher uniquement la colonne "Longueur"
print("\nColonne Longueur :")
print(df["Longueur"])


# 3) Filter les séquences longueur > 10
print("\nSéquences avec longueur > 10 :") 
df_filtered = df[df["Longueur"] > 10] 
print (df_filtered)

# 4) Pourcentage moyen de GC (3 chiffres aprés virgule)
moyenne_gc = df["Pourcentage_GC"].mean() 
print("\nPourcentage moyen de GC :", round(moyenne_gc, 3))


# 5) Ajouter colonne "Catégorie GC"
def categ(gc):
        if gc > 55:
            return "Riche"
        elif 45 <= gc <= 55:
            return "Moyen"
        else:
            return "Faible"
                  
df["Catégorie_GC"] = df["Pourcentage_GC"].apply(categ)
print(df)


# 6) Ajouter colonne du nombre de 'G'
df["Nb_G"] = df["Séquence"].apply(lambda seq: seq.count("G"))
print(df)



 # 7) Écart-type de % GC et Longueur
ecart_gc= df["Pourcentage_GC"].std()
ecart_longueur=df["Longueur"].std()
print("\nÉcart-type%GC:",ecart_gc)
print("Écart-typeLongueur:", ecart_longueur)

      
# 8) Sauvegarder en CSV 
df.to_csv("ADN_final.csv", index=False)
      
print("\nFichier 'ADN.cvs' sauvegardé.")
print("\nTableau final :")
print(df) 
      




