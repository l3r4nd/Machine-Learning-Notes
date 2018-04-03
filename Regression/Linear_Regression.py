class Linearregression:
    def __init__(self, fit_intercept = True, random_state = 0):
        self.fit_intercept = fit_intercept
        self.random_state = np.random.seed(random_state)
    
    def fit(self, X, y):
        print('Training...')
        num = np.sum((X - np.mean(X)) * (y - np.mean(y)))
        denom = np.sum((X - np.mean(X))**2)
        self.slope = num/denom
        
        if self.fit_intercept == True:
            self.intercept = np.mean(y) - self.slope * np.mean(X)
        else:
            self.intecept = 0
            
        self.equation = self.intercept + np.dot(self.slope, X)
        
        return 'Training is complete!'
    
    def predict(self, X_test):
        self.pred = self.intercept + self.slope * X_test
        return self.pred
    
    def score(self, y_true, y_pred, method):
            if method == 'rmse':
                return np.sqrt(np.mean((y_true - y_pred))**2)
            if method == 'mse':
                return np.mean((y_true - y_pred)**2)
