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
from datetime import time
from typing import List

# import projekto_duomenys


class Project:
    def __init__(
        self, stalai_1: int, stalai_2: int, stalai_4: int, laikas: time
    ) -> None:
        self.stalai_1: int = stalai_1
        self.stalai_2: int = stalai_2
        self.stalai_4: int = stalai_4
        self.laikas: time = laikas

    def get_laisvi_stalai(self) -> str:
        t: time = self.laikas
        if time(22, 1) <= t <= time(23, 59) or time(0, 0) <= t <= time(7, 59):
            return "Kavine uzdaryta"
        else:
            laisvi_stalai_1: int = random.randint(1, self.stalai_1)
            laisvi_stalai_2: int = random.randint(1, self.stalai_2)
            laisvi_stalai_4: int = random.randint(1, self.stalai_4)
            return f"Liko laisvu stalu :  stalai_1:  {laisvi_stalai_1}, stalai_2:  {laisvi_stalai_2}, stalai_4:  {laisvi_stalai_4}"


class Reserv(Project):
    def __init__(
        self, rezervuotas_stalas: bool, name: str, surname: str, laikas: time
    ) -> None:
        self.rezervuotas_stalas: bool = rezervuotas_stalas
        self.name: str = name
        self.surname: str = surname
        self.laikas: time = laikas

    def get_rezervuotas_stalas(self) -> str:
        t: time = self.laikas
        if time(22, 1) <= t <= time(23, 59) or time(0, 0) <= t <= time(7, 59):
            return "Prisijunkite kavines darbo laiku"
        elif self.rezervuotas_stalas == True:
            return f"Prasome pasakyti savo varda ir pavarde"

        elif self.rezervuotas_stalas == False:
            if "pageidaujate uzeiti" == True:
                "Prasome  praeiti, arba rezervuokite staliuka"


class Person(Reserv, Project):
    def __init__(self, name: str, surname: str, num_per: int) -> None:
        self.name: str = name
        self.surname: str = surname
        self.num_per: int = num_per

    def get_name(self) -> str:
        if self.num_per == 1:
            # liko_laisvi_stalai_1 = laisvi_stalai_1 - 1
            rezerv_laik: int = random.randint(8, 21)
            return f"{self.name}   {self.surname} jus rezervavote vienvieti stala    {rezerv_laik} valandai"

        elif self.num_per == 2:
            # liko_laisvi_stalai_2 = laisvi_stalai_2 - 1
            rezerv_laik: int = random.randint(8, 21)
            return f"{self.name}   {self.surname} jus rezervavote dvivieti stala  {rezerv_laik} valandai"

        elif self.num_per >= 3:
            # liko_laisvi_stalai_4 = laisvi_stalai_4 - 1
            rezerv_laik: int = random.randint(8, 21)
            return f"{self.name}   {self.surname} jus rezervavote seimynini  stala   {rezerv_laik} valandai"
        # return f"liko laisvu stalu :  {liko_laisvi_stalai_1}, {liko_laisvi_stalai_2}, {liko_laisvi_stalai_4}"


class Laikas(Project):
    def __init__(self, laikas: time) -> None:
        self.laikas: time = laikas

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

    def get_menu(self) -> str:
        t: time = self.laikas

        if time(8, 0) <= t <= time(11, 0):
            return f"Dabar yra pusryciu metas. Prasome pasirinkti is {self.PUSRYCIAI} meniu :"
        elif time(11, 1) <= t <= time(16, 0):
            return f"Dabar yra pietu metas. Prasome pasirinkti is {self.PIETUS} ir {self.ALK_GERIMAI}"
        elif time(16, 1) <= t <= time(19, 0):
            return f"Dabar yra pavakariu metas. Prasome pasirinkti is {self.PAVAKARIAI} ir {self.ALK_GERIMAI}"
        elif time(19, 1) <= t <= time(21, 30):
            return f"Dabar yra vakarienes metas. Prasome pasirinkti is {self.VAKARIENE} ir {self.ALK_GERIMAI}"
        elif time(21, 31) <= t <= time(22, 0):
            return f"Siuo metu karstu patiekalu nera. Prasome pasirinkti is {self.ALK_GERIMAI} gerimai"
        else:
            return "Kavine uzdaryta"


lk = Laikas
name = "Pavyzdys"
surname = "Pavyzdinis"
num_per: int = 4
nam = name
sur = surname
st: int = num_per


per = Person(nam, sur, st)
t = time(12, 30)
lk = Laikas(t)
rez = Reserv(True, nam, sur, t)
p = Project(5, 5, 5, t)

# per = {
#     "Peter",
#     "Parker",
# }

print(rez.get_rezervuotas_stalas())

print(per.get_name())
print(p.get_laisvi_stalai())
print(lk.get_menu())
