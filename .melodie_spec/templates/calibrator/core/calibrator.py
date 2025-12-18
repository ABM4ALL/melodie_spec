from Melodie import Calibrator
from .model import TemplateModel

class TemplateCalibrator(Calibrator):
    def setup(self):
        self.add_scenario_calibrating_property("calibration_param")
        self.add_environment_property("target_env_property")

    def distance(self, model: TemplateModel) -> float:
        env = model.environment
        # Example distance calculation
        return (env.target_property - 0.5) ** 2
