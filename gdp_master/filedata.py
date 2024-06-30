import pandas as pd
from statsmodels.regression.linear_model import OLS  

class file_data:
    def __init__(self, filename, key):              
        self.fn = filename
        self.key = key

    def get_data(self, key):                         
        X = []
        Y = []
        data2 = pd.read_csv(self.fn, encoding="ISO-8859-1")
        data1 = data2[data2['CID'] == self.key]    
        Y = data1['GDP']                           
        X = data1[['CON', 'GOV', 'CAP', 'EXP', 'IMP']]
        year = data1[['Year']]  
        return X, Y, year

class OLSModel(file_data):                              
    def __init__(self, filename, X, Y, key):        
        file_data.__init__(self, filename, key)
        self.y = Y
        self.x = X
        self.key = key

    def olsm(self):                                 
        X, Y, year = self.get_data(self.key)
        model = OLS(Y, X)  
        result = model.fit()                    
        return result

# Example usage:
filename = 'DataFinal.csv' 
key = 91  

data_handler = OLSModel(filename, None, None, key) 
result = data_handler.olsm()

print(result.summary())


	                        

