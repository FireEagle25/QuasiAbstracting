from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml import NetworkWriter, NetworkReader
from pybrain.tools.shortcuts import buildNetwork


class Net:
    inputs_count = 5
    hidden_layers_count = 4
    outputs_count = 1

    @staticmethod
    def create_from_file(filename):
        return Net(NetworkReader.readFrom(filename))

    def __init__(self, net=None):
        self.net = net

    def _init_net(self):
        self.net = buildNetwork(Net.inputs_count, Net.hidden_layers_count, Net.outputs_count)
        self.net.activate([Net.inputs_count, Net.outputs_count])

    def train(self, dataset):
        if not self.net:
            self._init_net()

        supervised_dataset = SupervisedDataSet(Net.inputs_count, Net.outputs_count)

        for row in dataset:
            supervised_dataset.addSample(row[0], row[1])

        trainer = BackpropTrainer(self.net, supervised_dataset)
        trainer.trainUntilConvergence()

    def save_to_file(self, filename):
        NetworkWriter.writeToFile(self.net, filename)

    def print(self):
        for mod in self.net.modules:
            print("Module:", mod.name)
            if mod.paramdim > 0:
                print("--parameters:", mod.params)
            for conn in self.net.connections[mod]:
                print("-connection to", conn.outmod.name)
                if conn.paramdim > 0:
                    print("- parameters", conn.params)
            if hasattr(self.net, "recurrentConns"):
                print("Recurrent connections")
                for conn in self.net.recurrentConns:
                    print("-", conn.inmod.name, " to", conn.outmod.name)
                    if conn.paramdim > 0:
                        print("- parameters", conn.params)
