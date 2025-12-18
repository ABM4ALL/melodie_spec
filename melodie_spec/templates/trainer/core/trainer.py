from Melodie import Trainer
from .agent import TemplateAgent

class TemplateTrainer(Trainer):
    def setup(self):
        self.add_agent_training_property("agent_list", ["strategy_param"], lambda scenario: list(range(scenario.agent_num)))

    def collect_data(self):
        self.add_agent_property("agent_list", "strategy_param")
        self.add_environment_property("total_payoff")

    def utility(self, agent: TemplateAgent) -> float:
        return agent.accumulated_payoff
