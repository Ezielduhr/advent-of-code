from advent_of_code.utilities import GetInput


class PileOfCards:
    def __init__(self):
        self.sum_of_cards_score = int()
        self.cards = list()
        self.total_amount_of_cards = int()

    def add_card(self, card_input):
        card_number, cleaned_input = card_input.split(":")
        winning_numbers, card_numbers = cleaned_input.split("|")
        self.cards.append(Scratchcard(card_number, winning_numbers, card_numbers))

    def calculate_sum_of_cards(self):
        self.sum_of_cards_score = sum([card.score for card in self.cards])

    def duplicate_cards(self):
        for i_card in self.cards:
            # add cards to list so they get counted extra?
            if i_card.matches:
                for match in range(1, i_card.matches+1):
                    card_to_duplicate = i_card.card_number + match
                    [card.add_copy(i_card.copies) for card in self.cards if card.card_number == card_to_duplicate]

        self.total_amount_of_cards = sum([card.copies for card in self.cards])


class Scratchcard:
    def __init__(self, card_number, winning_numbers, card_numbers):
        self.card_number = int(card_number.replace('   ', ' ').replace('  ', ' ').split(' ')[1])
        self.winning_numbers = winning_numbers.replace('  ', ' ')[1:-1].split(' ')
        self.card_numbers = card_numbers.replace('  ', ' ')[1:].split(' ')
        self.copies = 1
        self.matches = int()
        self.score = int()

    def calculate_score(self):
        self.matches = len(set(self.card_numbers).intersection(set(self.winning_numbers)))
        if self.matches == 1:
            self.score = 1
        elif self.matches > 1:
            self.score = 2**(self.matches-1)
        else:
            self.score = 0

    def add_copy(self, amount):
        self.copies += amount


def main(challenge_input):
    pile = PileOfCards()

    for line in challenge_input.split('\n'):
        pile.add_card(line)
    [card.calculate_score() for card in pile.cards]
    pile.calculate_sum_of_cards()
    print(pile.sum_of_cards_score)
    pile.duplicate_cards()
    print(pile.total_amount_of_cards)


if __name__ == "__main__":
    main(GetInput('twenty_three').set_input('input_04.txt'))
