def make_deck() -> list[tuple]:
    value = [str(x) for x in range(1, 11)]
    value.extend(["J", "Q", "K"])
    suits = ["♥️", "♦️", "♠️", "♣️"]
    deck = [(x, y) for x in value for y in suits]
    return deck


def draw_cards(deck: list[tuple], cards: tuple | list[tuple]) -> list[tuple]:
    ref_deck = make_deck()
    deck = [x for x in ref_deck if x not in cards]
    return deck


deck = make_deck()
cards_drawn = [
    ("4", "♣️"),
    ("5", "♥️"),
    ("6", "♦️"),
    ("9", "♣️"),
    ("9", "♥️"),
    ("4", "♥️"),
    ("5", "♦️"),
    ("8", "♦️"),
    ("7", "♣️"),
    ("5", "♠️"),
    ("1", "♥️"),
    ("8", "♥️"),
    ("5", "♣️"),
    ("6", "♣️"),
    ("8", "♣️"),
    ("6", "♥️"),
]
deck = draw_cards(deck, cards_drawn)
print(deck)
