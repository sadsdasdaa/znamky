predmety=["matematika", "AJ", "chemie", "NJ", "fyzika", "dejepis"]
print("Delka pole je: ", len(predmety))
print("Seznam predmetu: ")
for predmet in predmety:
    print("Predmety: ", predmety)
novyPredmet=input("Zadejte novy predmet.")
predmety.append(novyPredmet)
smazat= input("Napis predmet, ktery chcete smazat.")
if smazat in predmety:
    predmety.remove(smazat)
    print(f"Predmet {smazat} byl vymazan")
else:
    print("Tento predmet neni v seznamu")
predmety.sort()
predmety.reverse()
print(predmety)
