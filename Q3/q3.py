if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    data = np.array([[1000,25],
                     [280,120],
                     [900,30]])
    
    df = pd.DataFrame(data, index=['store1', 'store2', 'store3'], columns=['unit price', 'number'])

    print(df,'\n')

    df['total price'] = df['unit price'] * df['number']

    print(df,'\n')

    df = df.sort_values(by = ['total price'], ascending = False)

    print(df.iloc[[0,1]])
