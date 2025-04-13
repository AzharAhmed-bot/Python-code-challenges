# Data Mining Model


class DataMining:
    def __init__(self,train_set):
        self.x=[data[0] for data in train_set]
        self.y=[data[1] for data in train_set]

        self.n=len(self.x)

        self.E_x=sum(self.x)
        self.E_x2=sum([data**2 for data in self.x])
        self.E_x_squared=self.E_x**2
        self.E_y=sum(self.y)
        self.E_xy=sum(self.x[i]*self.y[i] for i in range(self.n))

        self.theta_1=(self.n*self.E_xy-(self.E_x*self.E_y))/(self.n*self.E_x2-self.E_x_squared)
        self.theta_0=(self.E_y-self.theta_1*self.E_x)/self.n

    def calculate_rmse(self):
        # The formula is:

        error_sum = sum((self.y[i] - (self.theta_0 + self.theta_1 * self.x[i])) ** 2 for i in range(self.n))
        rmse= (error_sum /self.n) **0.5
        return rmse
    
    def predict(self,x):
        y=self.theta_0+ x* self.theta_1
        # Calculate the RMSE
        return y
    



example_train_set = [(0, 1),(2, 2),(4, 3),(9, 8),(3, 5)]
data_mining=DataMining(example_train_set)
print(data_mining.predict(1))  # Example prediction
print(data_mining.predict(2))  # Example prediction
print(data_mining.predict(3))  # Example prediction

print(data_mining.calculate_rmse()) 