from mpf.core.mode import Mode

class Base(Mode):
    def mode_init(self):
        print("My custom divertercontrol code is being initialized")

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters

        #print("My custom mode code is starting")

        # call a delay in 5 seconds
        #self.delay.add(5000, self.my_callback)


        # what player are we?
        #print(self.player.number)

        # what's the player's score?
        #print('Score: {}'.format(self.player.score))
        self.player.diverter_state = "start"
        self.add_mode_event_handler('divertercontrol_checkworldstate', self.checkdiverterstate)

        # turn LED "led01" red
        #self.machine.leds.led01.color('red')

    def checkdiverterstate(self, **kwargs):
        oldstate = self.player.diverter_state
        #MULTIBALLS
        if self.machine.mode_controller.is_active("villagermb") or self.machine.mode_controller.is_active("night"):
            if self.player.crafting_full == 1:
                self.player.diverter_state="multiballhelpertools"
            else:
                self.player.diverter_state="multiballhelpernotools"    
        elif self.machine.mode_controller.is_active("nether"):
            self.player.diverter_state="multiballnether"
        elif self.machine.mode_controller.is_active("stronghold"):
            if (self.player.stronghold_progress == 4 and self.player.multiplier_mb == 1):
                self.player.diverter_state="strongholdtravel"
            else:
                self.player.diverter_state="strongholdidle"    
        elif self.machine.mode_controller.is_active("theend"):
            if self.machine.state_machines.statemachine_theend.state == "state_prepare":
                self.player.diverter_state="theendprepare"
            elif self.machine.state_machines.statemachine_theend.state  == "state_battle":
                self.player.diverter_state="theendbattle"
            elif self.machine.state_machines.statemachine_theend.state  == "state_victory":
                self.player.diverter_state="theendvictory"
            elif self.machine.state_machines.statemachine_theend.state  == "state_travel":
                self.player.diverter_state="theendtravel"
            else:
                self.player.diverter_state="theendunknown"
        #WORLD TRAVEL
        elif self.machine.mode_controller.is_active("travelready"):
            self.player.diverter_state="worldtravel"
        #NIGHT AND VILLAGER MULTIBALLS
        elif self.player.villagermb_ready == 1 and self.player.nightmb_ready==1:
            if self.machine.multiball_locks.nightvillagerlock1.locked_balls==1:
                self.player.diverter_state="worldnightvillagersidelock"
            else:
                self.player.diverter_state="worldnightvillagertoplock"
        elif self.player.villagermb_ready == 1:
            self.player.diverter_state="worldvillager"
        elif self.player.nightmb_ready==1:
            self.player.diverter_state="worldnight"
        #TOOLS
        elif self.player.crafting_full == 1:
            self.player.diverter_state="worldtoolsfull"
        elif self.player.crafting_enabled == 1:
            self.player.diverter_state="worldtools"
        #IDLE
        else:
            self.player.diverter_state="worldidle"

        if oldstate != self.player.diverter_state:
            self.machine.events.post("divertercontrol_statechanged", callback=None, **kwargs)


    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("My custom mode code is stopping")