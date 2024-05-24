import random
# draw_card picks a random card from the list then turns it into a tuple with the (index + 2) for easy sorting


def draw_card() -> tuple:
    cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
    card_index = random.choice(range(len(cards)))
    card_value = cards[card_index]
    drawn_card = ((card_index + 2), card_value)
    return drawn_card


def check_straight(card1: tuple, card2: tuple, card3: tuple) -> int:
    hand = [(card1[0]), (card2[0]), (card3[0])]
    hand.sort()
    if hand[0] == hand[1] - 1 and hand[1] == hand[2] - 1:
        score = hand[2]
        return score
    else:
        return 0


def check_3ofa_kind(card1: tuple, card2: tuple, card3: tuple) -> int:
    if card1 == card2 == card3:
        score = (card1[0])
        return score
    else:
        return 0


def check_royal_flush(card1: tuple, card2: tuple, card3: tuple) -> int:
    if check_straight(card1, card2, card3) == 14:
        score = 14
        return score
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3) -> int:
    print(f"The left player's hand was: {left1[1]}, {left2[1]}, and {left3[1]}")
    print(f"The right player's hand was: {right1[1]}, {right2[1]}, and {right3[1]}")
    left_3 = check_3ofa_kind(left1, left2, left3)
    left_straight = check_straight(left1, left2, left3)
    left_flush = check_royal_flush(left1, left2, left3)
    right_3 = check_3ofa_kind(right1, right2, right3)
    right_straight = check_straight(right1, right2, right3)
    right_flush = check_royal_flush(right1, right2, right3)

    # checking for royal flush, if both have one, game is a draw
    if left_flush == 14 and right_flush < 14:
        print('Left is the winner')
        return -1
    elif right_flush == 14 and left_flush < 14:
        print('Right is the winner')
        return 1

    # checking for straights
    elif left_straight > 0 or right_straight > 0:
        if left_straight > right_straight:
            print('Left is the winner')
            return -1
        elif right_straight > left_straight:
            print('Right is the winner')
            return 1
        else:
            print('The game is a draw')
            return 0

    # checking for 3 of a kind
    elif left_3 > right_3:
        print('Left is the winner')
        return -1
    elif right_3 > left_3:
        print('Right is the winner')
        return 1

    # all other options
    else:
        print('The game is a draw')
        return 0


print(play_cards(draw_card(), draw_card(), draw_card(), draw_card(), draw_card(), draw_card()))
