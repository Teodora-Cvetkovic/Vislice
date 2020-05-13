import random

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "o"
NAPACNA_CRKA = "-"
ZMAGA = "w"
PORAZ = "x"
VEC_KOT_ENA =">"

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if not crka in self.crke:
                return False
            else:
                return True
    
    def poraz(self):
        return self.stevilo_napak > STEVILO_DOVOLJENIH_NAPAK

    def pravilini_del_gesla(self):
        delni =''
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + " "
            else:
                delni += "_ "
        return delni[:-1]

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, ugib):
        if len(ugib) > 1:
            return VEC_KOT_ENA
        crka = ugib.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)

            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open("C:\\Users\\teodo\\Desktop\\T\\UVP\\Vislice\\besede.txt", "r", encoding="utf-8") as datoteka_z_besedami:
    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka_z_besedami]

def nova_igra():
    return Igra(random.choice(bazen_besed))


igra = Igra("abrakadabra", ["a", "e"])