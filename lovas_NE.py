class Lo_NE:
    def __init__(self, lonev, hetialkalom = 0 , osszesperc = 0):
        self.lonev = lonev
        self.hetialkalom = hetialkalom
        self.osszesperc = osszesperc

    def edzeshozzaadas(self, ujperc: int):
        self.hetialkalom += 1
        self.osszesperc += ujperc

def terheles_ellenorzes_NE(alkalmak):
    if alkalmak < 3:
        return "Még kevés a heti mozgatás (legalább 3 kell)!"
    elif alkalmak == 3:
        return "Megvan az ideális 3 edzés."
    else:
        return "Túl sok az edzés a héten, pihenőnap kell!"

