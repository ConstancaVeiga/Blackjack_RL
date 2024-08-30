# QV Learning algorithm thats allows for deck splitting
import random
import numpy as np

class BlackjackENVsplit:

    # heart = "\u2665"
    # spade = "\u2660"
    # diamond = "\u2666"
    # club = "\u2663"

    # suits = {
    #     "diamonds": diamond,
    #     "hearts": heart,
    #     "spades": spade,
    #     "clubs": club
    # }

    def __init__(self):
        self.deck = self.generate_deck()
        random.shuffle(self.deck)
        self.player_hands = [[]]  # Multiple hands for splitting
        self.dealer_hand = []
        self.current_hand = 0

    @staticmethod
    def generate_deck():
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        deck = [{'number': number, 'suit': suit} for number in numbers for suit in suits]
        return deck

    def deal_card(self):
        return self.deck.pop()

    def start_game(self):
        self.player_hands = [[self.deal_card(), self.deal_card()]]  # Start with one hand
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.current_hand = 0

    @staticmethod
    def hand_value(hand):
        value = 0
        aces = 0
        for card in hand:
            if card['number'] in ['J', 'Q', 'K']:
                value += 10
            elif card['number'] == 'A':
                value += 11
                aces += 1
            else:
                value += int(card['number'])

        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def player_action(self, action):
        current_hand = self.player_hands[self.current_hand]
        if action == "hit":
            current_hand.append(self.deal_card())
        elif action == "split" and len(current_hand) == 2 and current_hand[0]['number'] == current_hand[1]['number']:     # allow for splitting
            self.player_hands.append([self.player_hands[self.current_hand].pop()])
            self.player_hands[self.current_hand].append(self.deal_card())
            self.player_hands[-1].append(self.deal_card())

        return self.game_status()

    def dealer_action(self, output=False):
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
            if output:
                # print("Dealer hits and has:", self.format_cards(self.dealer_hand), self.hand_value(self.dealer_hand))
              pass

    def game_status(self):
        current_hand_value = self.hand_value(self.player_hands[self.current_hand])
        if current_hand_value > 21:
            return "player_bust"
        elif current_hand_value == 21:
            return "player_blackjack"
        else:
            return "continue"

    def game_result(self):
        self.dealer_action()
        results = []
        dealer_value = self.hand_value(self.dealer_hand)

        for hand in self.player_hands:
            player_value = self.hand_value(hand)
            if player_value > 21:
                results.append("loss")
            elif dealer_value > 21 or player_value > dealer_value:
                results.append("win")
            elif player_value == dealer_value:
                results.append("draw")
            else:
                results.append("loss")

        return results

    @staticmethod
    def format_cards(cards):
        result = ""
        for card in cards:
            suit = BlackjackGame.suits[card["suit"]]
            result += f"{card['number']}{suit} "

        return result.strip()
