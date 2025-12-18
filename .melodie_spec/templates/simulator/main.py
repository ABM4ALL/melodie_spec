import os
from Melodie import Config, Simulator
from core.model import TemplateModel
from core.scenario import TemplateScenario

if __name__ == "__main__":
    config = Config(
        project_name="{{project_name}}",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
    )
    simulator = Simulator(
        config=config,
        model_cls=TemplateModel,
        scenario_cls=TemplateScenario
    )
    
    # Run serially
    simulator.run()
    
    # Run in parallel (Process-based) - Recommended for most cases
    # simulator.run_parallel(cores=4)
    
    # Run in parallel (Thread-based) - Recommended for Python 3.13+ (No-GIL)
    # simulator.run_parallel_multithread(cores=4)
