# Moduł tworzenia przedmiotów dla eksploracji

# Matuszak 2021

class Item(object):
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def __str__(self):
        show = ""
        show += self.name
        show += ","
        show += self.ability


legendary_sword = Item("Excalibur", "Nieśmiertelność")
witch_eye = Item("Oko wiedźmy", "Przewidywanie przyszłości")
dwarf_party = Item("Krasnoludzki browar", "Niestety nie odpocząłeś")
princes_ring = Item("Pierścień ślubny", "Ożenisz się z księżniczką")
princes_castle = Item("Zamek w Davias", "Obrona przed złem oraz bogactwo")
bandit_hand = Item("Złodieje", "Straciłeś cały dobytek")
hungry_troll = Item("Głodny troll", "Zostałeś pożarty")

home_depo = []

if __name__ == "__main__":
    print("To moduł zawierający klasy instancji do travelera")