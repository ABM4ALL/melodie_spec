from Melodie import Grid, Spot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .scenario import TemplateScenario


class TemplateSpot(Spot):
    """
    Represents a single cell on the grid.
    Add custom properties that affect agent behavior here.
    """
    def setup(self):
        # Example: Add custom spot properties
        # self.stay_prob: float = 0.0
        pass


class TemplateGrid(Grid):
    """
    Manages the 2D space, spots, and agent positions.
    """
    scenario: "TemplateScenario"

    def setup(self):
        """
        Configure the grid.
        Apply property matrices loaded from scenario to spots if needed.
        """
        # Example: Apply a 2D matrix to spot properties
        # self.set_spot_property("stay_prob", self.scenario.stay_prob_matrix)
        pass
