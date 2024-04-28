# Třída Položka (Item)
# Jedná se o základní třídu pro všechny položky, které lze objednat.

# Měla by mít dva atributy: name (řetězec reprezentující název položky) a price (float reprezentující cenu položky).
# Implementujte metodu __str__ tak, aby vracela řetězcovou reprezentaci položky ve formátu: <název>: <cena> Kč.
# Atributy:

# name: Název položky (string).
# price: Cena položky (float).
# Metody:

# __str__(): Vrací řetězcovou reprezentaci položky.

class Item:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: {self.price} Kč. "
    
# Třída Pizza (dědí z Item)
# Reprezentuje pizzu, která je specifickým typem položky.

# Přidává dodatečný atribut: ingredients (slovník, kde klíče jsou názvy ingrediencí a hodnoty jejich množství v gramech).
# Implementujte metodu add_extra pro přidání extra ingrediencí do pizzy. Tato metoda by měla odpovídajícím způsobem aktualizovat cenu pizzy.
# Napište metodu __str__ tak, aby zahrnovala seznam ingrediencí a celkovou cenu.
# Atributy:

# ingredients: Slovník ingrediencí a jejich množství (dict).
# Metody:

# add_extra(ingredient, quantity, price_per_ingredient): Přidává extra ingredienci do pizzy a aktualizuje její cenu.
# __str__(): Vrací textový popis pizzy včetně ingrediencí a ceny.

class Pizza(Item):
    def __init__(self, name: str, price: float, ingredients: dict, ) -> None:
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: int):
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient

    def __str__(self) -> str:
        for ingredient, quantity in self.ingredients.items():
            ingredients_string = ", ".join([f"{ingredient}: {quantity} g"])
            return f"Pizza {self.name} - Ingredients: {ingredients_string}, Total Price: {self.price} Kč"

margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
print(margarita)
margarita.add_extra("olivy", 50, 10)
print(margarita)

# Třída Drink (dědí z Item)
# Reprezentuje nápoj.

# Přidává dodatečný atribut: volume (integer reprezentující objem nápoje v mililitrech).
# Přepište metodu __str__ tak, aby vracela název nápoje, objem a cenu.
# Atributy:

# volume: Objem nápoje v mililitrech (int).
# Metody:

# __str__(): Vrací popis nápoje, včetně jeho objemu a ceny.

class Drink(Item):
    def __init__(self, name: str, price: float, volume: int) -> None:
        super().__init__(name, price)
        self.volume = volume

    def __str__(self) -> str:
        return super().__str__() + f"Objem: {self.volume} ml. "

fanta = Drink("Fanta", 35, 500)
print(fanta)

# Reprezentuje objednávku učiněnou zákazníkem.
# Měla by obsahovat jméno zákazníka, adresu doručení, seznam objednaných položek a stav objednávky (např. "Nová", "Doručeno").
# Implementujte metodu mark_delivered, která změní stav objednávky na "Doručeno".
# Přepište metodu __str__ tak, aby vracela podrobné informace o objednávce, včetně jména zákazníka, adresy, položek v objednávce a stavu objednávky.
# Atributy:
# customer_name: Jméno zákazníka (string).
# delivery_address: Adresa doručení (string).
# items: Seznam položek v objednávce (list).
# status: Stav objednávky (string).
# Metody:
# mark_delivered(): Označí objednávku jako doručenou.
# __str__(): Vrací detaily objednávky, včetně zákazníka, adresy, položek a stavu.

class Order:
    def __init__(self, customer_name: str, delivery_adress: str, items: list, status = "nedoručena") -> None:
        self.customer_name = customer_name
        self.delivery_adress = delivery_adress
        self.items = items
        self.status = status
    
    def __str__(self) -> str:
        return f"Objednávka na jméno {self.customer_name} na adresu {self.delivery_adress} obsahující položky {", ".join(self.items)} je ve stavu {self.status}. "
    
    def mark_delivered(self):
        self.status = "doručena"

objednavka1 = Order("Zuzka", "Čapkova", ["fanta", "cola", "dezert"])
print(objednavka1)
objednavka1.mark_delivered()
print(objednavka1)

# Třída DeliveryPerson
# Reprezentuje doručovatele.
# Měla by obsahovat jméno doručovatele, telefonní číslo, stav dostupnosti a aktuální objednávku, kterou doručuje (pokud nějakou má).
# Implementujte metodu assign_order, která přiřadí objednávku doručovateli, pokud je dostupný. 
# Stav objednávky by měl být aktualizován na "Na cestě".
# Implementujte metodu complete_delivery, která označí objednávku jako doručenou a doručovatele znovu učiní dostupným pro nové objednávky.
# Přepište metodu __str__ tak, aby vracela informace o doručovateli, včetně jeho stavu dostupnosti.
# Atributy:
# name: Jméno doručovatele (string).
# phone_number: Telefonní číslo doručovatele (string).
# available: Dostupnost doručovatele (bool).
# current_order: Aktuální objednávka k doručení (Order).
# Metody:
# assign_order(order): Přiřadí objednávku doručovateli, pokud je dostupný.
# complete_delivery(): Označí objednávku jako doručenou a doručovatele znovu učiní dostupným.
# __str__(): Vrací informace o doručovateli, včetně jeho stavu dostupnosti.

class DeliveryPerson:
    def __init__(self, name: str, phone_number: str, available: bool, current_order: Order) -> None:
        self.name = name
        self.phone_number = phone_number
        self.available = available
        self.current_order = current_order

    def __str__(self) -> str:
        if self.available == True:
            return f"Doručovatel {self.name} s telefonním číslem {self.phone_number} je dostupný."
        else:
            return f"Doručovatel {self.name} s telefonním číslem {self.phone_number} právě doručuje objednávku: {self.current_order} "
    
    def assign_order(self):
        if self.available == True:
            self.current_order = Order
            self.available = False
    def complete_delivery(self):
        self.available = True


dorucovatel1 = DeliveryPerson("Martin Král", "777 888 999", False, objednavka1)
print(dorucovatel1)
dorucovatel1.complete_delivery()
print(dorucovatel1)


# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)
print(margarita)

# Vytvoření instance nápoje
cola = Drink("Cola", 15, 500)
print(cola)
# Vytvoření a výpis objednávkyˇ

# order = Order("Jan Novák", "Pražská 123", [margarita, cola])
# print(order)