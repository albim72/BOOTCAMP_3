class AutoProgramowanie(type):
    def __new__(cls, name, bases, dct):
        # Dodajemy nową metodę do klasy
        dct['nowa_metoda'] = cls.nowa_metoda
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def nowa_metoda(self):
        print("To jest nowa metoda dodana dynamicznie!")


# Klasa wykorzystująca metaklasę AutoProgramowanie
class MojaKlasa(metaclass=AutoProgramowanie):
    def istniejaca_metoda(self):
        print("To jest istniejąca metoda.")


# Tworzymy instancję klasy
obj = MojaKlasa()

# Wywołujemy istniejącą metodę
obj.istniejaca_metoda()

# Wywołujemy nową metodę dodaną dynamicznie
obj.nowa_metoda()
