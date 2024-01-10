import pandas as pd
import yfinance as yf
from typing import List
from datetime import datetime
import time

class CotationCollector:
    def __init_(self):
        return None

    def start(self, acoes: List):
        df = self.extractCotation(acoes=acoes)
        return df

    def extractCotation(self, acoes: List):
        data_frame_completed = pd.DataFrame()
        for acao in acoes:
            result = yf.download(tickers=f'{acao}.SA', period='1y')
            data_frame = pd.DataFrame(result).reset_index()
            data_frame = data_frame[['Date', 'Close', 'Adj Close']].assign(Acao=f'{acao}')
            data_frame_completed = pd.concat([data_frame_completed, data_frame])
        return data_frame_completed
    
    def actualDate(self):
        data_atual = datetime.today().strftime('%Y-%m-%d')
        return None