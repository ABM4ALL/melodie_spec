
from Melodie import Model
from .agent import TemplateAgent
from .environment import TemplateEnvironment
from .data_collector import TemplateDataCollector
from .scenario import TemplateScenario

class TemplateModel(Model):
    def create(self):
        """
        The `create` method is used to instantiate the components of the model,
        including agent lists, environment, and data collector.
        """
        # Create agent lists. 
        # You can create multiple agent lists if needed, e.g., self.agents_group1, self.agents_group2
        self.agent_list = self.create_agent_list(TemplateAgent)
        
        # Create environment
        self.environment = self.create_environment(TemplateEnvironment)
        
        # Create data collector
        self.data_collector = self.create_data_collector(TemplateDataCollector)
        
        # Create Grid or Network if necessary
        # self.grid = self.create_grid(TemplateGrid, Spot)
        # self.network = self.create_network()

    def setup(self):
        """
        The `setup` method is used to initialize the parameters of agents and the environment.
        This is where you pass the initialization data from the scenario (e.g., self.scenario.agent_params_df) to the agents.
        """
        # Setup agents with parameters from the scenario
        # Example: self.agent_list.setup_agents(agents_num=self.scenario.agent_num, params_df=self.scenario.agent_params_df)
        self.agent_list.setup_agents(agents_num=self.scenario.agent_num)
        
        # Setup grid/network if they exist
        # self.grid.setup_grid()
        # self.grid.setup_agent_locations(self.agent_list)

    def run(self):
        for t in range(self.scenario.periods):
            self.environment.step()
            self.data_collector.collect(t)
