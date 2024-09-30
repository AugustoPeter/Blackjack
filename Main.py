import Deck as Deck
import Card as Card
import Hand as Hand

deck = Deck.Deck()
deck.shuffle()

hand = Hand.Hand()
hand.add_cards((deck.deal(2)))
print(hand.display())
