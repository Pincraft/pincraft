from mpf.core.mode import Mode

class Base(Mode):
    

    def mode_init(self):
        print("Gamecontroller init...")
        

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters

        self.add_mode_event_handler('player_add_request', self.gc_checkaddplayer)
       # self.machine.variables.set_machine_var("game_num_players", 1)


        self.add_mode_event_handler('gameselect_Easy_selected', self.gc_modeeasyselected)
        self.add_mode_event_handler('gameselect_Normal_selected', self.gc_modenormalselected)
        self.add_mode_event_handler('gameselect_Hardcore_selected', self.gc_modehardselected)
        self.add_mode_event_handler('gameselect_Competition_selected', self.gc_modecompetitionselected)
        self.add_mode_event_handler('gameselect_COOP_selected', self.gc_modecoopselected)
        self.add_mode_event_handler('gameselect_Story_selected', self.gc_modestoryselected)


        self.add_mode_event_handler('mode_selected', self.gc_modeselected)
        
        self.add_mode_event_handler('player_added', self.gc_playeradded)

    #EASY MODE SELECTED
    def gc_modeeasyselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "EASY")
        self.machine.variables.set_machine_var("game_mode_display", "Easy Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 11)
        self.machine.variables.set_machine_var("difficulty_night", 11)
        self.machine.variables.set_machine_var("difficulty_tools", 4)
        self.machine.variables.set_machine_var("difficulty_extraball1", 6)
        self.machine.variables.set_machine_var("difficulty_extraball2", 6)      

    #NORMAL MODE SELECTED
    def gc_modenormalselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "NORMAL")
        self.machine.variables.set_machine_var("game_mode_display", "Normal Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 21)
        self.machine.variables.set_machine_var("difficulty_night", 76)
        self.machine.variables.set_machine_var("difficulty_tools", 1)
        self.machine.variables.set_machine_var("difficulty_extraball1", 6)
        self.machine.variables.set_machine_var("difficulty_extraball2", 12)
    
    #HARDCORE MODE SELECTED
    def gc_modehardselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "HARDCORE")
        self.machine.variables.set_machine_var("game_mode_display", "Hardcore Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 41)
        self.machine.variables.set_machine_var("difficulty_night", 101)
        self.machine.variables.set_machine_var("difficulty_tools", 1)
        self.machine.variables.set_machine_var("difficulty_extraball1", 12)
        self.machine.variables.set_machine_var("difficulty_extraball2", 12)

    #COMPETITION MODE SELECTED
    def gc_modecompetitionselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "COMPETITION")
        self.machine.variables.set_machine_var("game_mode_display", "Competition Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 41)
        self.machine.variables.set_machine_var("difficulty_night", 101)
        self.machine.variables.set_machine_var("difficulty_tools", 1)
        self.machine.variables.set_machine_var("difficulty_extraball1", 0)
        self.machine.variables.set_machine_var("difficulty_extraball2", 0)

    #COOPERATIVE MODE SELECTED
    def gc_modecoopselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "COOP")
        self.machine.variables.set_machine_var("game_mode_display", "Cooperative Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 21)
        self.machine.variables.set_machine_var("difficulty_night", 76)
        self.machine.variables.set_machine_var("difficulty_tools", 1)
        self.machine.variables.set_machine_var("difficulty_extraball1", 0)
        self.machine.variables.set_machine_var("difficulty_extraball2", 0)

    #STORY MODE SELECTED
    def gc_modestoryselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_mode", "STORY")
        self.machine.variables.set_machine_var("game_mode_display", "Story Mode")
        self.machine.variables.set_machine_var("difficulty_villager", 11)
        self.machine.variables.set_machine_var("difficulty_night", 51)
        self.machine.variables.set_machine_var("difficulty_tools", 4)
        self.machine.variables.set_machine_var("difficulty_extraball1", 0)
        self.machine.variables.set_machine_var("difficulty_extraball2", 0)

    #MODE SELECTED
    def gc_modeselected(self, **kwargs):
        self.machine.variables.set_machine_var("game_num_players", 1) 
        game_mode=self.machine.variables.get_machine_var("game_mode")
        if game_mode=="STORY":
            self.machine.game.balls_per_game=1
        else:
            self.machine.game.balls_per_game=3
        return (True)

    #PLAYER ADDING - Do not allow adding of player if game select screen is active, or certain critera applies
    def gc_checkaddplayer(self, **kwargs):
        game_mode=self.machine.variables.get_machine_var("game_mode")
        if self.machine.mode_controller.is_active("gameselect"):        #Do not allow adding player if selecting screen
            return (False)
        elif game_mode=="EASY":
            return (True)
        elif game_mode=="NORMAL":
            return (True)
        elif game_mode=="HARDCORE":
            return (True)
        elif game_mode=="COMPETITION":
            return (True)
        elif game_mode=="COOP":
            players = self.machine.variables.get_machine_var("game_num_players")
            #DO DIFFERENT THINGS HERE
            if players < 4:
                players += 1
                self.machine.game.balls_per_game=players * 3
                self.machine.variables.set_machine_var("game_num_players", players)
                self.machine.events.post("coop_player_added", callback=None, **kwargs)
            return (False)
        elif game_mode=="STORY":
            return (False)
        else: #ERROR
            return (True)

    #PLAYER ADDED - When a new player is added, make sure mode is applied to their profile.
    def gc_playeradded(self, **kwargs):
        # Set Game Mode for Newly Added Players
        #player = kwargs['player']
        #player.game_mode = self.machine.variables.get_machine_var("game_mode")
        self.machine.variables.set_machine_var("game_num_players", self.machine.game.num_players)
        return (True)

    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("Game Controller Stopping")

