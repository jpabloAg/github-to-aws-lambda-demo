import json
import util as utl
import pandas as pd

def lambda_handler(event, context):
    
    operation = event['operation']
    num1 = event['num1']
    num2 = event['num2']
    print("RESULTADO DE LA OPERACION")
    if(operation == 'SUMA'):
        print(utl.suma(num1, num2))
    elif(operation == 'RESTA'):
        print(utl.resta(num1, num2))
    if(operation == 'MULTIPLICACION'):
        print(utl.multiplicacion(num1, num2))

    dummyData = {
        'col1':[1,2], 
        'col2':[3,4]
    }
    df = pd.DataFrame(data = dummyData)
    print(df)
    print('Done x4.0')
    print('DESPLIEGUE DE FUNCION LAMBDA EN PYTHON USANDO AWS CODEBUILD')