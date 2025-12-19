"""
{{project_name}} - Studio Entry Point

This script starts the Melodie Studio web server for the visualizer.
Run this first, then run run_simulator.py to start the simulation.
"""
import os
from Melodie import Config
from MelodieStudio.main import studio_main

if __name__ == "__main__":
    config = Config(
        project_name="{{project_name}}",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
        visualizer_entry="run_simulator.py",
    )
    studio_main(config)
