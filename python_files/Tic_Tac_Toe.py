import numpy as np
import time

from State import State
from Min_Max import Min_Max
from Alpha_Beta_Pruning import Alpha_Beta_Pruning

class Tic_Tac_Toe:
    WINNER = np.array([
        (0, 1, 2), # row 1 Horizontal-Line
        (3, 4, 5), # row 2 Horizontal-Line
        (6, 7, 8), # row 3 Horizontal-Line
        (0, 3, 6), # Column 1 Vertical-Line
        (1, 4, 7), # Column 2 Vertical-Line
        (2, 5, 8), # Column 3 Vertical-Line
        (0, 4, 8), # Diagonal from the left
        (2, 4, 6)  # Diagonal from the right
    ])
    
    def __init__(self, AI: str = "o", difficult_level: int = 4):
        '''
        Constructor is build the board and initate the variables
        
        :curr_state: State
        :param AI: symbol of the player either "x" or "o"
        :param difficult_level: int (0, 9]
        :return: None
        '''
        opponent = "x"
        if(AI == "x"):
            opponent = "o"
        elif (AI != "x" and AI != "o"):
            raise Exception("Symbol not Recongized!")
        
        if(difficult_level <= 0 or difficult_level > 9):
            difficult_level = 4
            print("set_difficult_level=4")
        
        self.__curr_state = State(opponent, AI, difficult_level)
        self.__tree_size = -1
        self.__depth = -1
        self.__time_to_think = -1
        
    def get_state(self) -> State:
        '''
        get_state method is getter method
        
        :return: State
        '''
        return self.__curr_state
    
    def get_difficult_level(self) -> int:
        '''
        get_difficult_level method is getter method
        
        :return: int
        '''
        return self.get_state().get_difficult_level()
            
    def get_AI(self) -> str:
        '''
        get_AI method getting the computer symbol
        
        :return: string "x" or "o"
        '''
        return self.get_state().get_AI()      
        
    def get_opponent(self) -> str:
        '''
        get_opponent method getting the player symbol
        
        :return: string "x" or "o"
        '''
        return self.get_state().get_opponent()
    
    def get_depth(self) -> int:
        '''
        get_depth method is getting the current depth of game tree
        
        :return: int
        '''
        return self.__depth
    
    def get_tree_size(self) -> int:
        '''
        get_tree_size method is getting the size of tree
        
        :return: int
        '''
        return self.__tree_size
    
    def get_time(self) -> int:
        '''
        get_time method is getting the time of thinking as AI
        
        :return: int
        '''
        return self.__time_to_think
    
    def get_winner(self) -> tuple:
        '''
        get_winner method is getter method
        
        :return: Tuple (symbol, "player" or "computer")
        '''
        is_draw = self.get_state().is_draw()
        is_win = self.get_state().is_win()
        
        if(is_draw or not is_win):
            return None
        else:
            if(self.get_state().get_winner() == self.get_state().get_AI()):
                return (self.get_state().get_AI(), "Computer")
            else:
                return (self.get_state().get_opponent(), "Player")

    def is_game_end(self) -> bool:
        return self.get_state().is_game_end()
          
    def make_move(self, cell_num: int) -> bool:
        move = self.get_state().make_move(cell_num)
        if(type(move) == State):
            self.__curr_state = move
            return True
        return False
    
    def play(self, algorithm: str = "minmax") -> str:
        '''
        play method it is similar to start button
        
        :return: None
        '''
        Min_Max.Expanded_Nodes = 0
        Alpha_Beta_Pruning.Expanded_Nodes = 0

        time_ex = []
        while(not self.is_game_end()): 
            if(self.get_state().get_turn() == self.get_state().get_AI()):
                move = None
                start = time.time()
                if(algorithm == "minmax"):
                    move = Min_Max.min_max(self.get_state())
                else:
                    move = Alpha_Beta_Pruning.min_max(self.get_state())
                end = time.time()
                time_ex.append(end - start)
                
                self.make_move(move)
            else:
                print(self)
                num = int(input())
                while(not self.make_move(num)):
                    print("You should choose empty domain")
                    print(self)
                    num = int(input())
        
        print(self)
        
        self.__depth = self.get_state().get_curr_depth()
        if(algorithm == "minmax"):
            self.__tree_size = Min_Max.Expanded_Nodes
        else:
            self.__tree_size = Alpha_Beta_Pruning.Expanded_Nodes
        
        self.__time_to_think = np.mean(time)
        winner = self.get_winner()
        if(self.get_winner() == None):
            return f"Avg time of AI Thinking: {self.__time_to_think}\nDRAW!"
        else:
            return f"Avg time of AI Thinking: {self.__time_to_think}\nThe Winner is the {winner[1]} ({winner[0]})"
    
    def automate_play(self) -> str:
        '''
        play method it is similar to start button
        
        :return: None
        '''
        Min_Max.Expanded_Nodes = 0
        Alpha_Beta_Pruning.Expanded_Nodes = 0
        
        time_minmax = []
        time_alpha = []
        
        while(not self.is_game_end()): 
            if(self.get_state().get_turn() == self.get_state().get_AI()):
                start_time = time.time()
                move = Min_Max.min_max(self.get_state())
                end_time = time.time()
                time_minmax.append(end_time - start_time)
                
                start_time = time.time()
                move = Alpha_Beta_Pruning.min_max(self.get_state())
                end_time = time.time()
                time_alpha.append(end_time - start_time)
                
                self.make_move(move)
            else:
                num = np.random.randint(9)
                while(not self.make_move(num)):
                    num = np.random.randint(9)
    
        return [np.mean(time_minmax),
                np.mean(time_alpha),
                Min_Max.Expanded_Nodes,
                Alpha_Beta_Pruning.Expanded_Nodes,
                self.get_state().get_curr_depth(),
                self.get_difficult_level(),
                self.get_state().get_winner() == self.get_AI()]
    
    def __str__(self) -> str:
        return str(self.get_state())