from enum import Enum
from datetime import date


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())


TanSzam = 0
Kieg = 0
Kiegész = 0
Kiegészít = 0
i = 0
x = 0
c = 0
tanárokArr = [[25] * 4] * 5
krétákArr = [[25] * 4] * 4
táblákArr = [[25] * 2] * 2
LeirtKarakterhezKreta = 0.00005

filename = 'Tanár Infók.txt'
with open(filename, encoding="UTF-8") as f_obj:
    sorok = f_obj.read().splitlines()
for v in sorok:
    tanárokArr[i] = sorok[i].split(" ")
    i = i + 1

print("Üdvözöljük a tanár-krétahasználat kalkulátorban ezen a gyönyörű " + str(
    Weekday.from_date(date.today())) + " napon. Persze minusz a Weekday. az elejéről, de ez\n részlet kérdése")
print("1. Jénai \n2. Pöpp \n3. Gémesi \n4. Dani \n5. Csekés")


def tanar_keres():
    TanSzame = input("\nAdja meg a tanár sorszámát! (1-5) \n")

    if TanSzame == "1":
        tanar_keres.Kieg = 0
    elif TanSzame == "2":
        tanar_keres.Kieg = 1
    elif TanSzame == "3":
        tanar_keres.Kieg = 2
    elif TanSzame == "4":
        tanar_keres.Kieg = 3
    elif TanSzame == "5":
        tanar_keres.Kieg = 4
    else:
        print("A megadott szám nem megfelelő!")
        tanar_keres()
    return tanar_keres.Kieg


# tanar.seb megadja, hogy egy perc alatt a kiválasztott személy hány szót tud leírni
# tanar.eross megadja, hogy mennyivel több/kevesebb kréta fog elfogyni a karakterek leírásakor. minél kisebb a szám, annál kevesebb kréta fog elfogyni
# tanar.eross ha = 20 ==> 20/100 - zal kell leosztani a krétahasznáálatát, mert enyhén nyomja csak rá a krétát a táblára
# tanar.seb a "Jénai" nevű abszolút nem valós személy esetében beleszámol néhány extra "elveszett" krétát, melyek legenda szerint ma is megtalálhatók az egyetem bejárata előtt a földön

class ErtelmetlenSuperclass:
    def __init__(self, nev, seb, eross, nem, marka, hossz, vonalvast, tipus, karakterszam):
        self.nev = nev
        self.seb = seb
        self.eross = eross
        self.nem = nem
        self.marka = marka
        self.hossz = hossz
        self.vonalvast = vonalvast
        self.tipus = tipus
        self.karakterszam = karakterszam


class Tanarok(ErtelmetlenSuperclass):
    def __init__(self, nev, seb, eross, nem):
        self.nev = nev
        self.seb = seb
        self.eross = eross
        self.nem = nem


tanar_keres()

Kiv_Tanar = Tanarok("nincs", "nincs", "nincs", "nincs")
Kiv_Tanar.nev = tanárokArr[tanar_keres.Kieg][0]
Kiv_Tanar.seb = tanárokArr[tanar_keres.Kieg][1]
Kiv_Tanar.eross = tanárokArr[tanar_keres.Kieg][2]
Kiv_Tanar.nem = tanárokArr[tanar_keres.Kieg][3]
print(Kiv_Tanar.nev, Kiv_Tanar.seb, Kiv_Tanar.eross, Kiv_Tanar.nem)
print("\nA kiválasztott tanár: " + Kiv_Tanar.nev + "! Igazán jó választás")
if Kiv_Tanar.nev == "Dani":
    print("\nVárjunk csak. De... de ő nem is egy tanár. Nem baj! " + Kiv_Tanar.nev + " egy kimagaslóan jó választás!")

filename2 = 'Kréták.txt'
with open(filename2, encoding="UTF-8") as f2_obj:
    krétáknak = f2_obj.read().splitlines()
for v in krétáknak:
    krétákArr[x] = krétáknak[x].split(" ")
    x = x + 1

print("\n1. Crayola\n2. Zsírkréta\n3. Giotto\n4. Sharpie")


def kreta_keres():
    KretaSzame = input("\nAdja meg a használt kréta/íróeszköz sorszámát! (1-4) \n")

    if KretaSzame == "1":
        kreta_keres.Kiegész = 0
    elif KretaSzame == "2":
        kreta_keres.Kiegész = 1
    elif KretaSzame == "3":
        kreta_keres.Kiegész = 2
    elif KretaSzame == "4":
        kreta_keres.Kiegész = 3
    else:
        print("A megadott szám nem megfelelő!")
        kreta_keres()
    return kreta_keres.Kiegész


