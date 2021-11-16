import json

class Analyzer():

    def __init__(self, probabilities, threshold, path):
        self.probabilities = probabilities
        self.threshold = threshold
        self.path = path

    
    def get_best_result(self):
        return max(self.probabilities)
    
    def get_results(self):
        result = self.probabilities.index(self.get_best_result())
        return result

    def read_classes(self):
        file = open(self.path,)
        json_classes = json.load(file)

        result = json_classes[f'{self.get_results()}']

        return result
