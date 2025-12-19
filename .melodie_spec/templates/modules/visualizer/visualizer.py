from Melodie import Visualizer
from typing import TYPE_CHECKING
# Optional: Import FloatParam for interactive parameters
# from MelodieInfra.lowcode.params import FloatParam

if TYPE_CHECKING:
    from .model import TemplateModel


class TemplateVisualizer(Visualizer):
    """
    Visualizer class for MelodieStudio.
    Defines charts, grid/network views, and interactive parameters.
    """
    model: "TemplateModel"

    def set_model(self, model: "TemplateModel"):
        """
        Called when the visualizer is bound to a model instance.
        Set grid/network dimensions here if needed.
        """
        super().set_model(model)
        # For Grid models:
        # self.width = model.grid.width()
        # self.height = model.grid.height()

    def setup(self):
        """
        Configure charts, grid/network views, and interactive parameters.
        """
        # --- Line Chart ---
        # self.plot_charts.add_line_chart("chart_name").set_data_source({
        #     "Series1": lambda: self.model.environment.property1,
        #     "Series2": lambda: self.model.environment.property2,
        # })

        # --- Grid Visualization ---
        # self.add_grid(
        #     name="grid_name",
        #     grid_getter=lambda: self.model.grid,
        #     var_getter=lambda agent: agent.state,  # Dynamic state for coloring
        #     var_style={
        #         0: {"label": "Type A", "color": "#0000FF"},
        #         1: {"label": "Type B", "color": "#FF0000"},
        #     },
        #     update_spots=False
        # )

        # --- Network Visualization ---
        # self.add_network(
        #     "network_name",
        #     lambda: self.model.network,
        #     {0: {"label": "S", "color": "#22c55e"}, 1: {"label": "I", "color": "#ef4444"}},
        #     lambda agent: agent.state,
        # )

        # --- Interactive Parameters (optional) ---
        # self.params_manager.add_param(
        #     FloatParam(
        #         name="param_name",
        #         value_range=(0.0, 1.0),
        #         step=0.01,
        #         getter=lambda scenario: scenario.param_name,
        #         setter=lambda scenario, val: setattr(scenario, "param_name", val),
        #         label="Parameter Label",
        #         description="Description of the parameter.",
        #     )
        # )
        pass
