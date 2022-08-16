from player import Player

class Betting:

    def __init__(self, players):
        self._BB = 1000
        self._SB = 500
        self._to_call = 1000
        self._fold_chart = []
        self._entire_bet_chart = []
        self._single_bet_chart = []

        for x in range(len(players)):
            self._fold_chart.append(-1)
            self._entire_bet_chart.append(0)
            self._single_bet_chart.append(0)

    ## modify_single: modifies the single_bet_chart
    def modify_single(self, pos, amount):
        self._single_bet_chart[pos] += amount
        self._entire_bet_chart[pos] += amount

    def single_bet_chart(self, pos):
        return self._single_bet_chart[pos]

    def modify_fold(self, pos):
        self._fold_chart[pos] = 1

    def clear_single(self):
        self._single_bet_chart = []

    def modify_entire(self, pos, amount):
        self._entire_bet_chart[pos] += amount

    def entire_bet_chart(self, pos):
        return self._entire_bet_chart[pos]

    def small_blind(self):
        return self._SB
    
    def big_blind(self):
        return self._BB

    def to_call(self):
        return self._to_call

def preflop(betting, players):

    players[0].subtract_chips(betting.small_blind())
    betting.modify_single(0, betting.small_blind())

    players[1].subtract_chips(betting.big_blind())
    betting.modify_single(1, betting.big_blind())

    ## big blind to call, raise double big blind

    not_finished = True

    turn = 2
    ## big blind in the beginning as "raiser"
    raiser = -1

    while (not_finished):
        if turn >= len(players):
            turn = 0

        if raiser == turn:
            return

        print("it's player", turn + 1, "'s turn, choose your action: check (if possible), fold, call, raise, or all-in")

        action = input()

        if action == "fold":
            betting.modify_fold(turn)
        elif action == "call":
            players[turn].subtract_chips(betting.to_call() - betting.single_bet_chart(turn))
            betting.modify_single(turn, betting.to_call() - betting.single_bet_chart(turn))
        elif action == "raise":
            raiser = turn
            raise_amount = input("Please input the amount to raise")

            players[turn].subtract_chips(raise_amount - betting.single_bet_chart(turn))
            betting.modify_single(turn, raise_amount - betting.single_bet_chart(turn))

        elif action == "check":
             a = 0
        elif action == "all-in":
            players[turn].subtract_chips(players[turn].chips())
            betting.modify_single(turn, players[turn].chips())

        turn += 1
        
    print(betting.fold_chart)
    print(betting.single_bet_chart)

