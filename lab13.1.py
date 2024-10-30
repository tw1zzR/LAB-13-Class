import random

class KARD:
    def __init__(self):
        self.cards = [f"{rank} {suit}" for suit in ["Чирва", "Бубна", "Хреста", "Піка"]
                      for rank in ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]]
        self.count_cards = len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            card = self.cards.pop()
            self.count_cards -= 1
            print(f"Видалено карту: {card}")
            return card
        else:
            print("Карт більше немає!")
            return None

    def deal_to_players(self, num_players):
        hands = {f"Гравець {i + 1}": [] for i in range(num_players)}

        for _ in range(6):
            for player in hands:
                if self.cards:
                    hands[player].append(self.deal_card())
                else:
                    break
        return hands

deck = KARD()

deck.shuffle()

hands = deck.deal_to_players(3)

print("\nРоздані карти:")

for player, hand in hands.items():
    print(f"{player}: {hand}")

print("\nКількість карт, що залишилася в колоді:", deck.count_cards)
