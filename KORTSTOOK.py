import random

class Kortstokk:
    def __init__(self):
        verdier = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        sorter = ["K", "S", "H", "R"]  # Kløver, Spar, Hjerter, Ruter
        self.kortstokk = [s + v for s in sorter for v in verdier]
        random.shuffle(self.kortstokk)  # Stokker kortstokken

    def hand(self, n):
        if n > len(self.kortstokk):
            raise ValueError("Ikke nok kort igjen i kortstokken!")
        hand = self.kortstokk[:n]
        self.kortstokk = self.kortstokk[n:]
        return hand

    def del_ut(self, n, p):
        if n * p > len(self.kortstokk):
            raise ValueError("Ikke nok kort igjen til å dele ut!")
        return [self.hand(n) for _ in range(p)]

    def __str__(self):
        return ", ".join(self.kortstokk)

kortstokk = Kortstokk()
print("Kortstokk:", kortstokk)
hender = kortstokk.del_ut(5, 4)  
print("Hender:", hender)
print("Gjenværende kort:", kortstokk) 