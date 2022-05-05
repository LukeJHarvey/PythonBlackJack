from AbsPlayer import AbsPlayer
class Dealer(AbsPlayer):
    
    def __init__(self):
        super().__init__()
        self.name = "Dealer"


    def choice(self):
        hand_value = self.get_hand_value()
        if min(hand_value) >= 17:
            return False
        else:
            return True