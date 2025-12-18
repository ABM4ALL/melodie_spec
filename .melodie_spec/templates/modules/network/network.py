from Melodie import Network, Edge

class TemplateNetwork(Network):
    def setup(self):
        self.edge_cls = Edge
