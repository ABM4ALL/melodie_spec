import os
from Melodie import Config
from core.trainer import TemplateTrainer
from core.model import TemplateModel
from core.scenario import TemplateScenario

if __name__ == "__main__":
    config = Config(
        project_name="{{project_name}}",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
    )
    
    trainer = TemplateTrainer(
        config=config,
        model_cls=TemplateModel,
        scenario_cls=TemplateScenario,
        # Number of parallel processors
        processors=1,
        # Parallel Mode: "process" (Recommended) or "thread" (Python 3.13+)
        parallel_mode="process"
    )
    
    trainer.run()
