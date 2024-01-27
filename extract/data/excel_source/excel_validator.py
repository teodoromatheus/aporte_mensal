import pandas as pd
import yfinance as fy
import os
import sys
from typing import List
from contracts.schema_excel import ExcelSchema

class ExcelValidator():
    def __init__(self):
        return None
    
    def start(self):
        if self.fileExists() == False:
            print('Arquivo Asset.xlsx não foi encontrado na pasta!')
            sys.exit()

        df = self.transformToDataframe()
        errors_schema = self.validateSchema(dataframe=df)

        if errors_schema:
            for error in errors_schema:
                print(error)
            sys.exit()

        return print(f'Validação schema OK!')
        
    def fileExists(self):
        if os.path.exists('extract/data/excel_source/Asset.xlsx'):
            return True
        else:
            return False
        
    def transformToDataframe(self) -> pd.DataFrame:
        dataframe = pd.read_excel('extract/data/excel_source/Asset.xlsx')
        return dataframe

    def validateSchema(self, dataframe: pd.DataFrame) -> List:
        errors = []
        for index, row in dataframe.iterrows():
            try:
                ExcelSchema(**row.to_dict())
            except Exception as e:
                errors.append(f'Erro na linha {index+2}: {e}')    
        return errors

    def validateUniqueAssets(self, dataframe: pd.DataFrame):
        pass

    def assetsExists(self, dataframe: pd.DataFrame):
        # TODO: Criar validação de ativo com yfinance
        pass

    def transformToList(self, dataframe: pd.DataFrame):
        # TODO: Transformar em lista para chamar classe de cotações
        pass