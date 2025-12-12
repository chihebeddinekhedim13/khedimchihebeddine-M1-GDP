# khedimchihebeddine-M1-GDP ... 12/12/2025
# benammar icherak
# benhadji serradj hadjer 
# boukhobza ahmed ramy
# bendada firas walid
# belkhir manel
# 5) Ajouter colonne "Catégorie GC"
def categ(gc):
          if gc > 55:
            return "Riche"
          elif 45 <= gc <= 55:
            return "Moyen"
          else:
            return "Faible"
df["Ctégorie_GC"]=df["Pourcentage_GC"].apply(categ)
print(df)

