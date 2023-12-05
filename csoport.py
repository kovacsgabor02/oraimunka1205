class csoport:

    def __init__(self, nev, evfolyam, atlag):
        self.nev = nev
        self.evfolyam = evfolyam
        self.atlag = atlag

    def __str__(self):
        return f"Név: {self.nev}, évfolyam: {self.evfolyam}, átlag: {self.atlag}."
