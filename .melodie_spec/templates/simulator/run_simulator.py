"""
{{project_name}} - Simulator Entry Point (Visual Mode)

This script runs the simulation with the visualizer.
Make sure run_studio.py is running first.
"""
import os
from Melodie import Config, Simulator
from core.model import TemplateModel
from core.scenario import TemplateScenario
from core.visualizer import TemplateVisualizer

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
        scenario_cls=TemplateScenario,
        visualizer_cls=TemplateVisualizer,  # Pass visualizer class here
    )
    
    # Run with visualizer (no arguments!)
    simulator.run_visual()
