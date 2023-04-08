# Cafeteria project : Create an live menu
# and payment system (a.k.a console program) :

# First the program should ask if table was reserved/
# not (Providing your full name) . And then if not
# would assign you a table (there is a specific number single,
#                            double or family tables) .
# After table is assigned to you, system should show
# how many free tables are and how which are reserved/occupied.
# The system must be able to show name/surname of the person of
# the reserved table (CLI option : enter reserved table nuber ;
#                      OUTCOME: Name/Surname/Time Reserved)
# After assigning table, system should show different menu options
# for breakfast, lunch , dinner , drinks (alcohol. alcohol free),
# to choose from. Special menu for vegetarian and vegan must be
# included too in the special menu. All menu items should have weight,
# preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section.
# Thus I can delete, add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering.
# After I finish, I need to see what I chosen, the full payable amount
# and approx waiting time for the food to be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).

# Kavinės projektas: sukurkite tiesioginį meniu ir
# mokėjimo sistemą (dar žinoma kaip konsolinė programa):

# Pirmiausia programa turėtų paklausti, ar stalas buvo rezervuotas /
# ne (nurodant jūsų vardą ir pavardę). O jei ne, priskirtų jums lentelę
# (yra konkretus skaičius vienos, dvivietės ar šeimos lentelės).
# Jums priskyrus lentelę, sistema turi parodyti, kiek yra laisvų staliukų
# ir kaip kurie rezervuoti/užimti. Sistema turi turėti galimybę parodyti
# rezervuotos lentelės asmens vardą/pavardę (CLI parinktis: įveskite rezervuotos
#                                            lentelės numerį;
#                                            REZULTATAS: Vardas/Pavardė/Rezervuotas laikas)
# Paskyrus lentelę, sistema turi parodyti skirtingus meniu variantus pusryčiams,
# pietums, vakarienei, gėrimams (be alkoholio, alkoholio), iš kurių galima rinktis.
# Specialus meniu vegetarams ir veganams taip pat turi būti įtrauktas į specialų meniu.
#  Visi meniu elementai turi turėti svorį, paruošimo laiką minutėmis, kalorijas ir kainą.
# Turiu turėti galimybę pakeisti užsakymą prieš mokėjimo skyrių. Taigi galiu ištrinti,
# pridėti daugiau, atnaujinti to paties užsakymo sumą.
# Turėčiau turėti galimybę iš visų meniu vienu užsakymu pasirinkti ką tik noriu.
# Kai baigsiu, turiu pamatyti, ką pasirinkau,
# visą mokėtiną sumą ir apytikslį laukimo laiką, kol maistas bus patiektas
# Pridėkite parinktį pridėti arbatpinigių (% nuo visos kainos)
# prie galutinės sąskaitos.
# Po apmokėjimo sistema turi sugeneruoti kvitą (registravimą).


import random
import datetime
from typing import List


class Project:
    def __init__(
        self, stalai_1: int, stalai_2: int, stalai_4: int, laikas: datetime
    ) -> None:
        self.stalai_1: int = stalai_1
        self.stalai_2: int = stalai_2
        self.stalai_4: int = stalai_4
        self.laikas: datetime = laikas

    def get_laisvi_stalai(self) -> str:
        t: datetime = self.laikas
        if 2200 <= t <= 2400 or 0000 <= t <= 800:
            return "Kavine uzdaryta"
        else:
            laisvi_stalai_1: int = random.randint(1, self.stalai_1)
            laisvi_stalai_2: int = random.randint(1, self.stalai_2)
            laisvi_stalai_4: int = random.randint(1, self.stalai_4)
            return f"Liko laisvu stalu :  stalai_1:  {laisvi_stalai_1}, stalai_2:  {laisvi_stalai_2}, stalai_4:  {laisvi_stalai_4}"


class Reserv(Project):
    def __init__(self, rezervuotas_stalas: bool, name: str, surname: str) -> None:
        self.rezervuotas_stalas: bool = rezervuotas_stalas
        self.name: str = name
        self.surname: str = surname

    def get_rezervuotas_stalas(self) -> str:
        if self.rezervuotas_stalas == True:
            return f"Prasome pasakyti savo varda ir pavarde"

        elif self.rezervuotas_stalas == False:
            return "Prasome palaukti"


class Person(Reserv):
    def __init__(self, name: str, surname: str) -> None:
        self.name: str = name
        self.surname: str = surname


class Laikas(Project):
    def __init__(self) -> None:
        self.laikas: datetime = laikas
        super().__init__(laikas=laikas)

    PUSRYCIAI: dict[str, set[int]] = {
        "gerimai": {1, 2, 3, 4, 5, 6, 7},
        "maistas": {11, 12, 13, 14, 15, 16, 17},
    }
    PIETUS: dict[str, set[int]] = {
        "gerimai": {
            21,
            22,
            23,
            24,
            25,
            26,
            27,
        },
        "maistas": {211, 212, 213, 214, 215, 216, 217},
    }
    PAVAKARIAI = {
        "gerimai": {31, 32, 33, 34, 35, 36, 37},
        "maistas": {311, 312, 313, 314, 315, 316, 317},
    }
    VAKARIENE = {
        "gerimai": {41, 42, 43, 44, 45, 46, 47},
        "maistas": {411, 412, 413, 414, 415, 416, 417},
    }
    ALK_GERIMAI = {"Alkoholiniai gerimai": {541, 542, 543, 544, 545, 546, 547}}

    def get_laikas(self) -> str:
        
        t: datetime = self.laikas
        if 800 <= t <= 1100:
            return f"Dabar yra pusryciu metas. Prasome pasirinkti is {self.PUSRYCIAI} meniu :"
        elif 1100 <= t <= 1600:
            return f"Dabar yra pietu metas. Prasome pasirinkti is {self.PIETUS} ir {self.ALK_GERIMAI}"
        elif 1600 <= t <= 1900:
            return f"Dabar yra pavakariu metas. Prasome pasirinkti is {self.PAVAKARIAI} ir {self.ALK_GERIMAI}"
        elif 1900 <= t <= 2200:
            return f"Dabar yra vakarienes metas. Prasome pasirinkti is {self.VAKARIENE} ir {self.ALK_GERIMAI}"
        else:
            return "Kavine uzdaryta"


# lk = Laikas(805)
rez = Reserv(True, "peter", "piotr")
p = Project(5, 5, 5, 805)
per = Person
per = {
    "Peter",
    "Parker",
}

print(rez.get_rezervuotas_stalas())
print(p.get_laisvi_stalai())
#print(get_laikas())
