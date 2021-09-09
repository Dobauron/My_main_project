# Główny moduł wykonujący grę

from Traveler_Player import *
from Traveler_land import *
from Traveler_story import davias_story as d_s
from Traveler_story import lorencia_story as l_s
from Traveler_item import home_depo as h_d
from Traveler_story import dic_story


class Main(object):
    # Utworzenie obiektów z klas zaimportowanych
    def __init__(self):
        davias = Land("Davias", "Ice", 7, d_s)
        lorencia = Land("Lorencia", "Leaf", 4, l_s)
        home = Land("Home", "Safe", 1, h_d)
        self.player = Player(input("Jak się zwiesz podróżniku ? "), home)

        self.land_list = [home, davias, lorencia]  # lista krain

    # Przedstawia postać jej parametry oraz krainy i rozpoczyna grę
    def play(self):


        # Główna pętla wykonania
        response = ""
        while response != 0:

            print(self.player.name,   "\nTwoje możliwości to:"
                                      "\n1 - Podróż"
                                      "\n2 - Eksploracja"
                                      "\n3 - Odpoczynek"
                                      "\n0 - Koniec gry")
            response = int(input("Co zamierzasz zrobić: "))

            # Warunek wytrzymałości gracza, aby podróżować i explorować
            if self.player.sustain < 1 and response != 3:
                print("Nie możesz wykonywać zbyt wielu akcji, jesteś zmęczony")

            elif self.player.sustain >= 1 and response == 1:

                self.player.sustain -= 1
                self.player.location = self.player.travel(self.land_list)


            elif self.player.sustain > self.player.location.sustain_cost and response == 2:

                self.player.sustain -= self.player.location.sustain_cost
                self.player.exploration(self.player.location.story, dic_story)


            elif response == 3:
                self.player.sustain += 4
                if self.player.sustain > 10:
                    self.player.sustain = 10

            elif response == 0:
                print("Endgame")



play = Main()
play.play()

def data_for_view(Player_name):

