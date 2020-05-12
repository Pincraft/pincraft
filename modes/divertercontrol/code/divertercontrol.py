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
        if self.machine.mode_controller.is_active("villagermb"):
            self.player.diverter_state="multiballvillager"
        elif self.machine.mode_controller.is_active("night"):
            self.player.diverter_state="multiballnight"
        elif self.machine.mode_controller.is_active("stronghold"):
            self.player.diverter_state="stronghold"
        elif self.machine.mode_controller.is_active("theend"):
            self.player.diverter_state="theend"
        elif self.player.travel_enabled==1:
            self.player.diverter_state="worldtravel"
        elif self.player.villagermb_ready == 1:
            self.player.diverter_state="worldvillager"
        elif self.player.crafting_full == 1:
            self.player.diverter_state="worldtoolsfull"
        elif self.player.crafting_enabled == 1:
            self.player.diverter_state="worldtools"
        else:
            self.player.diverter_state="worldidle"

        if oldstate != self.player.diverter_state:
            self.machine.events.post("divertercontrol_statechanged", callback=None, **kwargs)


    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("My custom mode code is stopping")