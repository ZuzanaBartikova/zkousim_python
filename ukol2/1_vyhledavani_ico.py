import requests
import json 
# CAST 1 

# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace
zadane_ico = str(input("Zadejte IČO: "))

# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO
# ICO nahraď číslem, které zadal(ka) uživatel(ka). 

url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + zadane_ico
response = requests.get(url)

# převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa). 
data = response.json()
obchodni_jmeno = data.get('obchodniJmeno')
adresa_info = data.get('sidlo')
adresa = adresa_info.get('textovaAdresa')

# Získané informace vypiš na obrazovku.
print(f"{obchodni_jmeno}")
print(f"{adresa}")


