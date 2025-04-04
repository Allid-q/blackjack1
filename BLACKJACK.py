import random

class Kortstokk:
    def __init__(self):
        verdier = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        sorter = ["K", "S", "H", "R"]  # Kløver, Spar, Hjerter, Ruter
        self.kortstokk = [s + v for s in sorter for v in verdier]
        random.shuffle(self.kortstokk)

    def trekk_kort(self):
        if not self.kortstokk:
            raise ValueError("Kortstokken er tom!")
        return self.kortstokk.pop()

def beregn_verdi(hand):
    """Beregner verdien av en hånd i Blackjack."""
    verdi = 0
    ess_teller = 0
    kortverdier = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    for kort in hand:
        verdi_str = kort[1:]  
        verdi += kortverdier[verdi_str]
        if verdi_str == "A":
            ess_teller += 1

    while verdi > 21 and ess_teller:
        verdi -= 10  
        ess_teller -= 1

    return verdi

def vis_hand(spiller_hand, dealer_hand, skjult=True):
    """Viser hendene, med dealerens kort åpent fra start."""
    print("\nDine kort:", spiller_hand, "Verdi:", beregn_verdi(spiller_hand))
    
    if skjult:
        print("Dealerens kort: [?, " + dealer_hand[1] + "]", "Verdi: ???")
    else:
        print("Dealerens kort:", dealer_hand, "Verdi:", beregn_verdi(dealer_hand))

def blackjack():
    """Kjører en runde med Blackjack."""
    kortstokk = Kortstokk()
    spiller_hand = [kortstokk.trekk_kort(), kortstokk.trekk_kort()]
    dealer_hand = [kortstokk.trekk_kort(), kortstokk.trekk_kort()]

    while True:
        vis_hand(spiller_hand, dealer_hand, skjult=True)

        if beregn_verdi(spiller_hand) == 21:
            print("BLACKJACK! Du vinner!")
            return

        valg = input("Vil du (h)itte eller (s)tå? ").lower()
        if valg == "h":
            spiller_hand.append(kortstokk.trekk_kort())
            if beregn_verdi(spiller_hand) > 21:
                vis_hand(spiller_hand, dealer_hand, skjult=False)
                print("Du har over 21! Du taper.")
                return
        elif valg == "s":
            break

    print("\nDealer spiller...")
    while beregn_verdi(dealer_hand) < 17:
        dealer_hand.append(kortstokk.trekk_kort())

    vis_hand(spiller_hand, dealer_hand, skjult=False)

    spiller_verdi = beregn_verdi(spiller_hand)
    dealer_verdi = beregn_verdi(dealer_hand)

    if dealer_verdi > 21:
        print("Dealer buster! Du vinner!")
    elif spiller_verdi > dealer_verdi:
        print("Du vinner!")
    elif spiller_verdi < dealer_verdi:
        print("Dealer vinner!")
    else:
        print("Uavgjort!")

if __name__ == "__main__":
    blackjack()

