import numpy as np

from State import State
from Game_Algorithm import Game_Algorithm

class Min_Max(Game_Algorithm):
    Expanded_Nodes = 0
    
    def min_max(state: State) -> int:
        '''
        min_max method is implementation for minmax algorithm
        
        :param state: current state: State
        :return: int
        '''
        best_score = np.NINF
        move = -1
        
        successors = state.get_successors(typ = dict)
        for cell_num, state in successors.items():
            score = Min_Max.__min(state.get_successors(), depth = 0)
            #print(f" move: {move}, score: {score}, best_score: {best_score}")
            if(best_score < score):
                best_score = score
                move = cell_num
            Min_Max.Expanded_Nodes += 1
            
        return move
        
    def __max(states: list, depth: int = 0):
        best_score = np.NINF

        for state in states:
            if(depth >= state.get_difficult_level() or state.is_game_end()):
                Min_Max.Expanded_Nodes += 1
                return state.evaluate()
            
            score = Min_Max.__min(state.get_successors(), depth + 1)
            if(best_score < score):
                best_score = score
            
        return best_score
    
    def __min(states: list, depth: int = 0):
        best_score = np.Inf

        for state in states:
            if(depth >= state.get_difficult_level() or state.is_game_end()):
                Min_Max.Expanded_Nodes += 1
                return state.evaluate()

            score = Min_Max.__max(state.get_successors(), depth + 1)
            if(best_score > score):
                best_score = score
              
        return best_score