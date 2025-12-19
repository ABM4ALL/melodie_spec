from Melodie import Calibrator, Model
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .model import TemplateModel

class TemplateCalibrator(Calibrator):
    """
    Calibrator class for tuning model parameters to match target data.
    Inherits from Melodie.Calibrator.
    """
    def setup(self):
        """
        Configure calibration parameters and properties to record.
        """
        # 1. Register the property in Scenario to be calibrated.
        # This property MUST exist in your Scenario class.
        self.add_scenario_calibrating_property("calibration_param")
        
        # 2. Register environment properties to watch during calibration.
        # These will be saved to output files for analysis.
        self.add_environment_property("target_env_property")

    def distance(self, model: "TemplateModel") -> float:
        """
        Calculate the 'distance' (error) between the model's result and the target.
        The Genetic Algorithm seeks to Minimize this value.
        
        :param model: The model instance after a run.
        :return: A float representing the error (lower is better).
        """
        env = model.environment
        
        # Example: Calculate Squared Error
        # target_value = 0.8  # Define your target here
        # current_value = env.target_env_property
        # return (current_value - target_value) ** 2
        
        return 0.0
