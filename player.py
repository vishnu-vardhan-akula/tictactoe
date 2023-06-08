import math
import random

class player:
    def __init__(self,letter):
        self.letter=letter
'''class computerplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square'''
class Humanplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+'\'s turn.input move (0-9):')
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("invalid square.Try again.")
        return val
'''class computerplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+'\'s turn.input move (0-9):')
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("invalid square.Try again.")
        return val'''
class geniuscomputerplayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        if game.num_empty_squares()==9:
            square=random.choice(game.available_moves())
        else:
            square=self.minimax(game,self.letter)['position']
        return square
    def minimax(self,state,player):
        max_player='x'
        other_player='o' if player =='x' else 'x'
        
        #first,we want to check if the previous move is a winner
        #this is the base case
        if state.current_winner==other_player:
            #we shoulld return the position and score because we need to keep track of the score
            #for minimax to work
            return {
                'position':None,'score':1*(state.num_empty_squares()+1) if other_player ==max_player else -1 * (state.num_empty_squares()+1)
            }
        elif not state.empty_squares():
            return {
                'position':None,'score':0
            }
        if player==max_player:
            best={'position':None,'score':-math.inf}#each score should maximize(be larger)
        else:
            best={'position':None,'score':math.inf}
        for poss_move in state.available_moves():
            #1st:make a move ,try that spot
            state.make_move(poss_move,player)
            #2nd:recurse using minimax to simulate a game after making that move   
            sim_score=self.minimax(state,other_player)#now,we alternate players
            #3rd:undo that move
            state.board[poss_move]=' '
            state.current_winner=None
            sim_score['position']=poss_move
            #4th:update the dictionaries if necessary
            if player==max_player:
                if sim_score['score']>best['score']:
                    best=sim_score
            else:    #minimize the other player
                if sim_score['score']<best['score']:
                    best=sim_score
        return best

