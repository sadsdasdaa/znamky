# 1. Načtení od uživatele
vek = input("Zadejte svůj věk: ")  

# 2. Přetypování (převod na číslo)
vek = int(vek)  

# 3. Podmínky (if, elif, else)
if vek < 18:
    status = "nezletilý"
elif vek < 65:
    status = "dospělý"
else:
    status = "senior"

# 4. Logické operátory
plnoletost = vek >= 18 and vek < 65
mladistvy = vek >= 15 and vek < 18

# 5. Vypsání výsledků
print(f"Jste {status}.")
print(f"Plnoletý: {plnoletost}")
print(f"Mladistvý: {mladistvy}")

# 6. Okomentování + podpis
# Tento kód ukazuje základní práci s podmínkami, vstupy a výstupy.

# 7. Příkazy GitHubu:
# git init          # Inicializace repozitáře
# git add soubor.py # Přidání souboru ke commitu
# git commit -m "První commit"
# git push origin main # Odeslání na GitHub