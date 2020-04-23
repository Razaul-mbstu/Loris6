import random

class Game:
    def __init__(self,id,starter):
        self.id = id
        self.joker = 'Joker'
        self.all_cards = {}
        self.cards = self.load_cards()

        self.ready = False
        self.player_ready = [False,False,False,False,False,False]

        self.starter = starter
        self.turn = [False,False,False,False,False,False]
        self.moves = [None,None,None,None,None,None]
        self.chance_to_turn = starter
        self.trick_done = False
        self.trickTaker = -1     # Who takes a trick
        self.running_card = ''   # Cards Running on the table
        self.cards_on_table = {}

        self.art_card = [True,True,True,True,True,True]
        self.prev_trick = False
        self.prev_taker = -1
        self.called = False
        self.trump_taken = False
        self.trump_card = ''
        self.min_call = 3
        self.high_call_taker = -1
        self.chance_to_call = starter
        self.passed = 0
        self.trick_taken = [0,0] #Number of tricks taken by a team

        self.call_taken = {}
        self.points = [0,0]      # Total Points of a Team...
        self.team1 = [0,2,4]
        self.team2 = [1,3,5]
        self.power = False
        self.shuffle_cards()

    def playerReady(self,p):
        self.player_ready[p] = True

    def playerGone(self,p):
        self.player_ready[p] = False
        self.ready = False
        self.min_call = 3
        self.high_call_taker = -1
        self.chance_to_call = self.starter
        self.chance_to_turn = self.starter
        self.art_card = [True,True,True,True,True,True]
        self.turn = [False,False,False,False,False,False]
        self.moves = [None,None,None,None,None,None]
        self.called = False
        self.trump_taken = False
        self.trump_card = ''
        self.passed = 0
        self.prev_taker = -1
        self.prev_trick = False
        self.trick_taken = [0,0] #Number of tricks taken by a team
        self.call_taken = {}
        self.shuffle_cards()

    def readyGame(self):
        self.ready = True
        #self.shuffle_cards()

    def all_ready(self):
        T = True
        for t in self.player_ready:
            T = T and t
        return T

    def all_gone(self):
        T = False
        for t in self.player_ready:
            T = T or t
        return not T

    def artCard(self,p):
        self.art_card[p] = False

    def raisePower(self):
        self.power = True

    def reDistibrute(self):
        self.shuffle_cards()
        #Calculate total points
        a = self.trick_taken[0]
        b = self.trick_taken[1]
        taker = self.high_call_taker
        if taker == 0 or taker == 2 or taker == 4:
            if a >= self.min_call:
                if self.points[1] == 0:
                    self.points[0] = self.points[0]+self.min_call
                else:
                    if self.points[1]>=self.min_call:
                        self.points[1] = self.points[1] - self.min_call
                    else:
                        self.points[0] = self.min_call - self.points[1]
                        self.points[1] = 0
            else:
                if self.points[0] == 0:
                    self.points[1] = self.points[1]+self.min_call*2
                else:
                    if self.points[0] >= self.min_call*2:
                        self.points[0] = self.points[0] - self.min_call*2
                    else:
                        self.points[1] = self.min_call*2 - self.points[0]
                        self.points[0] = 0
        else:
            if b >= self.min_call:
                if self.points[0] == 0:
                    self.points[1] = self.points[1]+self.min_call
                else:
                    if self.points[0]>=self.min_call:
                        self.points[0] = self.points[0] - self.min_call
                    else:
                        self.points[1] = self.min_call - self.points[0]
                        self.points[0] = 0
            else:
                if self.points[1] == 0:
                    self.points[0] = self.points[0]+self.min_call*2
                else:
                    if self.points[1] >= self.min_call*2:
                        self.points[1] = self.points[1] - self.min_call*2
                    else:
                        self.points[0] = self.min_call*2 - self.points[1]
                        self.points[1] = 1

        if self.points[0] == 0:
            random.shuffle(self.team2)
            self.starter = self.team2[0]
        else:
            random.shuffle(self.team1)
            self.starter = self.team1[0]

        self.art_card = [True,True,True,True,True,True]
        self.chance_to_call = self.starter
        self.chance_to_turn = self.starter
        self.called = False
        self.trump_taken = False
        self.trump_card = ''
        self.min_call = 3
        self.high_call_taker = -1
        self.passed = 0
        self.prev_taker = -1
        self.prev_trick = False
        self.trick_taken = [0,0] #Number of tricks taken by a team
        self.call_taken = {}

    def load_cards(self):
        c_list = []
        for i in range(3,15):
            id = 'C{}'.format(i)
            c_list.append(id)
            self.all_cards[id] = id
        for i in range(3,15):
            id = 'D{}'.format(i)
            c_list.append(id)
            self.all_cards[id] = id
        for i in range(3,15):
            id = 'H{}'.format(i)
            c_list.append(id)
            self.all_cards[id] = id
        for i in range(4,15):
            id = 'S{}'.format(i)
            c_list.append(id)
            self.all_cards[id] = id
        id = 'Joker'
        c_list.append(id)
        self.all_cards[id] = id
        return c_list

    def get_cards(self,p):
        c = []
        for i in range(8):
            c.append(self.cards[p])
            p += 6

        return c

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def get_player_move(self,p):
        '''
        :param p:[0,1,2,3,4,5]
        :return: moves[p]
        '''
        return self.moves[p]

    def connected(self):
        return self.ready

    def all_player_turned(self): ##Wheather all player completed their turn
        T = True
        for t in self.turn:
            T = T and t
        return T

    def reset(self):
        self.turn = [False,False,False,False,False,False]
        self.moves = [None,None,None,None,None,None]
        self.called = False
        self.trick_taken = [0,0]
        self.running_card = ''
        self.cards_on_table = {}
        self.shuffle_cards()

    def reTurn(self):
        self.turn = [False,False,False,False,False,False]
        self.moves = [None,None,None,None,None,None]
        self.trick_done = False
        if self.trickTaker%2 == 0:
            self.trick_taken[0] += 1
        else:
            self.trick_taken[1] += 1
        self.running_card = ''
        self.cards_on_table = {}
        self.starter = self.trickTaker
        self.chance_to_turn = self.starter
        self.trickTaker = -1

    def play(self,player,move):
        self.turn[player] = True
        self.moves[player] = move
        self.cards_on_table[player] = self.all_cards[move]
        self.chance_to_turn += 1
        if self.chance_to_turn == 6:
            self.chance_to_turn = 0
        if player == self.starter:
            self.running_card = move
        self.power = False

    def trick_taker(self):
        taker = self.starter
        r = self.running_card[0]
        trumped = -1
        tr = False
        if r == 'J':
            for i in range(6):
                if self.moves[i][0] == r:
                    taker = i
                    break
        else:
            high_card = int(self.running_card[1:])
            for i in range(6):
                if r == self.moves[i][0] and not tr:
                    c = int(self.moves[i][1:])
                    if c>high_card:
                        taker = i
                        high_card = c
                elif self.moves[i][0] == self.trump_card[0]:
                    c = int(self.moves[i][1:])
                    if trumped < c:
                        trumped = c
                        taker = i
                        tr = True
                elif self.moves[i][0] == self.joker[0]:
                    taker = i
                    break
        self.trick_done = True
        self.prev_trick = True
        self.prev_taker = taker
        self.trickTaker = taker

    def call_up(self,p):
        self.min_call += 1
        self.high_call_taker = p
        self.call_taken[p] = self.min_call

    def call_pass(self,p):
        self.chance_to_call += 1
        self.passed += 1
        if self.passed == 6:
            self.called = True
        else:
            if self.chance_to_call == 6:
                self.chance_to_call = 0

    def trump_selected(self,data):
        self.trump_taken = True
        self.trump_card = data[1:]
