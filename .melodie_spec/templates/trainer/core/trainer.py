from Melodie import Trainer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .agent import TemplateAgent
    from .scenario import TemplateScenario

class TemplateTrainer(Trainer):
    """
    Trainer class for evolving agent strategies using Genetic Algorithms.
    Inherits from Melodie.Trainer.
    """
    def setup(self):
        """
        Configure the training process: which agents to train and which parameters to evolve.
        """
        # 1. Register agent properties to be trained.
        # - "agent_list_name": Name of the agent list in Model (e.g., "agents").
        # - ["param1", "param2"]: List of parameter names on the Agent to evolve.
        # - agent_ids_getter: Function returning list of agent IDs to train.
        self.add_agent_training_property(
            "agent_list", 
            ["strategy_param"], 
            lambda scenario: list(range(scenario.agent_num))
        )

    def collect_data(self):
        """
        Specify which data to save during the training process.
        Useful for analyzing how strategies evolve over generations.
        """
        self.add_agent_property("agent_list", "strategy_param")
        self.add_environment_property("total_payoff")

    def utility(self, agent: "TemplateAgent") -> float:
        """
        Calculate the 'utility' (fitness) of an agent.
        The Genetic Algorithm seeks to Maximize this value.
        
        :param agent: The agent instance after a run.
        :return: A float representing the agent's performance.
        """
        # Example: Return the agent's accumulated payoff
        # return agent.accumulated_payoff
        return 0.0
