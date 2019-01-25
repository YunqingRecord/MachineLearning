import numpy as np


class Perceptron():
    def __init__(self, dataSet, labels):
        self.dataSet = np.array(dataSet)
        self.labels = np.array(labels).transpose()  # make it to list
        self.weight = np.random.random()
        self.bias = 0
        self.iteration = 3000
        self.LR = 0.05

    def activation(self, y):
        if y > 0:
            return 1
        else:
            return -1

    def training(self):
        '''
        :args: judge the outcome from currently hyper plain and the ture label[i] then update the weight and bias
        :return:
        '''
        m, n = np.shape(self.dataSet)
        self.weight = np.random.random(n)
        self.bias = 1
        for i in range(self.iteration):
            for j in range(m):
                output = np.dot(self.weight, self.dataSet[j]) + self.bias
                if self.labels[j] * output < 0:
                    self.weight += self.LR*self.labels[j]*self.dataSet[j]
                    self.bias += self.LR*self.labels[j]
                    print(self.weight, self.bias)
        return None

    def predict(self, x):
        outcome = np.dot(x, self.weight) + self.bias
        prediction = np.where(outcome > 0, 1, -1)
        return prediction


if __name__ == '__main__':
    dataSet = np.array(
        [[3, 3],
         [4, 3],
         [199, 999]])
    labels = [1, 1, -1]

    perceptron = Perceptron(dataSet, labels)
    perceptron.training()
    prediction = perceptron.predict(dataSet)
    print(prediction)
