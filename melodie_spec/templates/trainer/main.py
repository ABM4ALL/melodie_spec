from Melodie import Config
from core.trainer import TemplateTrainer
from core.model import TemplateModel
from core.scenario import TemplateScenario

if __name__ == "__main__":
    config = Config(
        project_name="TrainerTemplate",
        project_root=".",
        input_folder="data/input",
        output_folder="data/output",
    )

    trainer = TemplateTrainer(
        config=config,
        scenario_cls=TemplateScenario,
        model_cls=TemplateModel,
        processors=4,
        parallel_mode="process",
    )
    trainer.run()
