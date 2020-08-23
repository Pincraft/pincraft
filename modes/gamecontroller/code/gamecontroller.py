from mpf.core.mode import Mode

class Base(Mode):
    def mode_init(self):
        print("My custom gamecontroller code is being initialized")

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters


        self.add_mode_event_handler('player_add_request', self.checkaddplayer)

    def checkaddplayer(self, **kwargs):
        if self.machine.mode_controller.is_active("gameselect"):
            return (False)
        else:
            return (True)



    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("Game Controller Stopping")