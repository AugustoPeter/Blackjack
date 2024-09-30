class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_cards(self, cards_list):
        self.cards.extend(cards_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False;

        for card in self.cards:
            self.value += int(card.rank["value"])
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealers " if self.dealer else "Your" } hand ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else :
                print(card)

        if not self.dealer:
            print("Value: ", self.get_value())