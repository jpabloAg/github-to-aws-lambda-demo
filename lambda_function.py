import json
import pandas as pd

def lambda_handler(event, context):
    dummyData = {
        'col1':[1,2], 
        'col2':[3,4]
    }
    df = pd.DataFrame(data = dummyData)
    print(df)
    print('Done x1')