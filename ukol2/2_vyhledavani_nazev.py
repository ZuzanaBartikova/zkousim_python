# CAST 2

import requests
import json

# Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. 
# Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat. 
# Následně vypiš všechny nalezené subjekty, které ti API vrátí.

# Zadání názvu a jeho úprava pro práci s API:
nazev = input("Zadejte název subjektu: ")
pro_data = {"obchodniJmeno": nazev}
json_pro_data = json.dumps(pro_data)

# vyhledání v databázi
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f"{json_pro_data}"
response = (requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data))

# Výstupní data
vystup = response.json()
pocet = vystup.get("pocetCelkem")
subjekty = vystup.get("ekonomickeSubjekty")
print(f"Nalezeno subjektů: {pocet}")
seznam_subjektu = []
for subjekt in subjekty:
    seznam_subjektu.append([subjekt["obchodniJmeno"], subjekt["ico"]])
for subjekt in seznam_subjektu:
    print(", ".join(subjekt))

