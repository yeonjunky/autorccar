import cv2
import numpy
from glob import glob
import os
from sklearn.model_selection import train_test_split

class NeuralNetwork:

    def CreateNetwork(self, layer_sizes):
        self.model = cv2.ml.ANN_MLP_create()
        self.model.setLayerSizes(np.int32(layer_sizes))
        self.model.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
        self.model.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
        self.model.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 0.01))

    def train(self):
        self.model.train(np.float32(X), cv2.ml.ROW_SAMPLE, np.float32(Y))

    def evaluate(self):
        pass

    def save(self, path):
        self.model.save(path)

    def load(self, path):
        self.model = cv2.ml.ANN_MLP_load(path)

    def predict(self):
        pass


def load_traning_data(input_size):
    x = np.empty((0, input_size))
    y = np.empty((0, 4))

    traning_data = glob('data_image\\data*.jpg')
    if traning_data is None:
        print("image doesn't exist. quit")

    for i in traning_data:
        with np.load(i) as data:
            train = data['train']
            train_label = data['train_label']
        X = np.vstack((X, train))
        Y = np.vstack(Y, train_label)

    return train_test_split(X, Y, test_size = 0.3)
