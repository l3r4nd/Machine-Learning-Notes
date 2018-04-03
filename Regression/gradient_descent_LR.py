class LinearRegressionGD:
    def __init__(self, learning_rate, epochs, random_state = 42):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.random_state = np.random.seed(random_state)
        
    def fit(self, X_train, y_train):
        b0, b1, temp0, temp1 = 0, 0, 0, 0
        N = y_train.shape[0]
        
        for i in np.arange(self.epochs):
            # y = mx + b
            y_pred = b0 + b1 * X_train
            # calculate Residual Sum of Squares(RSS)
            cost = 1/N * np.sum((y_train - y_pred)**2)
            temp0 = temp0 - self.learning_rate * -np.sum(np.mean(y_train - y_pred))
            temp1 = temp1 - self.learning_rate * -np.sum(np.mean((y_train - y_pred) * X_train))
            b0 = temp0
            b1 = temp1
            
        return b0, b1, cost
        
    def predict(self, X_test):
        y_pred = b0 + b1 * X_test
        return y_pred
