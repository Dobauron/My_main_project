# Moduł bazowej klasy krainy

# Matuszak 2021


#Klasa krainy
class Land(object):

    def __init__(self, name, kind, sustain_cost, story):
        self.sustain_cost = sustain_cost  # Koszt przejścia w daną krainę
        # self.list_of_danger = []
        self.name = name
        self.kind = kind
        self.story = story


        # troll_story = "Napotkałeś trolle, ugotowały cię i zjadły, koniec gry."
        # witch_story = "Napotkałeś wiedzmę która zamienia cię w żaboklickiego i maks masz garba"
        # bandit_story = "Zaatakowali cię bandyci i okradli, ale wciąż żyjesz"
        # princess_story = "Uratowałeś księżniczkę która w zamian obiecała ci swoją rękę i zamek w krainie Tarkan"
        # dwarf_story = "Napotykasz krasnoludy z którym postanawiasz odpocząć"
        # legendary_sword = "Odnajdujesz skrzynie w której znajduję się legendarny miecz broniący przed trolami"
        # self.list_of_danger.append(troll_story)
        # self.list_of_danger.append(witch_story)
        # self.list_of_danger.append(bandit_story)
        # self.list_of_danger.append(princess_story)
        # self.list_of_danger.append(dwarf_story)
        # self.list_of_danger.append(legendary_sword)


    def __str__(self):
        show = ""
        show += self.name
        return show

    #Metoda prezentacji lokacji
    def presentation(self):
        print(self.name, self.kind)


if __name__ == "__main__":
    print("To moduł zawierający klasy instancji do travelera")