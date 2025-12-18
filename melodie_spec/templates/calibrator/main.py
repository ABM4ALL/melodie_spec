from Melodie import Config
from core.calibrator import TemplateCalibrator
from core.model import TemplateModel
from core.scenario import TemplateScenario

if __name__ == "__main__":
    config = Config(
        project_name="CalibratorTemplate",
        project_root=".",
        input_folder="data/input",
        output_folder="data/output",
    )
    
    calibrator = TemplateCalibrator(
        config=config,
        scenario_cls=TemplateScenario,
        model_cls=TemplateModel,
        processors=4, # Number of parallel processors
        parallel_mode="process", # "process" or "thread"
    )
    calibrator.run()
