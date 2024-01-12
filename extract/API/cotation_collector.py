import pandas as pd
import yfinance as yf
from typing import List
from datetime import datetime
from contracts.schema_cotation import CotationSchema

class CotationCollector:
    def __init__(self):
        return None

    def start(self, acoes: List):
        df = self.extractCotation(acoes=acoes)
        errors = self.validateDataFrame(dataframe=df)
        return errors

    def extractCotation(self, acoes: List):
        data_frame_completed = pd.DataFrame()
        for acao in acoes:
            result = yf.download(tickers=f'{acao}.SA', period='1y')
            data_frame = pd.DataFrame(result).reset_index()
            data_frame = data_frame[['Date', 'Close', 'Adj Close']].assign(Asset=f'{acao}')
            data_frame_completed = pd.concat([data_frame_completed, data_frame])
        
        data_frame_completed.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)
        return data_frame_completed
    
    def validateDataFrame(self, dataframe: pd.DataFrame) -> List:
        errors = []
        for index, row in dataframe.iterrows():
            try:
                CotationSchema(**row.to_dict())
            except Exception as e:
                errors.append(f'Erro na linha {index+2}: {e}')
        return errors
    
    def actualDate(self):
        data_atual = datetime.today().strftime('%Y-%m-%d')
        return None