class SGD:
    __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grad):
        for key in params.keys():
            params[key] -= self.lr * grad[key]
