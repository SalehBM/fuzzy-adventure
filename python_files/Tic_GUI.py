import tkinter as tk

from Tic_Tac_Toe import Tic_Tac_Toe

class Tic_GUI(tk.Tk):
    window_size = (640, 600)
    rectangle_tic_tac = (320, 320)
    window_background = "#1a2a33"
    secondary_color = "#1f3641"
    element_color = "#31c3bd"
    secondary_elment_color = "#f2b137"
    text_color = "#a8bfc9"

    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe Project")
        self.geometry(f'{Tic_GUI.window_size[0]}x{Tic_GUI.window_size[1]}')
        self.configure(bg=Tic_GUI.window_background)

        self.char_x = tk.PhotoImage(file='./python/images/icon-x.png')
        self.char_o = tk.PhotoImage(file='./python/images/icon-o.png')
        self.empty = tk.PhotoImage()

        self.initial()

    def initial(self):
        self.__user = "x"
        self.__AI = "o"
        self.__difficult_level = 4

        self.__VS_AI = True
        self.create_control_panel()

        self.__game = None
        self.__algorithm = "MinMax"

    def game(self):
        return self.__game

    def get_user(self):
        return self.__user

    def get_AI(self):
        return self.__AI

    def get_difficult(self):
        return self.__difficult_level
    
    def get_is_vsAI(self):
        return self.__VS_AI

    def get_algorithm(self):
        return self.__algorithm

    def set_user(self, symbol):
        if(symbol == "x"):
            self.__AI = "o"
            self.__user = "x" 
        else:
            self.__AI = "x"
            self.__user = "o"

    def set_difficult(self, difficult):
        self.__difficult_level = difficult

    def vs_AI(self, vs_AI: bool):
        self.__VS_AI = vs_AI

    def select(self, element):
        element.config(bg= Tic_GUI.text_color,
                        fg= Tic_GUI.window_background)
        
    def deselect(self, element):
        element.config(bg= Tic_GUI.window_background,
                        fg= Tic_GUI.text_color)

    def update_depth(self):
        self.depth_label.config(text= f"Current Depth: {self.game().get_state().get_curr_depth()}")

    def update_tree_size(self):
        tree_size = 0
        if(self.get_algorithm() == "MinMax"):
            from Min_Max import Min_Max
            tree_size = Min_Max.Expanded_Nodes
        else:
            from Alpha_Beta_Pruning import Alpha_Beta_Pruning
            tree_size = Alpha_Beta_Pruning.Expanded_Nodes

        self.states_label.config(text= f"Tree size: {tree_size}")

    def X_button_event(self):
        self.select(self.x_button)
        self.deselect(self.o_button)
        self.set_user("x")

    def O_button_event(self):
        self.select(self.o_button)
        self.deselect(self.x_button)
        self.set_user("o")

    def difficult_event(self, difficult):
        self.select(self.difficult_buttons[difficult - 1])

        for i in range(9):
            if(i != difficult - 1):
                self.deselect(self.difficult_buttons[i])

        self.set_difficult(difficult= difficult)

    def difficult_1_event(self):
        self.difficult_event(1)

    def difficult_2_event(self):
        self.difficult_event(2)

    def difficult_3_event(self):
        self.difficult_event(3)

    def difficult_4_event(self):
        self.difficult_event(4)

    def difficult_5_event(self):
        self.difficult_event(5)

    def difficult_6_event(self):
        self.difficult_event(6)

    def difficult_7_event(self):
        self.difficult_event(7)

    def difficult_8_event(self):
        self.difficult_event(8)

    def difficult_9_event(self):
        self.difficult_event(9)

    def vs_AI_event(self):
        self.vs_AI(True)
    
    def vs_player_event(self):
        self.vs_AI(False)
    
    def cell_wining_event(self, cells):
        color = None
        if (self.game().get_state().get(cells[0]) == "x"):
            color = Tic_GUI.element_color
        else:
            color = Tic_GUI.secondary_elment_color

        for i in range(3):
            self.cells[cells[i]].config(bg= color)

    def define_winner_cells(self):
        from Tic_Tac_Toe import Tic_Tac_Toe
        for x1, x2, x3 in Tic_Tac_Toe.WINNER: 
            if(self.game().get_state().get(x1) == self.game().get_state().get(x2) == self.game().get_state().get(x3) != "-"):
                self.cell_wining_event([x1, x2, x3])
        return False

    def game_end_event(self):
        self.define_winner_cells()
        self.winner_frame = tk.Frame(self.game_frame, 
                                    bg= Tic_GUI.secondary_color,
                                    )
        self.winner_frame.grid(row= 4, column=0,
                                rowspan= 10, columnspan= 15)


        self.winner_label = tk.Label(self.winner_frame,
                                        text= "You Win",
                                        bg= Tic_GUI.secondary_color,
                                        fg= Tic_GUI.text_color)
        self.winner_label.config(font=("", 18, "bold"))
        self.winner_label.grid(row= 6, column= 0, columnspan= 15, padx = 125, pady= 10)

        self.winner_label_2 = tk.Label(self.winner_frame,
                                        text= "X TAKES THE ROUND",
                                        bg= Tic_GUI.secondary_color,
                                        fg= Tic_GUI.text_color)
        self.winner_label_2.config(font=("", 18, "bold"))
        self.winner_label_2.grid(row= 8, column= 0, columnspan= 15, pady= 20)

        self.quit_button = tk.Button(self.winner_frame,
                                    text="Quit",
                                    bg= Tic_GUI.text_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 12,
                                    command= lambda: self.destroy())
        self.quit_button.config(font=("", 16, "bold"))
        self.quit_button.grid(row= 10,
                        column=0,
                        columnspan= 5,
                        pady= 10,
                        padx= 20)

        self.next_button = tk.Button(self.winner_frame,
                                    text="Next Round",
                                    bg= Tic_GUI.secondary_elment_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 12,
                                    command=self.restart_event)
        self.next_button.config(font=("", 16, "bold"))
        self.next_button.grid(row= 10,
                        column=6,
                        columnspan= 5,
                        pady= 40,
                        padx= 20)

        winner = self.game().get_winner()
        if(winner == None):
            self.winner_label.config(text= "DRAW!")
            self.winner_label_2.config(text= f"NO ONE TAKE THE ROUND",
                                        fg= [Tic_GUI.element_color, Tic_GUI.secondary_elment_color][self.get_AI() == "x"])

        elif(self.game().get_winner()[0] == self.get_AI()):
            self.winner_label.config(text= "You Lose!")
            self.winner_label_2.config(text= f"{self.get_AI().capitalize()} TAKE THE ROUND",
                                        fg= [Tic_GUI.element_color, Tic_GUI.secondary_elment_color][self.get_AI() == "x"])
        else:
            self.winner_label.config(text= "You Win!")
            self.winner_label_2.config(text= f"{self.get_user().capitalize()} TAKE THE ROUND",
                                    fg= [Tic_GUI.element_color, Tic_GUI.secondary_elment_color][self.get_AI() == "x"])     

    def best_move(self):
        if(self.get_algorithm() == "MinMax"):
            from Min_Max import Min_Max
            move = Min_Max.min_max(self.game().get_state())
        else:
            from Alpha_Beta_Pruning import Alpha_Beta_Pruning
            move = Alpha_Beta_Pruning.min_max(self.game().get_state())
        
        return move

    def start_game(self):
        if(self.game().get_state().is_game_end()):
            return

        if(self.get_AI() == self.game().get_state().get_turn()):
            move = self.best_move()
            self.cell_event(move)

    def cell_event(self, cell):
        if(self.game().get_state().get_turn() == "x"):
            self.cells[cell].config(width = 110, height = 80,
                                    image= self.char_x)
        else:
            self.cells[cell].config(width = 110, height = 80, 
                                    image= self.char_o)
        
        if(not self.game().make_move(cell)):
            self.restart_event()

        if(self.game().get_state().is_game_end()):
            self.game_end_event()

        elif(self.get_is_vsAI() and self.get_AI() == self.game().get_state().get_turn()):
            cell = self.best_move()
            self.cell_event(cell)

        self.now_turn.config(text= f"{str.upper(self.game().get_state().get_turn())} Turn")
        self.update_depth()
        self.update_tree_size()

    def cell_0_event(self):
        self.cell_event(0)

    def cell_1_event(self):
        self.cell_event(1)

    def cell_2_event(self):
        self.cell_event(2)

    def cell_3_event(self):
        self.cell_event(3)

    def cell_4_event(self):
        self.cell_event(4)

    def cell_5_event(self):
        self.cell_event(5)

    def cell_6_event(self):
        self.cell_event(6)

    def cell_7_event(self):
        self.cell_event(7)

    def cell_8_event(self):
        self.cell_event(8)

    def minmax_event(self):
        self.select(self.minmax_button)
        self.deselect(self.alphabeta_btn)
        self.__algorithm = "MinMax"

    def alphabeta_event(self):
        self.select(self.alphabeta_btn)
        self.deselect(self.minmax_button)
        self.__algorithm = "Alphabeta"

    def create_control_panel(self):
        self.control_frame = tk.Frame(bg= Tic_GUI.secondary_color)
        self.control_frame.pack(side= tk.TOP,
                                padx= 10,
                                pady= 20)
        
        self.chooseLabel = tk.Label(self.control_frame,
                                        text="PICK PLAYER 1’S MARK",
                                        bg= Tic_GUI.secondary_color,
                                        fg= Tic_GUI.text_color)
        self.chooseLabel.config(font=("", 14, "bold"))
        self.chooseLabel.grid(row=0,
                            column= 0,
                            columnspan= 10,
                            pady=25)

        self.x_button = tk.Button(self.control_frame,
                                    text="X",
                                    bg= Tic_GUI.text_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 12,
                                    command=self.X_button_event)
        self.x_button.config(font=("", 18, "bold"))
        self.x_button.grid(row= 1,
                        column=0,
                        columnspan= 5,
                        pady= 10,
                        padx= 20)

        self.o_button = tk.Button(self.control_frame,
                                    text="O",
                                    bg= Tic_GUI.window_background,
                                    fg= Tic_GUI.text_color,
                                    borderwidth= 0,
                                    width= 12,
                                    command=self.O_button_event)
        self.o_button.config(font=("", 18, "bold"))
        self.o_button.grid(row= 1,
                            column=4,
                            columnspan= 5,
                            pady = 10,
                            padx= 20)

        self.note = tk.Label(self.control_frame,
                                    text= "Remember X Starts First.",
                                    bg= Tic_GUI.secondary_color,
                                    fg= Tic_GUI.text_color)
        self.note.config(font=("", 12))
        self.note.grid(row=2,
                        column= 0,
                        columnspan= 10)

        self.minmax_button = tk.Button(self.control_frame,
                                    text="MinMax",
                                    bg= Tic_GUI.text_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 15, height= 2,
                                    command=self.minmax_event)
        self.minmax_button.config(font=("", 14, "bold"))
        self.minmax_button.grid(row= 3,
                        column=0,
                        columnspan= 5,
                        pady= 20,
                        padx= 20)

        self.alphabeta_btn = tk.Button(self.control_frame,
                                    text="Alpha Beta Pruning",
                                    bg= Tic_GUI.window_background,
                                    fg= Tic_GUI.text_color,
                                    borderwidth= 0,
                                    width= 15, height= 2,
                                    command= self.alphabeta_event)
        self.alphabeta_btn.config(font=("", 14, "bold"))
        self.alphabeta_btn.grid(row= 3,
                            column=4,
                            columnspan= 5,
                            pady = 10,
                            padx= 10)
        
        self.difficult_label = tk.Label(self.control_frame,
                                        text="Difficult Level",
                                        bg= Tic_GUI.secondary_color,
                                        fg= Tic_GUI.text_color)
        self.difficult_label.config(font=("", 14, "bold"))
        self.difficult_label.grid(row=4,
                            column= 0,
                            columnspan= 10,
                            pady=10)
        
        self.difficult_buttons = []
        for i in range(9):
            self.difficult_buttons.append(tk.Button(self.control_frame,
                                    text=i + 1,
                                    bg= Tic_GUI.window_background,
                                    fg= Tic_GUI.text_color,
                                    borderwidth= 0,
                                    width=4,
                                    command= getattr(self, f"difficult_{i+1}_event")))
            self.difficult_buttons[i].config(font=("", 12, "bold"))
            self.difficult_buttons[i].grid(row= 5,
                                            column=i,
                                            padx = 5,
                                            pady = 15)
        self.select(self.difficult_buttons[self.get_difficult() - 1])

        self.vs_AI_button = tk.Button(self.control_frame,
                                    text="New Game (VS AI)",
                                    bg= Tic_GUI.secondary_elment_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 40,
                                    height= 2,
                                    command= lambda: self.create_game(VS_AI= True))
        self.vs_AI_button.config(font=("Comic Sans MS", 14, "bold"))
        self.vs_AI_button.grid(row= 6,
                                column=0,
                                columnspan = 10,
                                padx = 10,
                                pady = 15)

        self.vs_player_button = tk.Button(self.control_frame,
                                    text="New Game (VS Player)",
                                    bg= Tic_GUI.element_color,
                                    fg= Tic_GUI.window_background,
                                    borderwidth= 0,
                                    width= 40,
                                    height= 2,
                                    command= lambda: self.create_game(VS_AI= False))
        self.vs_player_button.config(font=("Comic Sans MS", 14, "bold"))
        self.vs_player_button.grid(row= 7,
                                    column=0,
                                    columnspan = 10,
                                    padx = 10,
                                    pady = 15)

    def destroy_control_panel(self):
        self.control_frame.destroy()

    def create_game(self, VS_AI: bool = True):
        self.__game = Tic_Tac_Toe(AI=str.lower(self.get_AI()), difficult_level= self.get_difficult())
        self.destroy_control_panel()
        if(VS_AI):
            self.vs_AI(vs_AI= True)
        else:
            self.vs_AI(vs_AI= False)

        self.game_frame = tk.Frame(bg= Tic_GUI.window_background)
        self.game_frame.pack(side= tk.TOP,
                                padx= 10,
                                pady= 20)

        self.char_x_small = tk.PhotoImage(file='./python/images/icon-x-small.png')
        self.char_o_small = tk.PhotoImage(file='./python/images/icon-o-small.png')

        self.states_label = tk.Label(self.game_frame, 
                                    text= "Tree size: 0",
                                    bg= Tic_GUI.window_background,
                                    fg= Tic_GUI.text_color)
        self.states_label.config(font=("", 12, "bold"))
        self.states_label.grid(row= 0, column=0,
                            columnspan= 3, rowspan= 3,
                            pady= 20)
        
        self.depth_label = tk.Label(self.game_frame, 
                                    text= "Current Depth: 0",
                                    bg= Tic_GUI.window_background,
                                    fg= Tic_GUI.text_color)
        self.depth_label.config(font=("", 12, "bold"))
        self.depth_label.grid(row= 0, column=5,
                                columnspan= 5, rowspan= 3)

        self.x_image = tk.Label(self.game_frame, highlightthickness=1,
                                width=30, height=30, bg= Tic_GUI.window_background,
                                image=self.char_x_small)
        self.x_image.grid(row = 5, column= 0, columnspan= 1,
                        padx= 5, pady= 30)

        self.x_image = tk.Label(self.game_frame, highlightthickness=1,
                                width=30, height=30, bg= Tic_GUI.window_background,
                                image=self.char_o_small)
        self.x_image.grid(row = 5, column= 1, columnspan= 1,
                        padx= 5, pady= 10)
        
        self.now_turn = tk.Label(self.game_frame,
                                text= "X TURN",
                                width=10, height= 2,
                                highlightthickness= 2,
                                highlightbackground= "#000",
                                bg= Tic_GUI.secondary_color,
                                fg= Tic_GUI.text_color)
        self.now_turn.config(font=("", 12, "bold"))
        self.now_turn.grid(row= 5, column= 3, columnspan= 3)

        self.restart_img = tk.PhotoImage(file='./python/images/restart.png')
        self.Restart = tk.Button(self.game_frame,
                                width=30, height= 30,
                                highlightthickness= 2,
                                highlightbackground= "#000",
                                bg= Tic_GUI.text_color,
                                image= self.restart_img,
                                command= self.restart_event)
        self.Restart.grid(row= 5, column= 8, columnspan= 1)

        self.cells = []
        counter = 0
        for i in range(3):
            for j in range(3):
                self.cells.append(tk.Button(self.game_frame, 
                                            bg= Tic_GUI.secondary_color,
                                            width= 15, height= 5,
                                            command= getattr(self, f"cell_{counter}_event")))
                self.cells[counter].grid(row = (3 * i) + 7, column = (j) * 3, columnspan = 3, rowspan = 3,
                                    padx = 10, pady = 10)
                counter += 1
        self.start_game()

    def restart_event(self):
        self.destroy()
        self.__init__()

window = Tic_GUI()
window.mainloop()