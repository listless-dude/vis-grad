import numpy as np

class Tensor:
    def __init__(self, data, _children=(), _operation=''):
        self.data = np.array(data)
        self.prev = set(_children)
        self.op = _operation

    def __repr__(self):
        return f"Tensor(data={self.data})"

    def __add__(self, other):
        return Tensor(self.data + other.data, (self, other), '+')
    
    def __mul__(self, other):
        return Tensor(self.data * other.data, (self, other), '*')
