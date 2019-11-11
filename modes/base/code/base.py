from mpf.core.mode import Mode
from math import modf 

class Base(Mode):
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
    def spinner_shot_handler(self, **kwargs):
        hourofday = self.player["hourofday"]

        if hourofday != 20:
            #hourofday += 1 #.50
            self.player["score"] += 1000
           # self.player["hourofday"] = hourofday
           
            hoursplit = modf(hourofday)
            hours = int(hoursplit[1])
            minutes = "00"
            time = ""

            if hoursplit[0] == .25:
                minutes = "15"
            elif  hoursplit[0] == .50:
                minutes = "30"
            elif  hoursplit[0] == .75:
                minutes = "45"

            if hoursplit[1] > 12:
                time = str(hours-12) + ":" + minutes + " PM"
            else:
                time = str(hours) + ":" + minutes + " AM"
                pass

            self.player["time"] = time

            #if hourofday == 20:
                #self.machine.modes.night.start()
        else:
            time = "NIGHT"


        #print("Spinner Hit")
    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("My custom mode code is stopping")
    