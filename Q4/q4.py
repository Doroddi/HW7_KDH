if __name__ == '__main__':
    import pandas as pd
    import numpy as np

    data = pd.read_csv('gender2.csv', encoding='Ansi')
    df = pd.DataFrame(data)
    
    newdf = df[['행정구역', '2022년_계_총인구수','2022년_남_총인구수', '2022년_여_총인구수']]
    newdf = newdf.set_index(keys='행정구역')

    
    newdf = newdf.rename(columns={'2022년_계_총인구수':'Total','2022년_남_총인구수':'Male','2022년_여_총인구수':'Female'})

    print(newdf)
