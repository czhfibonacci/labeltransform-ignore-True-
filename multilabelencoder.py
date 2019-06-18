from collections import defaultdict

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode
        self.d = defaultdict(LabelEncoder)
        self.normdict = defaultdict(list)
    def normcolumn(self,data,cols):
        output = data.copy()
        for col in cols:
            def normmap(x):
                if x not in self.normdict[col]:
                    return 'other'
                else:
                    return str(x)
            output[col] = output[col].astype(str).map(normmap)
        return output 
    
    def fit(self,X,y=None):
        # Encoding the variable
        for col in self.columns:
            self.normdict[col] = X[col].astype(str).value_counts().index.tolist()+['other']
            self.d[col].fit(self.normdict[col])

        return self # not relevant here
 
    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        
        if self.columns is not None:
                   # Using the dictionary to label future data
            output = self.normcolumn(output,self.columns)
            for col in self.columns:
                print(col)
                output[col] = self.d[col].transform(output[col].astype(str))
        return output
 
    def fit_transform(self,X,y=None):
        return self.fit(X).transform(X)
