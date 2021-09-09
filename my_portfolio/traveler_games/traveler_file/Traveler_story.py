# Moduł zawierający listę możliwych ewentów dla danej instancji

# Matuszak
from Traveler_item import *

# Historie
troll_story = "Napotkałeś trolle, ugotowały cię i zjadły, koniec gry."
witch_story = "Napotkałeś wiedzmę która zamienia cię w żaboklickiego i maks masz garba"
bandit_story = "Zaatakowali cię bandyci i okradli, ale wciąż żyjesz"
princess_story = "Uratowałeś księżniczkę która w zamian obiecała ci swoją rękę i zamek w krainie Tarkan"
dwarf_story = "Napotykasz krasnoludy z którym postanawiasz odpocząć"
legendary_chest = "Odnajdujesz skrzynie w której znajduję się legendarny miecz broniący przed trolami"


davias_story = [dwarf_story, legendary_chest, troll_story]
lorencia_story = [princess_story, bandit_story, witch_story]

# Słownik który przydziela item, event do histori
dic_story = {troll_story: hungry_troll,
            witch_story: witch_eye,
            bandit_story : bandit_hand,
            princess_story: [princes_ring, princes_castle],
            dwarf_story: dwarf_party,
            legendary_chest: legendary_sword}
