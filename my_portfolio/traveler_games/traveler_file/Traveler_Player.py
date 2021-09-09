#Moduł importujący gracza oraz jego możliwości

#Matuszak 2021
from Traveler_land import Land
from random import randrange
class Player(object):
    def __init__(self, name, location, sustain=10):
        self.name = name
        self.sustain = sustain
        self.inventory = []
        self.location = location

    #metoda przedstawiająca atrybuty gracza
    def presentation(self):
        print(self.name)
        print(self.sustain)
        print(self.inventory)
        print(self.location)


    #metoda pozwalająca mu podróżować
    def travel(self, locations):
        print("Witaj podróżniku, gdzie chcesz sie udać?")
        print("Do wyboru masz: ")

        #zmienna dająca możliwość wyboru miejsca po wykonaniu instrukji do zmiennej new_location przez indeksowanie listy
        choose_number = 1

        #Pętla przedstawia po kolei według listy krainy możliwe do zwiedzenia
        for el in locations:
            print(choose_number,"-", el)
            choose_number +=1
        new_location = int(input(""))

        #zwraca wybraną krainę i nadpisuje atrybut location
        return locations[new_location-1]

    # Metoda losująca historie przydażającą się bohaterowi
    def exploration(self, location, story):
        random_story = randrange(0, len(location))
        for keys, value in story.items():
            if location[random_story] == keys:
                print(keys, value)


if __name__ == "__main__":
    print("To moduł zawierający klasy instancji do travelera")