from mpf.core.mode import Mode
from math import modf 

class World1(Mode):
    def mode_init(self):
        print("My custom mode code is being initialized")

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters
        #self.add_mode_event_handler('s_spinner_active', self.spinner_shot_handler)
        #self.add_mode_event_handler('s_s_collectitem1_active', self.collectitem1_handler)
        #self.machine.switches.s_spinner.add_handler('spinner_shot',1)
        #spinner = self.machine.switches.s_spinner
        # spinner.add_handler(self.spinner_shot_handler, 1, 0, False, None)
        print("World 1 being initialized")


        self.machine.lights['l_collectitem5'].color('white',0,0,'item') 
        self.machine.lights['l_collectitem4'].color('white',0) 
        self.machine.lights['l_collectitem5'].on(255) 
    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("My custom mode code is stopping")
    