import numpy as np
import copy

class State:
    def __init__(self, player = "x", AI = "o", difficult_level = 4):
        
        self.__AI = AI
        if(AI == "o"):
            self.__opponent = "x"
        elif(AI == "x"):
            self.__opponent = "o"
        else:
            raise Exception("Symbol not Recongized!")
        
        if(difficult_level <= 0 or difficult_level > 9):
            difficult_level = 4
            print("set_difficult_level=4")
        
        self.__board = np.full((9,), "-")
        self.__is_win = False
        self.__winner = None
        self.__turn = "x"
        self.__difficult_level = difficult_level

    def get(self, num) -> str:
        '''
        get method is getting the cell
        
        :param num: number of cell from [0-9]
        :return: state of cell as string ("-" or "x" or "o")
        '''
        return self.__board[num]
    
    def get_r(self, num) -> str:
        '''
        get_r method is getting the cell that represented in print
        
        :param num: number of cell from [0-9]
        :return: state of cell as string (range[0-9] or "x" or "o").
        '''
        if(self.get(num) == "-"):
            return num
        return self.get(num)
    
    def get_difficult_level(self) -> int:
        '''
        get_difficult_level method is getter method
        
        :return: int
        '''
        return self.__difficult_level
    
    def get_AI(self) -> str:
        '''
        get_AI method getting the computer symbol
        
        :return: string "x" or "o"
        '''
        return self.__AI      
        
    def get_opponent(self) -> str:
        '''
        get_player method getting the player symbol
        
        :return: string "x" or "o"
        '''
        return self.__opponent
    
    def get_successors(self, typ: object = list) -> dict:
        successors = None
        
        if(typ == list):
            successors = np.array([])
            
            for cell_num in range(9):
                if(self.is_empty(cell_num)):
                    successors = np.append(successors, self.make_move(cell_num))
                    
        elif(typ == dict):
            successors = dict()
            for cell_num in range(9):
                if(self.is_empty(cell_num)):
                        successors.update({cell_num: self.make_move(cell_num)})
                        
        return successors
    
    def get_winner(self) -> str:
        '''
        get_winner method is getter method
        
        :return: str
        '''
        return self.__winner
    
    def get_turn(self) -> str:
        '''
        get_turn method getting whos turn now
        
        :return: string "x" or "o"
        '''
        return self.__turn
        
    def get_curr_depth(self) -> int:
        '''
        get_currr_depth method is getting the current depth of game tree
        
        :return: int
        '''
        depth = 0
        for cell_num in range(9):
            if(not self.is_empty(cell_num)):
                depth += 1
                
        return depth - 1
    
    def is_empty(self, cell_num) -> bool:
        '''
        is_empty method make sure the cell is empty
        
        :param num: number of cell from [0-9]
        :return: boolean
        '''
        return self.get(cell_num) == "-"
    
    def is_draw(self) -> bool:
        '''
        is_draw method, check if there is draw in game
        
        :return: boolean
        '''
        evaulation = self.chances_to_win()
        if(evaulation["x"] == 0 and evaulation["o"] == 0):
            return True
        return False
    
    def is_win(self) -> bool:
        '''
        isWin method to check if there are a winner
        
        :return: boolean
        '''
        from Tic_Tac_Toe import Tic_Tac_Toe
        for x1, x2, x3 in Tic_Tac_Toe.WINNER: 
            if(self.get(x1) == self.get(x2) == self.get(x3) != "-"):
                self.__winner = self.get(x1)
                return True
        return False
    
    def is_game_end(self) -> bool:
        '''
        is_game_end method to check if the game end or not
        
        :return: boolean
        '''
        return self.is_win() or self.is_draw()
    
    def alt_turn(self) -> None:
        if(self.get_turn() == "x"):
            self.__turn = "o"
        else:
            self.__turn = "x"
    
    def __set_move(self, cell_num: int):
        if(self.is_empty(cell_num)):
            self.__board[cell_num] = self.get_turn()
            return True
        return False
    
    def make_move(self, cell_num: int):
        '''
        move method play the game with the number of cell
        
        :param num: number of cell [0-9]
        :return: boolean
        '''
        new_state = copy.deepcopy(self)
        if(new_state.__set_move(cell_num)):
            if(new_state.is_game_end()):
                new_state.__is_win = True
                new_state.__winner = new_state.get_winner()
                return new_state
            else:
                new_state.alt_turn()
                return new_state
            
        return None 
    
    def chances_to_win(self) -> tuple:
        '''
        chances_to_win method determine the chances of win for each player
        
        :return: Tuple (player chances to win, opponent chances to win)
        ''' 
        players = {
            "x": 0,
            "o": 0
        }
        from Tic_Tac_Toe import Tic_Tac_Toe
        for player in ["x", "o"]:
            for x1, x2, x3 in Tic_Tac_Toe.WINNER:  
                if(self.get(x1) == self.get(x2) == self.get(x3) == player):
                    players[player] += 8
                
                if((self.is_empty(x1) and self.is_empty(x2) and self.is_empty(x3)) or
                   (self.is_empty(x1) and self.get(x2) == self.get(x3) == player) or
                   (self.get(x1) == self.get(x3) == player and self.is_empty(x2)) or
                   (self.get(x1) == self.get(x2) == player and self.is_empty(x3)) or
                   (self.is_empty(x1) and self.is_empty(x2) and self.get(x3) == player) or 
                   (self.get(x1) == player and self.is_empty(x2) and self.is_empty(x3)) or
                   (self.is_empty(x1) and self.is_empty(x3) and self.get(x2) == player)):
                    players[player] += 1
                 
        return players

    def evaluate(self) -> int:
        '''
        evaluate method "Evaluate Function" that will build the tree with evalution
        
        :return: int (player chances to win - opponent chances to win)
        '''
        evaluation = self.chances_to_win()
        return evaluation[self.get_AI()] - evaluation[self.get_opponent()]
        
    def __str__(self) -> str:
        return f"""Player({self.get_turn()}) Turn:\n| {self.get_r(0)} | {self.get_r(1)} | {self.get_r(2)} |\n| {self.get_r(3)} | {self.get_r(4)} | {self.get_r(5)} |\n| {self.get_r(6)} | {self.get_r(7)} | {self.get_r(8)} |"""
