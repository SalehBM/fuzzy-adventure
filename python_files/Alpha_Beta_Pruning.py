import numpy as np

from State import State
from Game_Algorithm import Game_Algorithm

class Alpha_Beta_Pruning(Game_Algorithm):
    Expanded_Nodes = 0
    
    def min_max(state: State) -> int:
        '''
        min_max method is implementation for alpha_beta_pruning algorithm
        
        :param state: current state: State
        :return: int
        '''
        best_score = np.NINF
        move = -1
        
        successors = state.get_successors(typ = dict)
        for cell_num, state in successors.items():
            score = Alpha_Beta_Pruning.__min(state.get_successors(), depth = 0)
            #print(f"move: {move}, score: {score}, best_score: {best_score}")
            if(best_score < score):
                best_score = score
                move = cell_num
            Alpha_Beta_Pruning.Expanded_Nodes += 1
            
        return move
        
    def __max(states: list, depth: int, alpha = np.NINF, beta = np.Inf) -> int:
        best_score = np.NINF

        for state in states:
            if(alpha > beta or depth >= state.get_difficult_level() or state.is_game_end()):
                Alpha_Beta_Pruning.Expanded_Nodes += 1
                return state.evaluate()
            
            score = Alpha_Beta_Pruning.__min(state.get_successors(), depth + 1, alpha, beta)
            
            if(best_score < score):
                best_score = score
                alpha = score
                
        return best_score
    
    def __min(states: list, depth: int, alpha = np.NINF, beta = np.Inf):
        best_score = np.Inf

        for state in states:
            if(alpha > beta or depth >= state.get_difficult_level() or state.is_game_end()):
                Alpha_Beta_Pruning.Expanded_Nodes += 1
                return state.evaluate()

            score = Alpha_Beta_Pruning.__max(state.get_successors(), depth + 1, alpha, beta)
            
            if(best_score > score):
                best_score = score
                beta = score 
            
            
        return best_score