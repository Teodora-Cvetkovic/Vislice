import model


def izpis_igre(igra):
    tekst = (
        "=============================================="
        "Število preostali poskusov: {stevilo_preostalih_poskusov} \n\n"
        "         {pravilni_del_gesla} \n\n"
        "Neuspeli poskusi: {neuspeli_poskusi} \n\n"
        "=============================================="

    ).format(
        stevilo_preostalih_poskusov = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        neuspeli_poskusi = igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        "########## Jeeeeej!!! Zmaga!!! Geslo je bilo: {geslo} ########## \n\n"
    ).format(
        geslo = igra.geslo
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        "########## Boooo!!! Poraz!!! Geslo je bilo: {geslo} ########## \n\n"
    ).format(
        geslo = igra.geslo
    )
    return tekst

def izpis_napake():
    return "########## Ugiba se ena črka naenkrat ##########"

def zahtevaj_vnos():
    return input("Črka: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        # najprej izpišemo stanje, da vidimo, koliko črk je ipd
        print(izpis_igre(igra))
        # čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_ENA:
            print(izpis_napake())
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            break
    return

pozeni_vmesnik()