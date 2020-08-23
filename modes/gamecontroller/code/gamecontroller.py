from mpf.core.mode import Mode

class Base(Mode):
    def mode_init(self):
        print("Gamecontroller init...")

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters

        self.add_mode_event_handler('player_add_request', self.gc_checkaddplayer)
        self.add_mode_event_handler('mode_selected', self.gc_modeselected)
        
        self.add_mode_event_handler('player_added', self.gc_playeradded)

    #MODE SELECTED - Mode is Selected, Set Required Functionality
    def gc_modeselected(self, **kwargs):
        if self.player.game_mode=="STORY":
            #Need to turn on endless ball save as well
            self.machine.game.balls_per_game==1
        else:
            self.machine.game.balls_per_game==3

    #PLAYER ADDING - Do not allow adding of player if game select screen is active, or certain critera applies
    def gc_checkaddplayer(self, **kwargs):
        if self.machine.mode_controller.is_active("gameselect"):
            return (False)
        elif self.player.game_mode=="STORY":
            return (False)
        elif self.player.game_mode=="COOP":
            #DO DIFFERENT THINGS HERE
            if self.machine.game.balls_per_game < 12:
                self.machine.game.balls_per_game+=3
            return (False)
        else:
            return (True)

    #PLAYER ADDED - When a new player is added, make sure mode is applied to their profile.
    def gc_playeradded(self, **kwargs):
        # Set Game Mode for Newly Added Players
        #kwargs['player'].game_mode = self.player[1].game_mode
        return (True)

    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("Game Controller Stopping")