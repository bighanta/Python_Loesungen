
# Erstellung der Klasse Haus mit vorgegebenen Variablen - Aufgabe 1
class Haus:
    def __init__(self, streetname, number, color, price, floors, squaremeters) -> None:
        self.streetname = streetname
        self.number = number
        self.color = color
        self.price = price
        self.floors = floors
        self.squaremeters = squaremeters

    # Ausgabe Einstellungen
    def __str__(self) -> str:
        return "Haus ( \r\n\tStraße: " + str(self.streetname) +", \r\n\tNummer: " + str(self.number) +", \r\n\tNeue Farbe: " + str(self.color) +", \r\n\tPreis: " + str(self.price) +"€, \r\n\tQuadratmeter: " + str(self.squaremeters)+"m^2 \r\n)\r\n"

    # Teil der Aufgabe 4
    def neuer_anstrich(self, color):
        self.color = color
        return "Haus ( \r\n\tStraße: " + str(self.streetname) +", \r\n\tNummer: " + str(self.number) +", \r\n\tNeue Farbe: " + str(self.color) +", \r\n\tPreis: " + str(self.price) +"€, \r\n\tQuadratmeter: " + str(self.squaremeters)+"m^2 \r\n)\r\n"


# Erstellung eines Objekts aus der Klasse Haus - Aufgabe 2
# Erstellung einer Hausliste und Entfernung des letzten Eintrags - Aufgabe 3
house1 = Haus("Gutenbergstraße", 32, "Weiß", 150000, 1, 100)
house2 = Haus("Hauptsrtaße", 42, "Blau", 300000, 2, 150)
house3 = Haus("Gärtnergasse", 69, "Grün", 200000, 1, 130)

houseSale = [house1, house2, house3]
houseSale.pop()

print("Aufgabe 3:", houseSale)

# Erstellen Sie ein neues Haus-Objekt und führen Sie eine Funktion auf dieses aus, die die Farbe ändert - Aufgabe 4
houseColor = Haus("Schillerstraße", 1, "Keine", 100000, 3, 230)
Haus.neuer_anstrich(houseColor, "Gelb")

print("Aufgabe 4:", str(houseColor))

# Entferne alle Häuser über 200.000€ Preis - Aufgabe 5
cheapHouses = [x for x in houseSale if x.price < 200000]

print("Aufgabe 5:", cheapHouses)
