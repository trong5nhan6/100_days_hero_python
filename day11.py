import math


class ReLUActivateFunction:
    def __init__(self, tensor):
        self.tensor = tensor

    def calculate(self):
        Relu_tensor = []
        for i in range(len(self.tensor)):
            if self.tensor[i] >= 0:
                tensor = self.tensor[i]
            if self.tensor[i] < 0:
                tensor = 0
            Relu_tensor.append(tensor)
        return Relu_tensor


class SigmoidActivateFunction(ReLUActivateFunction):
    def calculate(self):
        Sigmoi_tensor = []
        for i in range(len(self.tensor)):
            tensor = 1 / (1 + math.exp(-self.tensor[i]))
            Sigmoi_tensor.append(round(tensor,4))
        return Sigmoi_tensor


tensor = [1, -5, 1.5, 2.7, -5]

Relu = ReLUActivateFunction(tensor)
Sigmoi = SigmoidActivateFunction(tensor)
print(Relu.calculate())
print(Sigmoi.calculate())
