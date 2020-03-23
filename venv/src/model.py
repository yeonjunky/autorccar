import cv2
import numpy
from sklearn.model_selection import train_test_split

class NeuralNetwork:
    def __init__(self):
        self.model = cv2.ml.ANN_MLP_create()
        self.CreateNetwork()


    def CreateNetwork(self, layer_sizes):
        self.model.setLayerSizes(np.int32(layer_sizes))
        self.model.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
        self.model.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
        self.model.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 0.01))


def load_traning_data(file_path, input_size):
    return train_test_split()


