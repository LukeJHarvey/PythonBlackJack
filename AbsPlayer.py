from Card import Card
class AbsPlayer:
    def __init__(self):
        self.hand = [] #Array of Type Card
        self.bust = False #Boolean, Is Player Busted

    def get_hand_value(self):
        """Return the Value of Players current hand
        If an Ace is in play, then split to multiple totals
        """
        totals = [0]
        for c in self.hand:
            if c.value == "A":
                new_totals = totals.copy()
                for i in range(len(totals)):
                    totals[i] += 1
                    new_totals[i] += 11
                totals += new_totals       
            else: 
                for i in range(len(totals)):
                    totals[i] += Card.CARD_VALUE[c.value]
        return totals

    def get_highest_hand_value(self):
        totals = self.get_hand_value()
        max = -1
        for i in totals:
            if i >= max and i <= 21:
                max = i
        return max

    def add_card(self, new_card):
        """Add an additional card to players hand

        Keyword arguments:
        new_card -- Card being added to the hand
        Return
        True -- Player does not bust
        False -- Player busts
        """
        self.hand.append(new_card)
        if min(self.get_hand_value()) > 21:
            self.bust = True
            return False
        return True
    
    def clear_hand(self):
        """Empty player hand and reset bust status
        Return previous hand
        """
        ret_hand = self.hand.copy()
        self.hand = []
        self.bust = False
        return ret_hand
    
    def print_hand(self):
        ret = ""
        for c in self.hand:
            ret += "{}({}) ".format(c.value, c.suit)
        print(ret)

    def hand_string(self):
        ret = ""
        for c in self.hand:
            ret += "{}({}) ".format(c.value, c.suit)
        return ret

    def choice(self):
        """Players Choice
        True - Hit for another Card
        False - Stay, do not get another Card
        """
        pass