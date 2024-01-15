import pandas as pd
import yfinance as yf
from typing import List
from datetime import datetime
from contracts.schema_cotation import CotationSchema
import sys

class CotationCollector:
    def __init__(self):
        return None

    def start(self, acoes: List):
        df = self.extractCotation(acoes=acoes) 
        error_schema = self.validateDataFrame(dataframe=df)
        if error_schema:
            for error in error_schema:
                print(error)
            sys.exit()
        error_actual_date = self.validateActualDate(dataframe=df, acoes=acoes)
        if error_actual_date:
            for error in error_actual_date:
                print(error)
            sys.exit()
        return print('Extração e Validação concluída!')

    def extractCotation(self, acoes: List) -> pd.DataFrame:
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
    
    def validateActualDate(self, acoes: List, dataframe: pd.DataFrame) -> bool:
        data_atual = datetime.today().strftime('%Y-%m-%d')
        errors = []
        for acao in acoes:
            retorno = dataframe.loc[(dataframe['Asset'] == acao) & (dataframe['Date'] == data_atual)]
            if retorno.empty:
                erro = f'Ativo {acao} não tem cotação na data atual'
                errors.append(erro)
        return errors