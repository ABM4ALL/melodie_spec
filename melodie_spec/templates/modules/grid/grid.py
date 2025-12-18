from Melodie import Grid, Spot

class TemplateGrid(Grid):
    def setup(self):
        self.set_spot_property("is_blocked", 0)
