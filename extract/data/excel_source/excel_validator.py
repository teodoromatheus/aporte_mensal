import pandas as pd
import yfinance as fy
import os
import sys

class ExcelValidator():
    def __init__(self):
        return None
    
    def start(self):
        if self.fileExists() == False:
            print('Arquivo Asset.xlsx não foi encontrado na pasta!')
            sys.exit()
        
        df = self.transformToDataframe()
        return df
    
        
    def fileExists(self):
        if os.path.exists('extract/data/excel_source/Asset.xlsx'):
            return True
        else:
            return False


    def transformToDataframe(self) -> pd.DataFrame:
        dataframe = pd.read_excel('extract/data/excel_source/Asset.xlsx')
        return dataframe

    def validateSchema(self, dataframe: pd.DataFrame, schema):
        pass

    def validateUniqueAssets(self, dataframe: pd.DataFrame):
        pass

    def assetsExists(self, dataframe: pd.DataFrame):
        pass

    def transformToList(self, dataframe: pd.DataFrame):
        pass