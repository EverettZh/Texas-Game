class Player():
    """
    Fields: _number is the player number
            _ptype determine the player type, whether it is a human or a bot
            _hand determines the current hand of the player
            _name is the player's name
            _chips is the number of chips the player currently have

    """

    def __init__(self, _number, _ptype, _name, _chips = 10000):
        self._number = _number
        self._ptype = _ptype
        self._hand = []
        self._name = _name
        self._chips = _chips

    def name(self):
        return self._name

    def ptype(self):
        return self._ptype

    def set_hand(self, hand):
        self._hand = hand

    def hand(self):
        return self._hand

    def name(self):
        return self._name

    def chips(self):
        return self._chips
    
    ## subtract_chips: subtract current chips of player by amount
    ## Int -> Int
    ## effects: modifies player's chips
    def subtract_chips(self, amount):
        self._chips = self._chips - amount
        return self.chips

def choose_players():
    player_numbers = input("Please enter the number of players playing: ")

    while ((not player_numbers.isdigit) or int(player_numbers) < 2 or int(player_numbers) > 9):
        print("The number of players must be in Integer form and cannot be less than 2 or greater than 9")

        player_numbers = input("Please enter the number of players playing")

    return int(player_numbers)

def create_players(num_players):
    players = []

    for x in range(num_players):
        print("Please enter Player", x + 1, "'s name")
        name = input()
        players.append('')
        players[x] = Player(x, 'human', name, 10000)

    return players

def players_shift(players):
    num_players = len(players)

    shifted_players = []
    shifted_players.append(players[num_players - 1])

    for x in range(num_players - 1):
        shifted_players.append(players[x])

    return shifted_players