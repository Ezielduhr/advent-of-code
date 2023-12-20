import pytest
from advent_of_code.twenty_three.scratchcards import PileOfCards


@pytest.fixture()
def pile():
    pile = PileOfCards()
    test_input = """Card  10: 38 40 81 54 30 61 82 51 99 71 | 43 74 45 70 18 31 66 96 21 92 61 91 55 67 41 15 77 88 11  7  8 93 30 35 82
Card  11: 69 47 52 27 78 17 39 88 83 72 | 70 87 71 33 25 43 82 49 30 58 67 89 95 74 93 28 99 85 78 73 10 75  9 91 15
Card  12: 54 46 50 79 57 88 90 61 12  5 | 64 33 13 35 57 29 81 89 49 47 37 25 66 68 20 73 19 36 39 79  5 96  3 95 42
Card  13: 67 56 62 13 55 38 89 10 91 75 | 23 58 95 92 17 52 84 64 77 54 20 98 89 83  4 66 87 25 27 51  2 37 81 56 12
Card  14: 54 42 51 76 66 14 74  6 35 89 | 50 47 63 16 91 41 43 39  2 95 84  8 18 23 83 64 97 48 96 69 29 44  1 24 72
Card  15: 83  1 88 31 58 35 21 62 36 33 | 68 30 85 28 71 49  2 86 12 13  7 42 20 93 66 17  4 67 19 65 43  6 16 75 22
Card  16:  3  6 41 38 71 53 86 12 49 84 | 84 12  6 44 31 85 71 50 41 35 27 38 96 42 21  9 13 86 49 91 36 40 53  3 93
Card  17:  1 14 50 61 19 68 48 40 63 69 | 19 11 69 63 25 50 86 80 26 29 42 48 52 21 56 14  6 41 68 40  1 61 36 16  3
Card  18: 27  3 77 91 69 84 14 32 50  5 |  6  5 64 91  3 10  4  1 84 76 77 70 27 59 78 24 32 92 69 50 52 54 82 14 95
Card  19: 93 65  3 23 46 82 49 95 30 91 | 35 89 49 82 32 18 71 46 81 93 95 23 27 45 96 65 94 24 70  3 30 19 85 56 91
Card  20: 73 98 10 19  2 39 42 81 93 41 | 87 42 93 34 95 82 73 83 89 31 70 98 20 12 41 61 10 65 81 71 19 39 35  2  5"""

    for line in test_input.split('\n'):
        pile.add_card(line)
    [card.calculate_score() for card in pile.cards]

    yield pile
    del pile


def test_simple_score(pile):
    assert pile.cards[1].score == 1


def test_multiply_score(pile):
    assert pile.cards[0].score == 4


def test_sum_of_cards(pile):
    pile.calculate_sum_of_cards()
    assert pile.sum_of_cards_score == 2571


def test_amount_of_cards(pile):
    pile.duplicate_cards()
    assert pile.total_amount_of_cards == 66