kreta_keres()


class Kreta(ErtelmetlenSuperclass):
    def __init__(self, marka, hossz, vonalvast, tipus):
        self.marka = marka
        self.hossz = hossz
        self.vonalvast = vonalvast
        self.tipus = tipus


Kiv_Kréta = Kreta("nincs", "nincs", "nincs", "nincs")
Kiv_Kréta.marka = krétákArr[kreta_keres.Kiegész][0]
Kiv_Kréta.hossz = krétákArr[kreta_keres.Kiegész][1]
Kiv_Kréta.vonalvast = krétákArr[kreta_keres.Kiegész][2]
Kiv_Kréta.tipus = krétákArr[kreta_keres.Kiegész][3]

print("\nA kiválasztott kréta márkája: " + Kiv_Kréta.marka)

filename3 = 'Táblák.txt'
with open(filename3, encoding="UTF-8") as f3_obj:
    táblák_beolvas = f3_obj.read().splitlines()
for z in táblák_beolvas:
    táblákArr[c] = táblák_beolvas[c].split(" ")
    c = c + 1

print("\nTáblák típusai: \n1. Krétatábla\n2. Mágnestábla")


def tabla_keres():
    TablaSzama = input("\nAdja meg a használt tábla sorszámát! (1 vagy 2) \n")

    if TablaSzama == "1":
        tabla_keres.Kiegészít = 0
    elif TablaSzama == "2":
        tabla_keres.Kiegészít = 1
    else:
        print("A megadott szám nem megfelelő!")
        tabla_keres()
    return tabla_keres.Kiegészít


class Táblák(ErtelmetlenSuperclass):
    def __init__(self, tipus, karakterszam):
        self.tipus = tipus
        self.karakterszam = karakterszam


tabla_keres()

Kiv_Tábla = Táblák("nincs", "nincs")
Kiv_Tábla.tipus = táblákArr[tabla_keres.Kiegészít][0]
Kiv_Tábla.karakterszam = táblákArr[tabla_keres.Kiegészít][1]
print("\nA megadott tábla: " + Kiv_Tábla.tipus)

if (Kiv_Kréta.tipus == "kréta" and Kiv_Tábla.tipus == "Mágnestábla") or (
        Kiv_Kréta.tipus == "filctoll" and Kiv_Tábla.tipus == "Krétatábla"):
    print("Ezzel a krétával nem lehet erre a táblatípusra írni! Próbáld újra!")
else:
    Eredeti_Array = [Kiv_Kréta.hossz, Kiv_Kréta.vonalvast, Kiv_Tanar.eross, Kiv_Tanar.seb, Kiv_Tábla.karakterszam]
    Szamolhato_Array = [int(numeric_string) for numeric_string in Eredeti_Array]

    perclimit = input("Adja meg hány perce lesz a kiválasztott személynek a táblára írnia: (Ajánlott 1-10)\n")
    karakter = input("\nAdja meg hány karaktert kéne leírnia a kiválasztott személynek:\n")

    Kreta_karakterszam = (Szamolhato_Array[0] * 100 / Szamolhato_Array[1])/(Szamolhato_Array[2] / 100)
    LeirtKarakterhezKreta = int(karakter) / Kreta_karakterszam

    SzöveghezIdő = int(karakter) / Szamolhato_Array[3]

    f = open("myfile.txt", "w", encoding="UTF-8")

    if SzöveghezIdő > int(perclimit):

        f.write("Nem tudta leírni a szöveget ennyi idő alatt\n")
        f.write("A szöveg leírásához a választott személynek " + str(SzöveghezIdő) + " percre lett volna szüksége\n")
        f.write("A kiválasztott személynek e szöveg leírásához " + str(
            LeirtKarakterhezKreta) + "db krétára volt szüksége\n")
    elif SzöveghezIdő == int(perclimit):
        f.write("A kiválasztott személy épp, hogy be tudta fejezni a szöveget\n")
        f.write("A kiválasztott személynek e szöveg leírásához " + str(
            LeirtKarakterhezKreta) + "db krétára volt szüksége\n")
    else:
        f.write("A kiválasztott személy bőven időben le tudta írni a szöveget\n")
        f.write("A kiválasztott személynek e szöveg leírásához " + str(
            LeirtKarakterhezKreta) + "db krétára volt szüksége\n")

    if Szamolhato_Array[4] < int(karakter):
        f.write("Egy ilyen hosszú szöveg nem fért ki egy táblára!\n")
    else:
        f.write("A kért hosszúságú szöveg kifért a megadott táblára!\n")
    print("Az eredmények megjelentek a myfile.txt-ben\n")

    f.close()
